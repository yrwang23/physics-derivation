#!/usr/bin/env python3
"""
render_katex.py — 将包含 LaTeX 公式的 markdown 文件渲染为 KaTeX 网页。

用法:
    python3 render_katex.py <输入.md> [--output <输出.html>]
    python3 render_katex.py --stdin [--title "推导标题"] [--output <输出.html>]

输出是一个自包含的 HTML 文件，通过 CDN 加载 KaTeX 渲染数学公式。
用 codex 侧边栏的 in-app browser 打开，可对照聊天内容查看。
"""
import argparse
import os
import re
import sys
import html as html_mod

# KaTeX CDN 版本
KATEX_VERSION = "0.16.21"

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{katex_ver}/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@{katex_ver}/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@{katex_ver}/dist/contrib/auto-render.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #e0e0e0;
    background: #1a1a2e;
    max-width: 860px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
  }}
  h1 {{ font-size: 1.6rem; color: #f0f0f0; border-bottom: 1px solid #333; padding-bottom: 0.5rem; margin: 1.5rem 0 1rem; }}
  h2 {{ font-size: 1.25rem; color: #e0e0f0; margin: 1.5rem 0 0.75rem; }}
  h3 {{ font-size: 1.1rem; color: #d0d0e0; margin: 1.2rem 0 0.5rem; }}
  p {{ margin: 0.75rem 0; }}
  ul, ol {{ margin: 0.5rem 0 0.5rem 1.5rem; }}
  li {{ margin: 0.3rem 0; }}
  code {{
    font-family: "JetBrains Mono", "Fira Code", "Consolas", monospace;
    font-size: 0.9em;
    background: #2a2a3e;
    padding: 0.15em 0.4em;
    border-radius: 3px;
  }}
  pre {{
    background: #12121e;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    overflow-x: auto;
    margin: 0.75rem 0;
  }}
  pre code {{ background: none; padding: 0; }}
  blockquote {{
    border-left: 3px solid #4a4a6a;
    padding-left: 1rem;
    margin: 0.75rem 0;
    color: #b0b0c0;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 0.75rem 0;
  }}
  th, td {{
    border: 1px solid #333;
    padding: 0.4rem 0.6rem;
    text-align: left;
  }}
  th {{ background: #22223a; }}
  tr:nth-child(even) {{ background: #1e1e32; }}
  hr {{ border: none; border-top: 1px solid #333; margin: 1.5rem 0; }}
  .katex {{ font-size: 1.05em !important; }}
  .katex-display > .katex {{ font-size: 1.1em !important; }}
  .step-marker {{
    display: inline-block;
    background: #3a3a5a;
    color: #c0c0e0;
    font-size: 0.85em;
    font-weight: 600;
    padding: 0.15em 0.6em;
    border-radius: 4px;
    margin-right: 0.5em;
  }}
</style>
</head>
<body>
<div id="content">
{body}
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {{
    renderMathInElement(document.getElementById('content'), {{
      delimiters: [
        {{left: '$$', right: '$$', display: true}},
        {{left: '$', right: '$', display: false}}
      ],
      trust: true,
      strict: false
    }});
  }});
</script>
</body>
</html>"""


def md_to_html(text):
    """Convert basic markdown to HTML, preserving LaTeX math."""
    lines = text.split('\n')
    result = []
    in_code_block = False
    in_math_block = False
    code_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                result.append('<pre><code>' + html_mod.escape('\n'.join(code_buffer)) + '</code></pre>')
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # Math display blocks ($$...$$) — keep as-is for KaTeX
        if line.strip().startswith('$$'):
            in_math_block = not in_math_block
            result.append(line)
            i += 1
            continue

        if in_math_block:
            result.append(line)
            i += 1
            continue

        # Empty line = paragraph break
        if not line.strip():
            result.append('')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', line.strip()):
            result.append('<hr>')
            i += 1
            continue

        # Headers
        h_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h_match:
            level = len(h_match.group(1))
            content = inline_md(h_match.group(2))
            result.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            bq_content = []
            while i < len(lines) and lines[i].startswith('> '):
                bq_content.append(inline_md(lines[i][2:]))
                i += 1
            result.append('<blockquote>' + '<br>'.join(bq_content) + '</blockquote>')
            continue

        # Unordered list
        ul_match = re.match(r'^[\-\*]\s+(.+)$', line)
        if ul_match:
            items = []
            while i < len(lines):
                m = re.match(r'^[\-\*]\s+(.+)$', lines[i])
                if m:
                    items.append('<li>' + inline_md(m.group(1)) + '</li>')
                    i += 1
                else:
                    break
            result.append('<ul>' + ''.join(items) + '</ul>')
            continue

        # Ordered list
        ol_match = re.match(r'^\d+\.\s+(.+)$', line)
        if ol_match:
            items = []
            while i < len(lines):
                m = re.match(r'^\d+\.\s+(.+)$', lines[i])
                if m:
                    items.append('<li>' + inline_md(m.group(1)) + '</li>')
                    i += 1
                else:
                    break
            result.append('<ol>' + ''.join(items) + '</ol>')
            continue

        # Table
        if '|' in line and line.strip().startswith('|'):
            rows = []
            while i < len(lines) and '|' in lines[i]:
                rows.append(lines[i])
                i += 1
            result.append(table_to_html(rows))
            continue

        # Regular paragraph
        result.append('<p>' + inline_md(line) + '</p>')
        i += 1

    # Handle unclosed code block
    if in_code_block and code_buffer:
        result.append('<pre><code>' + html_mod.escape('\n'.join(code_buffer)) + '</code></pre>')

    return '\n'.join(result)


def inline_md(text):
    """Convert inline markdown (bold, italic, code, links)."""
    # Escape HTML first, then apply markdown
    text = html_mod.escape(text, quote=False)
    # Preserve LaTeX math delimiters (they're already escaped by html.escape...)
    # Actually html.escape doesn't escape $, so LaTeX is preserved.

    # Bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

    # Italic (*text*)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)

    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" style="color: #7aa2f7;">\1</a>', text)

    return text


def table_to_html(rows):
    """Convert markdown table to HTML."""
    if len(rows) < 1:
        return ''

    headers = [c.strip() for c in rows[0].strip().strip('|').split('|')]
    # Skip separator row (index 1)
    data_rows = rows[2:] if len(rows) > 2 else []

    html = '<table><thead><tr>'
    for h in headers:
        html += f'<th>{h}</th>'
    html += '</tr></thead><tbody>'

    for row in data_rows:
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        html += '<tr>'
        for c in cells:
            html += f'<td>{inline_md(c)}</td>'
        html += '</tr>'

    html += '</tbody></table>'
    return html


def main():
    parser = argparse.ArgumentParser(description='将 LaTeX markdown 渲染为 KaTeX 网页')
    parser.add_argument('input', nargs='?', help='输入 markdown 文件路径')
    parser.add_argument('--output', '-o', help='输出 HTML 文件路径')
    parser.add_argument('--title', '-t', default='物理公式推导', help='网页标题')
    parser.add_argument('--stdin', action='store_true', help='从 stdin 读取输入')
    args = parser.parse_args()

    # Read input
    if args.stdin:
        content = sys.stdin.read()
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        parser.print_help()
        sys.exit(1)

    # Determine output path
    if args.output:
        output_path = args.output
    elif args.input:
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        output_path = os.path.join(os.path.dirname(args.input) or '.', base_name + '.html')
    else:
        output_path = 'derivation.html'

    # Convert markdown to HTML body
    body_html = md_to_html(content)

    # Fill template
    full_html = HTML_TEMPLATE.format(
        title=html_mod.escape(args.title),
        katex_ver=KATEX_VERSION,
        body=body_html
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f'Rendered: {output_path}')
    print(f'File size: {os.path.getsize(output_path)} bytes')


if __name__ == '__main__':
    main()

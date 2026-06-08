#!/usr/bin/env python3
"""
add_knowledge.py — 添加或更新知识库条目（支持 YAML frontmatter 解析和分类导入）。

用法:
    # 交互式（从 stdin 读取内容）
    python3 add_knowledge.py --type theory --name "条目名" --category "量子多体" --topics 主题1 主题2

    # 从已有文件导入（自动解析 YAML frontmatter）
    python3 add_knowledge.py --content input.txt

    # 批量导入目录下所有 txt 文件
    python3 add_knowledge.py --batch ./extracted-notes/
"""
import argparse
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR = os.path.join(BASE_DIR, "knowledge-base")
USER_DIR = os.path.join(KB_DIR, "user-added")

# 分类目录映射
CATEGORY_DIRS = {
    "量子多体": "量子多体",
    "量子信息与神经网络": "量子信息与神经网络",
    "凝聚态计算": "凝聚态计算",
    "其他": "其他",
}


def parse_frontmatter(text):
    """Parse YAML-like frontmatter from text. Returns (metadata, body)."""
    meta = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not match:
        return meta, text

    body = text[match.end():]
    for line in match.group(1).split('\n'):
        line = line.strip()
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip().lower()
            val = val.strip().strip('"').strip("'")
            if key in ('topics', 'prerequisites'):
                # Parse list: ["a", "b"] or - "a"\n  - "b"
                val_list = re.findall(r'"([^"]+)"', val)
                if not val_list:
                    val_list = re.findall(r'-\s+"?([^"\n]+)"?', match.group(1).split(key)[1])
                meta[key] = val_list
            else:
                meta[key] = val
    return meta, body


def update_index(category, name, filename, topics):
    """Add a new entry to the personal knoeledge base section of INDEX.md."""
    index_path = os.path.join(KB_DIR, "INDEX.md")
    if not os.path.exists(index_path):
        print("Error: INDEX.md not found")
        return

    cat_dir = CATEGORY_DIRS.get(category, "其他")
    link = f"[{name}](./user-added/{cat_dir}/{filename})"
    topic_str = ", ".join(topics) if topics else "TBD"

    with open(index_path, "r") as f:
        content = f.read()

    # Find the correct category section
    section_markers = {
        "量子多体": "### 📐 量子多体 (many-body/)",
        "量子信息与神经网络": "### 🔬 量子信息与神经网络 (qinfo-nn/)",
        "凝聚态计算": "### 💻 凝聚态计算 (comp-cond-mat/)",
        "其他": "### 📦 其他 (other/)",
    }

    marker = section_markers.get(category)
    if not marker:
        print(f"Unknown category: {category}")
        return

    lines = content.split("\n")
    new_lines = []
    in_section = False
    inserted = False

    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == marker:
            in_section = True
        if in_section and not inserted:
            # Insert after the section marker, before the next section or empty placeholder
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith("*暂无条目*") or next_line.startswith("###"):
                    new_lines.append(f"| {name} | {link} | {topic_str} |")
                    # Also remove placeholder
                    if next_line.startswith("*暂无条目*"):
                        pass  # Will be handled below
                    inserted = True
                    in_section = False

    if not inserted:
        topic_str = ", ".join(topics) if topics else "TBD"
        new_lines.append(f"| {name} | {link} | {topic_str} |")

    # Write back
    with open(index_path, "w") as f:
        f.write("\n".join(new_lines))
    print(f"Updated INDEX.md: added '{name}' to {category}")


def main():
    parser = argparse.ArgumentParser(description="Add knowledge to physics derivation KB")
    parser.add_argument("--type", choices=["theory", "math-tool"], help="Type of entry")
    parser.add_argument("--name", help="Display name")
    parser.add_argument("--category", choices=list(CATEGORY_DIRS.keys()),
                        default="其他", help="Knowledge category")
    parser.add_argument("--topics", nargs="*", default=[], help="Topics")
    parser.add_argument("--content", help="Path to input file (with YAML frontmatter)")
    parser.add_argument("--batch", help="Directory containing multiple .txt files to import")

    args = parser.parse_args()

    if args.batch:
        # Batch import mode
        batch_dir = args.batch
        for fname in sorted(os.listdir(batch_dir)):
            if not fname.endswith(('.txt', '.md')):
                continue
            fpath = os.path.join(batch_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                text = f.read()
            meta, body = parse_frontmatter(text)
            if not meta.get('name'):
                print(f"Skipping {fname}: no name in frontmatter")
                continue
            process_entry(meta, body)
        return

    if args.content:
        with open(args.content, 'r', encoding='utf-8') as f:
            text = f.read()
        meta, body = parse_frontmatter(text)
        if not meta.get('name'):
            meta['name'] = args.name or os.path.splitext(os.path.basename(args.content))[0]
        if not meta.get('type'):
            meta['type'] = args.type or "theory"
        if not meta.get('category'):
            meta['category'] = args.category
        if not meta.get('topics'):
            meta['topics'] = args.topics
        process_entry(meta, body)
        return

    # Interactive mode
    if not args.name:
        parser.print_help()
        return

    print(f"Enter content for '{args.name}' (press Ctrl+D when done):")
    body = sys.stdin.read()
    meta = {
        'name': args.name,
        'type': args.type or 'theory',
        'category': args.category,
        'topics': args.topics,
    }
    process_entry(meta, body)


def process_entry(meta, body):
    """Process a single entry: write file and update INDEX."""
    name = meta.get('name', 'Unnamed')
    entry_type = meta.get('type', 'theory')
    category = meta.get('category', '其他')
    topics = meta.get('topics', [])

    cat_dir = CATEGORY_DIRS.get(category, "其他")
    target_dir = os.path.join(USER_DIR, cat_dir)
    os.makedirs(target_dir, exist_ok=True)

    # Generate filename
    filename = name.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "") + ".md"

    # Full file content (with reconstructed frontmatter)
    prereqs = meta.get('prerequisites', [])
    content = "---\n"
    content += f'name: "{name}"\n'
    content += f'type: {entry_type}\n'
    content += f'category: "{category}"\n'
    content += f'topics: {topics}\n'
    if prereqs:
        content += "prerequisites:\n"
        for p in prereqs:
            content += f'  - "{p}"\n'
    content += "---\n\n"
    content += body

    target_file = os.path.join(target_dir, filename)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {target_file}")

    update_index(category, name, filename, topics)
    print(f"Done! Added '{name}' to {category}.")


if __name__ == "__main__":
    main()

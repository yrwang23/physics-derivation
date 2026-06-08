---
name: physics-derivation
description: Trace and derive physics formulas from academic papers, with a personalized knowledge base. Use when Codex needs to (1) explain how a physics formula is derived from first principles, (2) trace a formula back through its reference chain, (3) build step-by-step derivation documents linking to the user's existing physics knowledge, (4) update the user's knowledge base with new concepts learned during derivation, or (5) save and organize reference papers for formula tracing. Designed for users with condensed matter, quantum information, and quantum AI background.
---

# Physics Derivation

## 概述

本 skill 帮助用户从物理 paper 中推导公式。核心思路是：**以推导为主线，在每一步需要某个概念或方法时停下来，展示其作用，询问用户是否了解，然后继续。** 全部输出使用中文。推导完成后生成 KaTeX 渲染的 HTML 网页，供用户在侧边栏对照查看。

---

## 知识库结构

### 参考材料库 (Reference Library)

位于 `knowledge-base/theories/` 和 `knowledge-base/math-tools/`，预置了本科水平的物理理论和数学工具条目。仅供 agent 查阅公式定义用，**绝不能默认用户已掌握**。

### 个人知识库 (Personal Knowledge Base)

位于 `knowledge-base/user-added/`，**初始为空**，按以下领域分类存放：

| 目录 | 分类 | 内容 |
|------|------|------|
| `量子多体/` | 📐 量子多体 | 多体理论工具：二次量子化、格林函数、路径积分等 |
| `量子信息与神经网络/` | 🔬 量子信息与神经网络 | 量子信息、量子计算、量子AI、神经网络量子态 |
| `凝聚态计算/` | 💻 凝聚态计算 | DMFT、QMC、DMRG、DFT 等数值方法 |
| `其他/` | 📦 其他 | 不属于以上分类的知识 |

当用户提供新知识点时，**必须询问用户属于哪个分类**，然后放入对应子目录。

---

## 推导工作流

### 总则

- **所有对用户的输出使用中文**
- **推导是主线，确认知识自然嵌入其中**
- **不默认用户了解任何概念**
- **展示方法的作用优先于展示定义**

### 流程

**第 1 步：理解公式与上下文** — 确认用户的需求，如用户有 PDF 请其保存到 `papers/`

**第 2 步：开始在推导中嵌入确认** — 从知识库中最基础的起点出发，逐步推导。每到一个需要新概念/方法的步骤：
  1. 展示该概念的作用，询问用户是否了解
  2. 了解 → 入库 → 继续；不了解 → 教学 → 入库 → 继续
  3. 入库时询问用户该知识点属于哪个分类

**第 3 步：生成 KaTeX 渲染视图** — 推导完成后：
  1. 将完整推导整理为 markdown 文件（含 LaTeX）
  2. 运行 `scripts/render_katex.py` 生成 HTML
  3. 用 in-app browser 打开供对照查看

**第 4 步：迭代问答** — 用户追问时回到第 2 步处理新知识点

> 详细流程参见 `references/workflow.md`

---

## KaTeX 渲染说明

推导过程中 chat 里使用 Unicode 符号确保可选中。推导完成后用 `render_katex.py` 将 LaTeX 渲染为 HTML 页面。

```bash
python3 scripts/render_katex.py 输入.md --title "标题" --output 输出.html
```

---

## 目录结构

```
physics-derivation/
  SKILL.md
  agents/openai.yaml
  knowledge-base/
    INDEX.md
    theories/                     # 参考材料：物理理论
    math-tools/                   # 参考材料：数学工具
    user-added/                   # 个人知识库（按分类子目录）
      量子多体/
      量子信息与神经网络/
      凝聚态计算/
      其他/
  papers/
  references/
    workflow.md
    derivation-template.md
    kb-entry-spec.md              # 给其他 AI 的输入规范
  scripts/
    add_knowledge.py
    render_katex.py
```

## 参考文件

- `references/workflow.md` — 完整的工作流说明
- `references/derivation-template.md` — 推导文档模板
- `references/kb-entry-spec.md` — 知识条目输入规范（给其他 AI 整理笔记用）

## 脚本

- `scripts/add_knowledge.py` — 添加知识条目（需指定分类）
- `scripts/render_katex.py` — 将 LaTeX 渲染为 KaTeX 网页

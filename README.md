# Physics Derivation Skill

一个为 Codex 定制的物理公式推导 skill，拥有个性化的知识库，能够逐步引导推导过程。

---

## 这是什么？

这是一个用于 [Codex](https://codex.openai.com) 的 skill，专门帮助物理方向的研究生从学术论文中**逐步推导物理公式**。它的核心工作方式是：

1. 你提出一个要推导的公式
2. Agent 从知识库中最基础的起点出发，**一步一确认**地推导
3. 每步需要用新概念或新方法时，**先展示它在当前步骤中的作用**，然后问你"这个了解吗？"
4. 了解 → 入库 → 继续；不了解 → 教学 → 入库 → 继续
5. 推导完成后可生成完整推导文档

所有输出使用中文，公式使用标准 LaTeX 格式。

---

## 知识库结构

知识库分为两部分：

### 参考材料库 (Reference Library)

预置的本科水平物理理论和数学工具条目，供 Agent 查阅公式定义用，**不代表用户已掌握**。

```
knowledge-base/theories/       # 7 个理论
knowledge-base/math-tools/     # 8 个数学工具
```

### 个人知识库 (Personal Knowledge Base)

记录你确认已掌握的知识，**初始为空**，按领域分类存放：

| 目录 | 领域 | 条目数 |
|------|------|--------|
| `量子多体/` | 多体理论、固体物理基础 | 23 |
| `凝聚态计算/` | DFT、NEGF、PAW 等计算方法 | 6 |
| `量子信息与神经网络/` | — | 0 |
| `其他/` | — | 0 |

---

## 使用方法

### 在 Codex 中触发

安装后，当你向 Codex 提出类似以下问题时，会自动触发此 skill：

> "帮我推导这个物理公式，一步步来，需要用到什么方法先告诉我作用再问我是否了解。"

### 知识库更新

新知识点在推导过程中自动添加，Agent 会询问你所属分类。

你也可以用另一个 AI 从 PDF 笔记中提取知识点：

1. 将 `references/kb-entry-spec.md` 发给那个 AI
2. 它按模板生成结构化 `.txt` 文件
3. 发回给 Codex，自动导入知识库

---

## 分类体系

```
user-added/
├── 📐 量子多体 /              ← 多体理论与固体物理基础
├── 🔬 量子信息与神经网络 /   ← 量子信息、量子AI
├── 💻 凝聚态计算 /            ← DFT、DMFT、NEGF 等
└── 📦 其他 /                  ← 以上均不属于
```

---

## 文件结构

```
physics-derivation/
├── SKILL.md                    # Skill 核心指令
├── README.md                   # 本文件
├── agents/openai.yaml          # UI 元数据
├── knowledge-base/
│   ├── INDEX.md                # 索引（参考材料库 + 个人知识库）
│   ├── theories/               # 参考材料：物理理论
│   ├── math-tools/             # 参考材料：数学工具
│   └── user-added/             # 个人知识库（按分类子目录）
│       ├── 量子多体/
│       ├── 量子信息与神经网络/
│       ├── 凝聚态计算/
│       └── 其他/
├── papers/                     # 参考文献 PDF
├── references/
│   ├── workflow.md             # 推导工作流说明
│   ├── derivation-template.md  # 推导文档模板
│   └── kb-entry-spec.md        # 知识条目输入规范
└── scripts/
    └── add_knowledge.py        # 添加知识条目
```

---

## 安装

将本仓库放入 `~/.codex/skills/`（或 `$CODEX_HOME/skills/`）即可自动发现：

```bash
git clone https://github.com/yrwang23/physics-derivation.git ~/.codex/skills/physics-derivation
```

## 依赖

- Codex 桌面版
- `python3`（用于运行脚本）

---

## 关于

- **作者**: Yiran Wang
- **方向**: 凝聚态理论 / 量子信息 / 量子人工智能

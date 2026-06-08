# 知识库索引

本知识库分为两部分：

1. **参考材料库 (Reference Library)** — 由 skill 预置的物理理论和数学工具条目。
   agent 可以在需要查阅公式或概念定义时参考这些条目。
   **重要：这些条目的存在不代表用户已经掌握。** agent 在使用它们之前必须先询问用户是否了解。

2. **个人知识库 (Personal Knowledge Base)** — 记录用户确认已掌握的知识，按领域分类存放。
   初始为空，通过对话逐步添加。

---

## 参考材料库

### 理论 (theories/)

| 条目 | 文件 | 涵盖主题 |
|------|------|----------|
| 经典力学 | [theories/classical-mechanics.md](./theories/classical-mechanics.md) | 牛顿力学, 拉格朗日力学, 哈密顿力学, 分析力学 |
| 电动力学 | [theories/electrodynamics.md](./theories/electrodynamics.md) | 麦克斯韦方程组, 电磁波, 辐射, 狭义相对论 |
| 量子力学 | [theories/quantum-mechanics.md](./theories/quantum-mechanics.md) | 薛定谔方程, 算符, 自旋, 微扰论, 散射 |
| 热力学与统计物理 | [theories/thermodynamics-statmech.md](./theories/thermodynamics-statmech.md) | 热力学定律, 系综, 相变, 临界现象 |
| 原子物理 | [theories/atomic-physics.md](./theories/atomic-physics.md) | 原子结构, 光谱, 精细结构, 塞曼效应 |
| 固体物理基础 | [theories/solid-state-physics.md](./theories/solid-state-physics.md) | 晶体结构, 能带论, 声子, 电子输运 |
| 数学物理方法 | [theories/math-methods.md](./theories/math-methods.md) | 复变函数, 数理方程, 特殊函数, 群论初步 |

### 数学工具 (math-tools/)

| 条目 | 文件 | 涵盖主题 |
|------|------|----------|
| 变分法 | [math-tools/variational-method.md](./math-tools/variational-method.md) | Euler-Lagrange 方程, 泛函导数 |
| 微扰论 | [math-tools/perturbation-theory.md](./math-tools/perturbation-theory.md) | 非简并微扰, 简并微扰, 含时微扰 |
| 线性代数 | [math-tools/linear-algebra.md](./math-tools/linear-algebra.md) | 矩阵, 本征值问题, 张量积 |
| 群论与对称性 | [math-tools/group-theory.md](./math-tools/group-theory.md) | 群表示论, Lie 群, 对称性分析 |
| 量子多体路径积分 | [math-tools/path-integral.md](./math-tools/path-integral.md) | Trotter 近似, 配分函数, 相空间泛函积分, QMC 基础 |
| 格林函数方法 | [math-tools/green-function.md](./math-tools/green-function.md) | 微分方程格林函数, 推迟/超前格林函数 |
| 傅里叶分析 | [math-tools/fourier-analysis.md](./math-tools/fourier-analysis.md) | Fourier 变换, 卷积, 采样定理 |
| 蒙特卡洛方法 | [math-tools/monte-carlo.md](./math-tools/monte-carlo.md) | Metropolis 算法, 重要性采样, 马尔可夫链 |

---

## 个人知识库 (Personal Knowledge Base)

按领域分类，每个分类对应一个子目录。

### 📐 量子多体 (many-body/)

| 条目 | 文件 | 涵盖主题 |
|------|------|----------|
| 二次量子化 | [user-added/量子多体/second-quantization.md](./user-added/量子多体/second-quantization.md) | 产生湮灭算符, 费米子反对易, 玻色子对易, 单体/双体算符 |
| 系综理论与量子力学绘景 | [user-added/量子多体/ensemble-theory-and-pictures.md](./user-added/量子多体/ensemble-theory-and-pictures.md) | 统计力学, 时间演化, Dyson 级数, 相互作用绘景 |
| Hubbard 模型 | [user-added/量子多体/hubbard-model.md](./user-added/量子多体/hubbard-model.md) | 强关联电子, 莫特绝缘体, 跳跃积分, 库仑相互作用 |
| 平均场与 HF 近似 | [user-added/量子多体/mean-field-hartree-fock.md](./user-added/量子多体/mean-field-hartree-fock.md) | Mean Field Theory, 自洽场, Hartree 项, Fock 项 |
| 路径积分与泛函积分 | [user-added/量子多体/functional-integral.md](./user-added/量子多体/functional-integral.md) | Grassmann 数, 配分函数泛函积分, Hubbard-Stratonovich 变换 |
| Matsubara 格林函数 | [user-added/量子多体/matsubara-green-function.md](./user-added/量子多体/matsubara-green-function.md) | 虚时格林函数, Dyson 方程, 解析延拓, 谱函数 |
| 格林函数基础理论 | [user-added/量子多体/many-body-green-function.md](./user-added/量子多体/many-body-green-function.md) | 推迟格林函数, Lehmann 表示, EOM, 态密度 |
| Lippmann-Schwinger 方程 | [user-added/量子多体/lippmann-schwinger.md](./user-added/量子多体/lippmann-schwinger.md) | 散射理论, 传播子, 积分方程 |
| Dyson 方程 | [user-added/量子多体/dyson-equation.md](./user-added/量子多体/dyson-equation.md) | 完整格林函数, 裸格林函数, 自能, 几何级数 |
| 杂质模型基础 | [user-added/量子多体/impurity-models.md](./user-added/量子多体/impurity-models.md) | 共振能级, Anderson 杂质, 自能, U 项退耦 |
| Cavity 方法 | [user-added/量子多体/cavity-method.md](./user-added/量子多体/cavity-method.md) | 空穴法, 作用量分解, 有效杂质, Anderson 杂质模型 |
| DMFT 无穷维严格性 | [user-added/量子多体/dmft-infinite-dimension.md](./user-added/量子多体/dmft-infinite-dimension.md) | 标度律, 态密度高斯分布, 局域自能, Cavity 对角化 |
| 倒格子与晶面间距 | [user-added/量子多体/reciprocal-lattice.md](./user-added/量子多体/reciprocal-lattice.md) | 固体物理, 晶体结构, 倒空间 |
| 离子晶体结合与体变模量 | [user-added/量子多体/ionic-bonding-bulk-modulus.md](./user-added/量子多体/ionic-bonding-bulk-modulus.md) | 固体物理, 离子结合, 马德隆常数, 体变模量 |
| 共价结合与LCAO模型 | [user-added/量子多体/covalent-bonding-lcao.md](./user-added/量子多体/covalent-bonding-lcao.md) | 固体物理, 共价键, 分子轨道 |
| 一维单原子链晶格振动 | [user-added/量子多体/monatomic-chain-phonon.md](./user-added/量子多体/monatomic-chain-phonon.md) | 固体物理, 晶格动力学, 简正坐标 |
| 一维双原子链与光学/声学支 | [user-added/量子多体/diatomic-chain-phonon.md](./user-added/量子多体/diatomic-chain-phonon.md) | 固体物理, 声学支, 光学支, 色散关系 |
| 三维晶格振动与玻恩-卡曼条件 | [user-added/量子多体/born-von-karman-3d.md](./user-added/量子多体/born-von-karman-3d.md) | 固体物理, 玻恩-卡曼边界条件, 态密度 |
| 固体热容模型 | [user-added/量子多体/solid-heat-capacity.md](./user-added/量子多体/solid-heat-capacity.md) | 固体物理, 爱因斯坦模型, 德拜理论 |
| 晶体X射线衍射原理 | [user-added/量子多体/xray-diffraction.md](./user-added/量子多体/xray-diffraction.md) | 固体物理, X射线衍射, 劳厄方程, 布拉格方程 |
| 结构因子与系统消光 | [user-added/量子多体/structure-factor.md](./user-added/量子多体/structure-factor.md) | 固体物理, 结构因子, 系统消光 |
| 能带论基础与布洛赫定理 | [user-added/量子多体/bloch-theorem.md](./user-added/量子多体/bloch-theorem.md) | 固体物理, 能带理论, 布洛赫定理 |
| 近自由电子近似 | [user-added/量子多体/nearly-free-electron.md](./user-added/量子多体/nearly-free-electron.md) | 固体物理, 近自由电子近似, 能隙 |

### 🔬 量子信息与神经网络 (qinfo-nn/)

*暂无条目*

### 💻 凝聚态计算 (comp-cond-mat/)

| 条目 | 文件 | 涵盖主题 |
|------|------|----------|
| 泛函与泛函导数 | [user-added/凝聚态计算/functional-derivative.md](./user-added/凝聚态计算/functional-derivative.md) | 密度泛函理论基础, 泛函分析, von Weizsacker 动能 |
| Hartree-Fock 方法 | [user-added/凝聚态计算/hartree-fock-method.md](./user-added/凝聚态计算/hartree-fock-method.md) | 量子化学, Slater 行列式, Roothaan-Hall 方程 |
| Kohn-Sham 密度泛函理论 | [user-added/凝聚态计算/kohn-sham-dft.md](./user-added/凝聚态计算/kohn-sham-dft.md) | KS-DFT, 交换关联泛函, 自洽场 SCF |
| 平面波基组与布洛赫定理 | [user-added/凝聚态计算/plane-wave-basis.md](./user-added/凝聚态计算/plane-wave-basis.md) | 固体物理, 能带理论, 截断能 |
| 开放量子系统输运与NEGF | [user-added/凝聚态计算/negf-quantum-transport.md](./user-added/凝聚态计算/negf-quantum-transport.md) | 量子输运, 非平衡格林函数, Landauer 公式 |
| PAW 方法 | [user-added/凝聚态计算/paw-method.md](./user-added/凝聚态计算/paw-method.md) | PAW理论, 第一性原理, 投影缀加波 |

### 📦 其他 (other/)

*暂无条目*

---

## 添加新知识时的规范

当用户提供新的知识点时：
1. 询问用户这个知识点属于哪个分类（量子多体 / 量子信息与神经网络 / 凝聚态计算 / 其他）
2. 将文件放入对应的子目录
3. 在对应的分类表格中添加一行
4. 如果新增分类需要与用户确认分类名称

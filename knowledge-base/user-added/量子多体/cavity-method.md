# Cavity 方法 (空穴法)

## 简介
从多体晶格问题中提取单格点有效动力学的标准方法。将目标格点从晶格中"挖出"（形成空穴），其余部分作为热库，对热库自由度积分后得到目标格点的有效作用量。是 DMFT 的核心推导工具。

## 关键公式
- 作用量分解: $S = S_0 + S_{\text{bath}} + S_{\text{mix}}$
  - $S_0$: 目标格点的局域项（化学势 + 相互作用）
  - $S_{\text{bath}}$: 其余格点的全部作用量
  - $S_{\text{mix}}$: 目标格点与 bath 的耦合（跳跃项）
- 有效作用量: $\displaystyle e^{-S_{\text{eff}}[\bar\psi_0, \psi_0]} = \frac{1}{Z_{\text{bath}}} \int \mathcal{D}[\bar\psi^{(0)}, \psi^{(0)}]\, e^{-S_{\text{bath}}[\bar\psi^{(0)}, \psi^{(0)}] - S_{\text{mix}}[\bar\psi_0, \psi_0; \bar\psi^{(0)}, \psi^{(0)}]}$
- 结果形式为 Anderson 杂质模型: $S_{\text{eff}}$ 包含局域相互作用项 $U n_\uparrow n_\downarrow$ 和 bath 诱导的动力学耦合项

## 先修知识
- [Hubbard 模型](./hubbard-model.md)
- [路径积分与泛函积分](./functional-integral.md)
- [Matsubara 格林函数](./matsubara-green-function.md)

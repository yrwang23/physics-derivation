# 路径积分与泛函积分 (Path Integral / Functional Integral)

## 简介
Feynman 路径积分的推广到场论和统计物理。在多体问题中，将配分函数表示为 Grassmann 数（费米子）或复数（玻色子）的泛函积分，是推导 DMFT 和进行微扰展开的核心数学框架。

## 关键公式
- 有限温度配分函数的泛函积分:
  $Z = \int \mathcal{D}[\bar\psi, \psi] \, e^{-S[\bar\psi, \psi]}$
- 费米子作用量:
  $S[\bar\psi, \psi] = \int_0^\beta d\tau \left[ \sum_i \bar\psi_i(\tau) (\partial_\tau - \mu) \psi_i(\tau) + H[\bar\psi, \psi] \right]$
- Grassmann 高斯积分:
  $\int \prod_i d\bar\psi_i d\psi_i \, e^{-\sum_{ij} \bar\psi_i A_{ij} \psi_j} = \det A$
- Hubbard-Stratonovich 变换: 将四次型 $\bar\psi \bar\psi \psi\psi$ 通过引入辅助场化为二次型

## 先修知识
- [二次量子化](./second-quantization.md)
- [量子力学](../theories/quantum-mechanics.md)
- [格林函数方法](../math-tools/green-function.md)
- [热力学与统计物理](../theories/thermodynamics-statmech.md)

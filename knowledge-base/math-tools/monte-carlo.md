# 蒙特卡洛方法 (Monte Carlo Methods)

## 简介
利用随机采样近似计算复杂系统的统计性质。广泛用于统计物理模拟和量子多体问题的计算。

## 关键公式
- Metropolis 接受概率: $P_{\text{accept}} = \min(1, e^{-\beta \Delta E})$
- 重要性采样期望值: $\langle A \rangle = \frac{\sum_s A(s) e^{-\beta E(s)}}{\sum_s e^{-\beta E(s)}} \approx \frac{1}{N} \sum_{i=1}^N A(s_i)$

## 先修知识
- [热力学与统计物理](../theories/thermodynamics-statmech.md)
- [概率论基础](../theories/math-methods.md)

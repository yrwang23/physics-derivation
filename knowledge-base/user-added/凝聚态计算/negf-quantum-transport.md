# 开放量子系统输运与NEGF (Quantum Transport & NEGF)

## 简介
对于有电流流过的开放量子系统（如电极-分子-电极构型），传统周期性边界条件不再适用。NEGF-DFT 将系统划分为半无界的左/右电极和中心散射区，通过电极自能 $\Sigma$ 将无限大环境自由度折叠到中心区。结合推迟格林函数、Fisher-Lee 关系和 Landauer 公式计算透射系数和电导。

## 关键公式
- 分区哈密顿量:
  $\mathbf{H} = \begin{bmatrix} H_L & V_{LC} & 0 \\ V_{CL} & H_C & V_{CR} \\ 0 & V_{RC} & H_R \end{bmatrix}$
- 中心区推迟格林函数:
  $G_C^r = [E^+ - H_C - \Sigma_L^r - \Sigma_R^r]^{-1}$
- 电极自能: $\Sigma_L = V_{CL} g_L^r V_{LC}$
- Landauer 电导公式:
  $G = \frac{e^2}{\pi \hbar} \text{Tr}\left[ \Gamma_L G_C^r \Gamma_R G_C^a \right]$

## 先修知识
- [格林函数基础理论](../user-added/量子多体/many-body-green-function.md)
- [Lippmann-Schwinger 方程](../user-added/量子多体/lippmann-schwinger.md)

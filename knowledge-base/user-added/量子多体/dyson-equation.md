# Dyson 方程 (Dyson Equation)

## 简介
多体格林函数理论的核心方程。连接了无相互作用的裸格林函数 $G_0$ 和有相互作用的完整格林函数 $G$，通过自能 $\Sigma$ 描述所有相互作用效应的总和。

## 关键公式
- Dyson 方程: $G = G_0 + G_0 \Sigma G$，等价于 $G^{-1} = G_0^{-1} - \Sigma$
- 几何级数展开: $G = G_0 \sum_{n=0}^\infty (\Sigma G_0)^n$
- 物理含义: 自能 $\Sigma$ 是不可约自能图之和，描述了电子与其他电子的散射效应
- 在 DMFT 中的两种用法:
  1. $\mathcal{G}_0^{-1} = G_{\text{loc}}^{-1} + \Sigma$ (从局域格林函数求 Weiss 场)
  2. $\Sigma = \mathcal{G}_0^{-1} - G_{\text{imp}}^{-1}$ (从杂质格林函数求新自能)

## 先修知识
- [Matsubara 格林函数](./matsubara-green-function.md)
- [微扰论](../math-tools/perturbation-theory.md)

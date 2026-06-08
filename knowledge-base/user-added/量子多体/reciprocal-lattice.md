# 倒格子与晶面间距 (Reciprocal Lattice & Interplanar Spacing)

## 简介
倒格子是为了描述晶体中周期性物理量而引入的重要概念。由于晶体原子周期性排列，可将实空间的周期函数进行三维傅里叶展开，展开波矢构成倒空间离散点阵即倒格子。倒格矢与正格子对应晶面垂直，其模长与晶面间距成反比。倒格子是X射线衍射和能带理论的基石。

## 关键公式
- 正格点位置矢量:
  $\vec{x} = l_1\vec{a}_1 + l_2\vec{a}_2 + l_3\vec{a}_3$
- 倒格子基矢:
  $\vec{b}_1 = 2\pi \frac{\vec{a}_2 \times \vec{a}_3}{\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)}$
- 正交关系: $\vec{a}_i \cdot \vec{b}_j = 2\pi \delta_{ij}$
- 倒格矢与晶面间距:
  $d = \frac{2\pi}{|\vec{G}_{\min}|}$

## 先修知识
- [傅里叶级数](../math-tools/fourier-analysis.md)

# 能带论基础与布洛赫定理 (Band Theory & Bloch Theorem)

## 简介
能带论建立于绝热近似、单电子近似和周期势场近似之上。布洛赫定理指出：周期势场中电子的波函数为平面波与周期调制函数的乘积（布洛赫波）。这解释了电子在晶格中无阻尼传导的量子力学机制。能量在倒空间具有周期不变性，被限制在离散能带中。

## 关键公式
- 周期势场薛定谔方程:
  $\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r})\right]\psi(\vec{r}) = E\psi(\vec{r})$
- 布洛赫波:
  $\psi_{\vec{k}}^n(\vec{r}) = U_{\vec{k}}^n(\vec{r}) e^{i\vec{k}\cdot\vec{r}}$
- 能量周期性: $E_n(\vec{k}) = E_n(\vec{k} + \vec{K}_n)$
- 时间反演对称性: $E_n(\vec{k}) = E_n(-\vec{k})$

## 先修知识
- [量子力学](../theories/quantum-mechanics.md)
- [倒格子与晶面间距](./reciprocal-lattice.md)

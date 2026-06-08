# 变分法 (Variational Method)

## 简介
研究泛函极值问题的数学工具。在物理学中广泛用于推导运动方程（最小作用量原理）和近似求解量子力学基态。

## 关键公式
- Euler-Lagrange 方程: $\frac{\partial L}{\partial y} - \frac{d}{dx}\frac{\partial L}{\partial y'} = 0$
- 泛函导数: $\frac{\delta F[y]}{\delta y(x)} = \lim_{\epsilon \to 0} \frac{F[y + \epsilon \delta_x] - F[y]}{\epsilon}$
- 量子力学变分原理: $E_0 \leq \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle}$

## 先修知识
- [经典力学](../theories/classical-mechanics.md)

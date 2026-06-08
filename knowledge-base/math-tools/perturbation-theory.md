# 微扰论 (Perturbation Theory)

## 简介
在精确可解系统的基础上，将微小的修正作为展开项逐级近似求解。分为定态微扰和含时微扰。

## 关键公式
- 定态非简并微扰 (一阶能量修正): $E_n^{(1)} = \langle n^{(0)} | \hat{H}' | n^{(0)} \rangle$
- 定态非简并微扰 (一阶波函数修正): $|n^{(1)}\rangle = \sum_{m \neq n} \frac{\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle$
- 含时微扰 (Fermi 黄金规则): $\Gamma = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f)$

## 先修知识
- [量子力学](../theories/quantum-mechanics.md)
- [线性代数](../math-tools/linear-algebra.md)

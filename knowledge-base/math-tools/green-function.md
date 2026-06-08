# 格林函数方法 (Green's Function Methods)

## 简介
用格林函数求解线性微分方程的方法。在凝聚态物理中广泛用于描述准粒子的传播和相互作用。

## 关键公式
- 微分方程格林函数: $[\partial_t^2 - \nabla^2] G(\mathbf{r}, t; \mathbf{r}', t') = \delta(\mathbf{r} - \mathbf{r}') \delta(t - t')$
- 推迟格林函数: $G^R(\mathbf{k}, \omega) = \frac{1}{\omega - \epsilon_\mathbf{k} + i0^+}$
- Matsubara 格林函数: $\mathcal{G}(\mathbf{k}, i\omega_n) = \frac{1}{i\omega_n - \epsilon_\mathbf{k}}$

## 先修知识
- [量子力学](../theories/quantum-mechanics.md)
- [傅里叶分析](../math-tools/fourier-analysis.md)
- [复变函数](../theories/math-methods.md)

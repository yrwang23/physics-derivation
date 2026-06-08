# DMFT 在无穷维下严格成立 (DMFT Exactness in d → ∞)

## 简介
DMFT 的严格理论基础：在晶格维度 $d \to \infty$ 时，需要对跳跃积分做标度变换 $t \to t^*/\sqrt{2d}$ 以保持动能有限。在此标度下，非局域传播子指数衰减，自能成为纯局域的 $\Sigma_{ij} = \delta_{ij}\Sigma_{\text{loc}}$，DMFT 严格精确。

## 核心论证

### 1. 标度律：让动能不发散
- 配位数 $Z = 2d$
- 动能 $\propto Z t^2$ 必须有限 $\Rightarrow$ $t = t^*/\sqrt{2d}$

### 2. 态密度
- 色散: $\epsilon_{\mathbf{k}} = -2t\sum_{\nu=1}^d \cos(k_\nu)$
- 中心极限定理 $\Rightarrow$ 态密度趋于高斯分布: $\rho(\varepsilon) = \frac{1}{\sqrt{2\pi}\,t^*} e^{-\varepsilon^2/(2t^{*2})}$

### 3. 自能动量无关
- 实空间非对角自能 $\Sigma_{ij}$ ($i \neq j$) 的传播子中至少有一条长度为 $|i-j|$ 的电子线
- 每条跳跃贡献因子 $t \sim 1/\sqrt{2d}$，所以非对角传播子 $\propto (1/\sqrt{2d})^{|i-j|} \to 0$
- 因此 $\Sigma_{ij} = \delta_{ij} \Sigma_{\text{loc}}$，动量空间中 $\Sigma(\mathbf{k}, i\omega_n) = \Sigma(i\omega_n)$

### 4. Cavity 格林函数对角化
- $\mathcal{G}_{ij}^{(0)}(i\omega_n) = \delta_{ij} \mathcal{G}_{ii}^{(0)}(i\omega_n)$
- 杂化函数有限: $\Delta(i\omega_n) = t^2 Z \, \mathcal{G}_{00}^{(0)}(i\omega_n) \sim t^{*2}$

## 关键文献
- Metzner & Vollhardt, Phys. Rev. Lett. 62, 324 (1989)

## 先修知识
- [Cavity 方法](./cavity-method.md)
- [二次量子化](./second-quantization.md)
- [Matsubara 格林函数](./matsubara-green-function.md)

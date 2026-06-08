# Matsubara 格林函数 (Matsubara Green's Functions)

## 简介
有限温度下多体系统的格林函数。通过在虚时间轴上定义，将量子统计力学中的热平均转化为类似零温格林函数的微扰展开形式。虚频率 $i\omega_n$ 取离散的 Matsubara 频率（费米子: $\omega_n = (2n+1)\pi/\beta$，玻色子: $\omega_n = 2n\pi/\beta$）。

## 关键公式
- 定义: $\mathcal{G}_{ij}(\tau) = -\langle T_\tau c_i(\tau) c_j^\dagger(0) \rangle$
- Matsubara 频率展开: $\mathcal{G}_{ij}(\tau) = \frac{1}{\beta} \sum_{n} e^{-i\omega_n \tau} \mathcal{G}_{ij}(i\omega_n)$
- 自由费米子格林函数: $\mathcal{G}_0(\mathbf{k}, i\omega_n) = \frac{1}{i\omega_n - \epsilon_\mathbf{k} + \mu}$
- Dyson 方程: $\mathcal{G}(\mathbf{k}, i\omega_n)^{-1} = \mathcal{G}_0(\mathbf{k}, i\omega_n)^{-1} - \Sigma(\mathbf{k}, i\omega_n)$
- 谱函数与推迟格林函数的关系: $A(\mathbf{k}, \omega) = -\frac{1}{\pi} \text{Im} G^R(\mathbf{k}, \omega)$
- 解析延拓: $i\omega_n \to \omega + i0^+$ 将 Matsubara 格林函数变为推迟格林函数

## 先修知识
- [二次量子化](./second-quantization.md)
- [格林函数方法](../math-tools/green-function.md)
- [热力学与统计物理](../theories/thermodynamics-statmech.md)

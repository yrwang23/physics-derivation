# PAW 方法 (Projector Augmented Wave Method)

## 简介
真实全电子波函数在核区剧烈振荡，用平面波展开需要极高截断能。PAW 引入线性变换 $\mathcal{T}$ 将平滑赝波函数 $|\tilde{\Psi}\rangle$ 映射为全电子波函数 $|\Psi\rangle$。空间分为全局平滑部分和局域缀加球区域。PAW 兼具平面波效率和全电子精度，能准确计算依赖核区密度的物理量（如磁矩、超精细作用）。通过补偿电荷机制消除远距离静电震荡误差。

## 关键公式
- PAW 波函数线性变换:
  $|\Psi\rangle = \mathcal{T}|\tilde{\Psi}\rangle = |\tilde{\Psi}\rangle + \sum_i (|\phi_i\rangle - |\tilde{\phi}_i\rangle)\langle \tilde{p}_i | \tilde{\Psi} \rangle$
- 电荷密度三重分解:
  $n(\vec{r}) = \tilde{n}(\vec{r}) + n^1(\vec{r}) - \tilde{n}^1(\vec{r})$
- 广义 KS 方程:
  $\hat{H}|\tilde{\Psi}_n\rangle = \varepsilon_n \hat{S}|\tilde{\Psi}_n\rangle$

## 先修知识
- [Kohn-Sham 密度泛函理论](./kohn-sham-dft.md)
- [平面波基组与布洛赫定理](./plane-wave-basis.md)

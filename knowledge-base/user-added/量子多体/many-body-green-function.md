# 格林函数基础理论 (Many-Body Green's Functions)

## 简介
格林函数是现代凝聚态物理的核心工具。推迟格林函数描述在时空中某点注入一个粒子后在另一点被探测到的概率振幅。通过 Lehmann 谱表示，格林函数的极点对应系统的单粒子激发能谱。借助运动方程 (EOM) 方法可以从哈密顿量直接推导格林函数。态密度与格林函数虚部成正比。

## 关键公式
- 推迟格林函数定义: $G^R(\vec{r}, t; \vec{r}', t') = -i\theta(t-t') \langle [ \hat{\psi}(\vec{r}, t), \hat{\psi}^\dagger(\vec{r}', t') ]_{\mp} \rangle$
- Zubarev 频域运动方程 (EOM): $\omega^+ \langle\langle \hat{A} ; \hat{B} \rangle\rangle_\omega = \langle [\hat{A}, \hat{B}]_{\mp} \rangle + \langle\langle [\hat{A}, \hat{H}] ; \hat{B} \rangle\rangle_\omega$
- 无相互作用格林函数频域解: $G_{km}^R(\omega^+) = \frac{\delta_{km}}{\omega^+ - \epsilon_k}$
- 态密度与格林函数关系: $A(\omega) = -\frac{1}{\pi} \operatorname{Im} G^R(\omega^+)$

## 先修知识
- [海森堡绘景](./ensemble-theory-and-pictures.md)
- [二次量子化](./second-quantization.md)
- [Matsubara 格林函数](./matsubara-green-function.md)

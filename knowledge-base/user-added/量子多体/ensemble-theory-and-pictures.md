# 系综理论与量子力学绘景

## 简介
统计物理中的微正则、正则以及巨正则系综，配分函数与热力学量的联系（如巨正则势、期望值等）。同时总结了三种量子力学等价图像：薛定谔绘景、海森堡绘景和相互作用绘景。相互作用绘景分离了自由演化与相互作用演化，结合 Dyson 级数展开，是多体微扰理论的基石。

## 关键公式
- 正则系综密度矩阵: $\hat{\rho} = \frac{1}{Z} e^{-\beta \hat{H}}$
- 巨正则热力学关系: $d\Omega = -SdT - Nd\mu - pdV$
- 海森堡绘景算符演化: $\hat{A}_H(t) = e^{i\hat{H}t/\hbar} \hat{A}_S e^{-i\hat{H}t/\hbar}$
- Dyson 时间演化算符: $\hat{U}(t, t_0) = 1 + \sum_{n=1}^\infty \left(\frac{-i}{\hbar}\right)^n \frac{1}{n!} \int_{t_0}^t dt_1 \dots \int_{t_0}^t dt_n \mathcal{T}[\hat{V}_I(t_1)\dots\hat{V}_I(t_n)]$

## 先修知识
- [量子力学基础](../theories/quantum-mechanics.md)
- [热力学与统计物理](../theories/thermodynamics-statmech.md)

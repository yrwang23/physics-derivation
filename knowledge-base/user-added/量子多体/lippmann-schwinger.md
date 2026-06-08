# Lippmann-Schwinger 方程与散射理论

## 简介
处理"自由哈密顿量 + 微扰相互作用"系统时，可以将偏微分薛定谔方程改写为等价的积分方程——Lippmann-Schwinger 方程。它自然地引入了系统无微扰的自由传播子（裸格林函数 $\hat{G}_0$）。物理意义为：总波函数等于自由入射波函数加上被势场多次散射后的修正项。为格林函数的无穷级数展开（Dyson 方程）奠定了基础。

## 关键公式
- 算符形式 LS 方程: $|\psi_E\rangle = |\psi_E^0\rangle + \hat{G}_0 \hat{V} |\psi_E\rangle$
- 全格林函数级数展开: $\hat{G} = \hat{G}_0 + \hat{G}_0 \hat{V} \hat{G} = \hat{G}_0 + \hat{G}_0 \hat{V} \hat{G}_0 + \hat{G}_0 \hat{V} \hat{G}_0 \hat{V} \hat{G}_0 + \dots$
- 坐标空间投影: $\psi_E(\vec{r}) = \psi_E^0(\vec{r}) + \int d\vec{r}' G_0(\vec{r}, \vec{r}', E) V(\vec{r}') \psi_E(\vec{r}')$

## 先修知识
- [薛定谔方程]
- [格林函数基础理论](./many-body-green-function.md)

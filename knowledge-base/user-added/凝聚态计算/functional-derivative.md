# 泛函与泛函导数 (Functional & Functional Derivative)

## 简介
泛函是定义域为函数空间、值域为实数或复数的映射，即"函数的函数"。在 DFT 中，系统总能量表示为电子密度 $n(\mathbf{r})$ 的泛函。泛函导数描述自变量函数做无穷小变分时泛函的变化率，是推导 Kohn-Sham 有效势和用变分原理最小化能量泛函的必要数学基础。

## 关键公式
- 泛函微积分基本定义:
  $\delta A = \int dx \frac{\delta A}{\delta n(x)} \delta n(x)$
- von Weizsacker 动能泛函导数:
  $\frac{\delta T_s^{vW}[n]}{\delta n} = -\frac{n''}{4n} + \frac{n'^2}{8n^2}$
- Hartree 势的泛函导数:
  $\frac{\delta U[n]}{\delta n(\vec{r})} = \int d^3r' \frac{n(\vec{r}')}{|\vec{r} - \vec{r}'|} = \mathcal{V}_H[n](\vec{r})$

## 先修知识
- [变分法](../math-tools/variational-method.md)

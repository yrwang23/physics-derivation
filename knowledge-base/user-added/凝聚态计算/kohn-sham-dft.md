# Kohn-Sham 密度泛函理论 (Kohn-Sham Density Functional Theory)

## 简介
KS 方法引入一个虚拟的无相互作用参考电子系统，假设其基态电子密度与真实系统完全相同。将真实系统动能拆分为无相互作用动能与残余项，将所有难以求解的多体效应归入交换关联泛函 $E_{xc}[\rho]$。通过自洽场（SCF）迭代求解单电子有效势方程，大幅降低第一性原理计算的计算量。

## 关键公式
- 总能量泛函:
  $E[\rho] = T_s[\rho] + \int \rho(\vec{r})V_{ext}(\vec{r})d\vec{r} + \frac{1}{2}\iint \frac{\rho(\vec{r})\rho(\vec{r}')}{|\vec{r}-\vec{r}'|}d\vec{r}d\vec{r}' + E_{xc}[\rho]$
- KS 有效势:
  $V_{eff}(\vec{r}) = V_{ext}(\vec{r}) + \int \frac{\rho(\vec{r}')}{|\vec{r}-\vec{r}'|} d\vec{r}' + V_{xc}(\vec{r})$
- 交换关联势: $V_{xc}(\vec{r}) = \frac{\delta E_{xc}[\rho]}{\delta \rho(\vec{r})}$
- KS 单电子方程:
  $\left( -\frac{1}{2}\nabla^2 + V_{eff}(\vec{r}) \right) \phi_i = \varepsilon_i \phi_i$

## 先修知识
- [泛函与泛函导数](./functional-derivative.md)
- [Hartree-Fock 方法](./hartree-fock-method.md)

# 近自由电子近似 (Nearly Free Electron Approximation)

## 简介
近自由电子近似将周期势视为微扰。通过平面波展开布洛赫函数，将薛定谔方程转化为傅里叶势场系数耦合的方程组。远离布里渊区边界时电子行为如自由波；在边界处简并能级分裂形成能隙，该条件等价于布拉格衍射条件。

## 关键公式
- 势场展开:
  $V(\vec{r}) = \sum_{\vec{K}_n} V(\vec{K}_n) e^{i\vec{K}_n\cdot\vec{r}}$
- 零级近似:
  $E(\vec{k}) \approx \frac{\hbar^2 k^2}{2m} + \sum_{\vec{K}\ne0} \frac{|V(\vec{K})|^2}{\frac{\hbar^2}{2m}[k^2 - |\vec{k}+\vec{K}|^2]}$
- 带隙条件: $|\vec{k}|^2 = |\vec{k} + \vec{K}_n|^2$
- 带隙大小:
  $E_{\pm} \approx \frac{\hbar^2 k^2}{2m} \pm |V(\vec{K}_n)|$

## 先修知识
- [能带论基础与布洛赫定理](./bloch-theorem.md)
- [微扰论](../math-tools/perturbation-theory.md)
- [倒格子与晶面间距](./reciprocal-lattice.md)

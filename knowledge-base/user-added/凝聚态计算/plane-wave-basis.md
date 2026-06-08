# 平面波基组与布洛赫定理 (Plane Wave Basis & Bloch Theorem)

## 简介
处理周期晶体时，根据 Bloch 定理将波函数写为相位因子与周期调制函数的乘积。将周期调制函数用倒空间的平面波基组展开，引入截断能 $E_{cut}$ 限制基组规模，是 VASP、QE 等第一性原理软件的核心技术。

## 关键公式
- Bloch 波函数: $\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r})$
- 平面波展开:
  $\psi_{\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} C_{i,\mathbf{k}+\mathbf{G}} e^{i(\mathbf{k}+\mathbf{G})\cdot\mathbf{r}}$
- 截断能:
  $\frac{\hbar^2 |\mathbf{k} + \mathbf{G}|^2}{2m} \le E_{cut}$

## 先修知识
- [能带论基础与布洛赫定理](../user-added/量子多体/bloch-theorem.md)
- [傅里叶分析](../math-tools/fourier-analysis.md)

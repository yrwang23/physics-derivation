# Hartree-Fock 方法 (Hartree-Fock Method)

## 简介
HF 方法是处理多电子相互作用系统的基石级近似理论。它将多体波函数假设为单电子自旋轨道的 Slater 行列式以满足反对称性，代入变分原理得到单电子 Fock 方程。方程包含库仑排斥项（Hartree 项）和交换相互作用项（Exchange 项），但完全忽略了电子关联能。通常在基组下展开轨道，转化为 Roothaan-Hall 方程求解。

## 关键公式
- Slater 行列式:
  $\Psi = \frac{1}{\sqrt{N!}} \hat{A} [\phi_1(1)\phi_2(2)\dots\phi_N(N)]$
- HF 总能量:
  $E = \sum_i \langle i | h(i) | i \rangle + \frac{1}{2}\sum_{ij} (J_{ij} - K_{ij})$
- 库仑算符:
  $\hat{J}_j(1)\phi_i(1) = \left( \int d\mathbf{r}_2 \phi_j^*(\mathbf{r}_2) \frac{1}{r_{12}} \phi_j(\mathbf{r}_2) \right) \phi_i(\mathbf{r}_1)$
- 交换算符:
  $\hat{K}_j(1)\phi_i(1) = \left( \int d\mathbf{r}_2 \phi_j^*(\mathbf{r}_2) \frac{1}{r_{12}} \phi_i(\mathbf{r}_2) \right) \phi_j(\mathbf{r}_1)$
- Roothaan-Hall 方程: $\mathbf{F} \mathbf{C} = \mathbf{S} \mathbf{C} \boldsymbol{\varepsilon}$

## 先修知识
- [量子力学](../theories/quantum-mechanics.md)
- [平均场与 HF 近似](../user-added/量子多体/mean-field-hartree-fock.md)

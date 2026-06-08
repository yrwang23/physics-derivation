# 量子多体路径积分

## 简介
路径积分提供了一种跳出传统算符代数框架理解量子体系演化与统计配分函数的新视角。通过将有限温度系统映射为无穷多微小时间切片上插入完备基的乘积（Trotter-Suzuki 近似），可以把抽象的算符对易转化为普通数值或复数场（费米子对应格拉斯曼数）的泛函积分。它是量子场论解析和数值计算（如 QMC 算法）的底层理论基石。

## 关键公式
- 复时间演化的热力学配分函数: $Z = \operatorname{Tr}[ e^{-\beta \hat{H}} ] = \operatorname{Tr}[ e^{-i\Delta t \hat{H}} ]^N, \quad \Delta t = -i\hbar\beta/N$
- Trotter 分解近似: $\exp\left[-i\Delta t \left(\frac{\hat{p}^2}{2m} + V(\hat{q})\right)\right] \approx \exp\left[-i\Delta t \frac{\hat{p}^2}{2m}\right] \exp\left[-i\Delta t V(\hat{q})\right]$
- 相空间路径积分形式: $Z = \int \mathcal{D}q \mathcal{D}p \exp(iS)$, $S = \int_0^t dt' (p\dot{q} - \mathcal{H}(p,q))$

## 先修知识
- [时间演化算符]
- [系综理论与量子力学绘景](./ensemble-theory-and-pictures.md)
- [变分法](../math-tools/variational-method.md)

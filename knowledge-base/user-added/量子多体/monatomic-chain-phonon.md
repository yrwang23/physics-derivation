# 一维单原子链晶格振动 (Monatomic Chain Lattice Vibration)

## 简介
简谐近似下，原子视为耦合振子系统。一维单原子链考虑最近邻弹性恢复力，通过牛顿运动方程和平面波解（格波）推导出色散关系。波矢独立范围在第一布里渊区，晶体具有低通滤波特性。

## 关键公式
- 运动方程:
  $m\ddot{\mu}_n = \beta(\mu_{n+1} + \mu_{n-1} - 2\mu_n)$
- 色散关系:
  $\omega = \sqrt{4\beta/m}\,|\sin(ka/2)|$
- 长波极限波速: $c = a\sqrt{\beta/m}$
- 布里渊区: $-\pi/a \le k \le \pi/a$
- 声子能量: $\varepsilon_{n_k} = (n_k + \frac{1}{2})\hbar\omega_k$

## 先修知识
- [经典力学](../theories/classical-mechanics.md)
- [固体物理基础](../theories/solid-state-physics.md)

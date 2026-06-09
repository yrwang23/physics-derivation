---
name: "T[γ] 的精确形式"
type: theory
category: "量子多体"
topics: ["LDFT", "单粒子能量泛函", "SIAM", "T[γ]"]
---

# T[γ] 的单粒子能量泛函

## 简介
在 LDFT 中，单粒子能量泛函（也称动能泛函）\(T[\gamma]\) 是精确已知的。它直接由哈密顿量的单粒子部分对密度矩阵 \(\gamma\) 取期望值得到，不涉及任何近似。

## 一般形式
\[
T[\gamma] = \sum_{\alpha\beta\sigma} t_{\alpha\beta} \gamma_{\alpha\beta\sigma}
\]

## SIAM 中的显式形式
\[
\boxed{T[\gamma] = \sum_k \varepsilon_k \gamma_{kk} + \varepsilon_f \gamma_{ff} + \sum_k V_{kf}(\gamma_{kf} + \gamma_{fk})}
\]

其中 \(\gamma_{\alpha\beta} = \gamma_{\alpha\beta\uparrow} + \gamma_{\alpha\beta\downarrow}\)。

## 各项的物理含义

| 项 | 矩阵元类型 | 物理含义 |
|---|---|---|
| \(\sum_k \varepsilon_k \gamma_{kk}\) | \(\gamma_{kk}\)（对角） | 导带电子的单粒子能量 |
| \(\varepsilon_f \gamma_{ff}\) | \(\gamma_{ff}\)（对角） | f 轨道的在位能 |
| \(\sum_k V_{kf}(\gamma_{kf} + \gamma_{fk})\) | \(\gamma_{kf}\)（非对角） | f 与导带之间的杂化/电荷涨落能 |

## 与常规 DFT 的对比
- 常规 DFT: 动能未知，需 Kohn-Sham 轨道构造
- LDFT: \(T[\gamma]\) 精确已知，误差仅来自 \(W[\gamma]\) 的近似

## 先修知识
- [二次量子化](./second-quantization.md)
- [杂质模型基础](./impurity-models.md)
- [格点 Hohenberg-Kohn 定理](./lattice-hk-theorem.md)

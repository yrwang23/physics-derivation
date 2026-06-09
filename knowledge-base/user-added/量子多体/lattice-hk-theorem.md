---
name: "格点 Hohenberg-Kohn 定理"
type: theory
category: "量子多体"
topics: ["LDFT", "密度矩阵", "Hohenberg-Kohn定理", "格点模型", "变分原理"]
---

# 格点 Hohenberg-Kohn 定理 (Lattice HK Theorem)

## 简介
格点 Hohenberg-Kohn 定理是 Lattice Density Functional Theory (LDFT) 的奠基性定理。它将传统 DFT 中的 HK 定理从连续空间推广到离散格点系统，证明单粒子密度矩阵 \(\gamma_{\alpha\beta\sigma} = \langle\Psi|\hat{c}^\dagger_{\alpha\sigma}\hat{c}_{\beta\sigma}|\Psi\rangle\) 可以作为多体问题的基本变量——即基态波函数 \(|\Psi\rangle\) 和基态密度矩阵 \(\gamma\) 之间存在一一对应关系。

## 与连续 DFT 的类比

| 连续 DFT | LDFT |
|---------|------|
| 基本变量: 电子密度 \(\rho(\vec r)\) | 基本变量: 密度矩阵 \(\gamma_{\alpha\beta\sigma}\) |
| 外势 \(v_{\text{ext}}(\vec r)\) 定义问题 | 跳跃积分 \(t_{\alpha\beta}\) 定义问题 |
| 外势 \(\times\) 密度算符 | 跳跃矩阵 \(\times\) 密度矩阵算符 |
| HK 定理: \(\rho(\vec r) \leftrightarrow |\Psi\rangle\) | 格点 HK 定理: \(\gamma \leftrightarrow |\Psi\rangle\) |

## 哈密顿量的形式

格点多体哈密顿量的最一般形式:
\[
\hat H = \underbrace{\sum_{\alpha\beta\sigma} t_{\alpha\beta} \hat{c}^\dagger_{\alpha\sigma} \hat{c}_{\beta\sigma}}_{\hat T} + \underbrace{\frac12 \sum_{\substack{\alpha\beta\gamma\delta \\ \sigma\sigma'}} V_{\alpha\beta\gamma\delta} \hat{c}^\dagger_{\alpha\sigma} \hat{c}^\dagger_{\beta\sigma'} \hat{c}_{\delta\sigma'} \hat{c}_{\gamma\sigma}}_{\hat W}
\]

其中 \(t_{\alpha\beta}\) 包含动能和外势的全部单粒子贡献，在 LDFT 中扮演"外势"的角色。

## 定理证明

**定理**: 对非简并基态，映射 \(|\Psi\rangle \to \gamma\)（基态波函数到基态密度矩阵）是单射，因此可逆。

**证明（反证法）**:
1. 假设存在两组不同的跳跃矩阵 \(t_{\alpha\beta}\) 和 \(t'_{\alpha\beta}\)，对应的哈密顿量 \(\hat H = \hat T + \hat W\) 和 \(\hat H' = \hat T' + \hat W\) 具有相同的基态密度矩阵 \(\gamma\) 但不同的基态 \(|\Psi\rangle\) 和 \(|\Psi'\rangle\)（相差超过一个相位因子）
2. 由变分原理:
\[
E_0 < \langle\Psi'|\hat H|\Psi'\rangle = \langle\Psi'|\hat H'|\Psi'\rangle + \langle\Psi'|\hat H - \hat H'|\Psi'\rangle = E'_0 + \sum_{\alpha\beta}(t_{\alpha\beta} - t'_{\alpha\beta})\sum_\sigma \gamma_{\alpha\beta\sigma}
\]
3. 交换带撇和不带撇的量:
\[
E'_0 < E_0 + \sum_{\alpha\beta}(t'_{\alpha\beta} - t_{\alpha\beta})\sum_\sigma \gamma_{\alpha\beta\sigma}
\]
4. 两式相加得到 \(E_0 + E'_0 < E_0 + E'_0\)，矛盾
5. 因此映射是单射，证毕

**关键点**: 非对角元 \(\gamma_{\alpha\beta\sigma}\)（\(\alpha \ne \beta\)）在证明中起了关键作用——它们是证明矛盾的核心。

## 推论

由 HK 定理可得:
- 基态波函数是 \(\gamma\) 的泛函: \(|\Psi\rangle = |\Psi[\gamma]\rangle\)
- 所有基态期望值都是 \(\gamma\) 的泛函
- 基态能量由变分原理确定: \(E_0 = \min_\gamma E[\gamma]\)

## 先修知识
- [二次量子化](./second-quantization.md)
- [杂质模型基础](./impurity-models.md)

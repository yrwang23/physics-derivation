# 杂质模型基础 (Resonant Level & Anderson Impurity)

## 简介
杂质模型是研究多体强关联物理、近藤效应及 DMFT 的起点。先求解共振能级模型，得出由能带杂化导致的"自能"表达式。在此基础上引入 Anderson 杂质模型，不仅考虑杂质能级与背景电子库的耦合，还在杂质位置加入局域库仑排斥 $U$。由于 $U$ 导致运动方程不可直接闭合，需要用平均场理论进行截断求解。

## 关键公式
- 共振能级模型自能: $\Sigma(\omega^+) = \sum_k \frac{|t_k|^2}{\omega^+ - \epsilon_k}$
- 全格林函数 Dyson 形式: $G_L^R(\omega^+) = \frac{1}{\omega^+ - \epsilon_0 - \Sigma(\omega^+)}$
- Anderson 杂质模型哈密顿量: $\hat{H} = \sum_{\sigma} \epsilon_0 \hat{n}_{d\sigma} + U \hat{n}_{d\uparrow}\hat{n}_{d\downarrow} + \sum_{k\sigma}\epsilon_k \hat{c}_{k\sigma}^\dagger \hat{c}_{k\sigma} + \sum_{k\sigma}(t_k \hat{c}_{d\sigma}^\dagger \hat{c}_{k\sigma} + h.c.)$
- 库仑项平均场退耦: $U \langle \hat{n}_{d\sigma} \rangle \langle\langle \hat{c}_{d\sigma} ; \hat{c}_{d\sigma}^\dagger \rangle\rangle_\omega$

## 先修知识
- [格林函数基础理论](./many-body-green-function.md)
- [平均场理论与 Hartree-Fock 近似](./mean-field-hartree-fock.md)
- [Hubbard 模型](./hubbard-model.md)

# 平均场理论与 Hartree-Fock 近似

## 简介
面对复杂的多体相互作用项，精确求解几乎不可能。平均场理论的核心是：系统的涨落通常是微小的，忽略涨落的二阶项（关联项），将多体系统简化为单粒子在其他粒子形成的有效平均场中运动的问题。Hartree-Fock 在此基础将双体相互作用重组为直接相互作用（Hartree 项）和交换相互作用（Fock 项），是计算多电子体系基态能的主要自洽方法。

## 关键公式
- 平均场近似展开: $\hat{n}_i \hat{n}_j \approx \langle \hat{n}_i \rangle \hat{n}_j + \hat{n}_i \langle \hat{n}_j \rangle - \langle \hat{n}_i \rangle \langle \hat{n}_j \rangle$
- HF 能量算符分离: $\hat{H} \approx \sum_k \epsilon_k \hat{n}_k + \hat{H}_{\text{Hartree}} + \hat{H}_{\text{Fock}}$
- Hartree 项: $\sum_{ijkm} V_{ijkm} [ \hat{n}_{ik} \langle \hat{n}_{jm} \rangle + \hat{n}_{jm} \langle \hat{n}_{ik} \rangle - \langle \hat{n}_{ik} \rangle \langle \hat{n}_{jm} \rangle ]$
- Fock 项: $\pm \sum_{ijkm} V_{ijkm} [ \hat{n}_{im} \langle \hat{n}_{jk} \rangle + \hat{n}_{jk} \langle \hat{n}_{im} \rangle - \langle \hat{n}_{im} \rangle \langle \hat{n}_{jk} \rangle ]$（减号对应费米子，加号对应玻色子）

## 先修知识
- [二次量子化](./second-quantization.md)

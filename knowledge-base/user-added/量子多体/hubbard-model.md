# Hubbard 模型 (Hubbard Model)

## 简介
描述强关联电子系统的最简模型。包含动能（跳跃项）和局域库仑相互作用两项竞争机制，是理解莫特绝缘体、磁性、高温超导等强关联现象的基础模型。

## 关键公式
- 哈密顿量: $H = -t \sum_{\langle ij\rangle, \sigma} (c_{i\sigma}^\dagger c_{j\sigma} + h.c.) + U \sum_i n_{i\uparrow} n_{i\downarrow} - \mu \sum_{i,\sigma} n_{i\sigma}$
  - $t$: 最近邻跳跃积分（动能）
  - $U$: 同格点库仑排斥
  - $\mu$: 化学势
- 半填充 ($\langle n \rangle = 1$) 时，$U > 0$ 导致莫特金属-绝缘体转变
- 极限 $U/t \to 0$: 自由电子能带; $U/t \to \infty$: Heisenberg 自旋模型

## 先修知识
- [二次量子化](./second-quantization.md)
- [固体物理基础](../theories/solid-state-physics.md)

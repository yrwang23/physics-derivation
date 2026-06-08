# 三维晶格振动与玻恩-卡曼边界条件 (3D Lattice Vibration & Born-von Karman BC)

## 简介
玻恩-卡曼周期性边界条件消除表面效应，使波矢 $k$ 离散取值。每个 $k$ 点在倒空间占据均匀体积，第一布里渊区状态总数等于原胞总数 $N$。含 $n$ 个原子的原胞在三维空间共有 $3nN$ 个振动模式。

## 关键公式
- 周期性条件: $e^{-i N_i \vec{k} \cdot \vec{a}_i} = 1$
- 离散波矢:
  $\vec{k} = \frac{n_1}{N_1}\vec{b}_1 + \frac{n_2}{N_2}\vec{b}_2 + \frac{n_3}{N_3}\vec{b}_3$
- 模式数量: $3nN$ 个振动模式（3 个声学支 + $3n-3$ 个光学支）

## 先修知识
- [倒格子与晶面间距](./reciprocal-lattice.md)
- [一维单原子链晶格振动](./monatomic-chain-phonon.md)

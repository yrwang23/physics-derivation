# 二次量子化 (Second Quantization)

## 简介
二次量子化是处理量子多体问题的标准数学语言。它在占据数表象下通过产生和湮灭算符描述多粒子体系，自然地内生了全同粒子的交换对称性（费米子的反对称性和玻色子的对称性）。可以将单体和双体物理量写成场算符的形式。核心思想是关注粒子在能级上的有序排布以及算符的作用顺序。

## 关键公式
- 费米子反对易关系: $\{ \hat{c}_i, \hat{c}_j^\dagger \} = \delta_{ij}, \quad \{ \hat{c}_i, \hat{c}_j \} = 0$
- 玻色子对易关系: $[ \hat{b}_i, \hat{b}_j^\dagger ] = \delta_{ij}, \quad [ \hat{b}_i, \hat{b}_j ] = 0$
- 单体算符二次量子化形式: $\hat{O} = \sum_{ij} \langle i | \hat{o} | j \rangle \hat{a}_i^\dagger \hat{a}_j$
- 双体算符二次量子化形式: $\hat{V} = \sum_{ijkm} \langle ij | \hat{V} | km \rangle \hat{a}_i^\dagger \hat{a}_j^\dagger \hat{a}_m \hat{a}_k$

## 先修知识
- [全同粒子]
- [算符代数]

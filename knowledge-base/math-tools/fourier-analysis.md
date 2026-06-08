# 傅里叶分析与小波 (Fourier Analysis & Wavelets)

## 简介
将函数分解为频率分量。物理学中最常用的变换工具之一，用于信号处理、解微分方程、量子力学中的动量空间表示等。

## 关键公式
- Fourier 变换: $\tilde{f}(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$
- 逆变换: $f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \tilde{f}(\omega) e^{i\omega t} d\omega$
- 卷积定理: $\mathcal{F}[f * g] = \mathcal{F}[f] \cdot \mathcal{F}[g]$

## 先修知识
- 微积分
- [线性代数](../math-tools/linear-algebra.md)

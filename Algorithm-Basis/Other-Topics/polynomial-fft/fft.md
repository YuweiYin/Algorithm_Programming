# Algorithm - Linear Programming - Fast Fourier Transform

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

- 多项式与快速傅立叶变换 Polynomial & FFT
    - 离散傅立叶变换 (Discrete Fourier Transform, DFT)
    - 快速傅立叶变换 (Fast Fourier Transform, FFT)

## DFT & FFT

如果使用单位复数根，可以在 $ \Theta(n log n) $ 时间内完成求值与插值运算。本节给出单位复数根的定义，并研究其性质，以及定义 DFT，然后说明如何仅用 $ \Theta(n log n) $ 时间就可以计算出 DFT 和它的逆。

### 单位复数根

![dft-fft-1](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-1.png)

![dft-fft-2](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-2.png)

### 离散傅立叶变换 DFT

![dft-fft-3](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-3.png)

### 快速傅立叶变换 FFT

FFT 加速的核心思想就是利用**分治策略**，同时也利用了类似**快速幂**的技术。

![dft-fft-4](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-4.png)

如下伪代码完成的任务是：递归求解次数界为 n 的多项式在 n 次单位复数根处的值。注意：这里的长度 n 实际上是 2n，因为在求值前 加倍给定多项式的次数界。因此实际处理的是 2n 次单位根。

```
RECURSIVE_FFT(a)
1  n = a.length  // n is a power of 2
2  if n == 1
3      return a
4  w_n = e^{2 i \pi / n}
5  w = 1
6  a^{0} = (a_0, a_2, ..., a_{n-2})
7  a^{1} = (a_1, a_3, ..., a_{n-1})
8  y^{0} = RECURSIVE_FFT(a^{0})
9  y^{1} = RECURSIVE_FFT(a^{1})
10 for k = 0 to (n/2)-1
11     y_k = y_k^{0} + w * y_k^{1}
12     y_{k + (n/2)} = y_k^{0} - w * y_k^{1}
13     w = w * w_n
14 return y  // y is assumed to be a column vector
```

算法过程描述如下：

1. 在 1 行，获取当前递归的子问题规模 n。
2. 在 2～3 行，处理基本情况，一个元素的 DFT 就是该元素自身，因为此时 `y_0 = a_0 * w_1^{0} = a_0 * 1 = a_0`。
3. 在 4～5 行，设置主 n 次单位复数根 `w_n`，以及初始 w 值为 1。
4. 在 6～7 行，定义以偶数下标元素组成的多项式的系数向量 `a^{0}`，下标为奇数时是 `a^{1}`。
5. 在 8～9 行，递归计算子问题 $ DFT_{n/2} $，对于 k = 0, 1, ..., (n/2) - 1，有：
        - $ y_k^{0} = A^{0} (w_{n/2}^{k}) $
        - $ y_k^{1} = A^{1} (w_{n/2}^{k}) $
    - 或者根据消去引理（$ w_{n/2}^{k} = w_{n/2}^{2k} $）有：
        - $ y_k^{0} = A^{0} (w_{n}^{2k}) $
        - $ y_k^{1} = A^{1} (w_{n}^{2k}) $
6. 在 10～13 行的循环中，综合了递归 $ DFT_{n/2} $ 的计算结果：
    - 第 11 行推出了 $ y_k^{0} = A(w_{n}^{k}) $
    - 第 12 行推出了 $ y_{k + (n/2)} = A(w_{n}^{k + (n/2)}) $
    - 第 4、5 和 13 行保证 w 可以正确更新
7. 在 14 行，最后，返回计算结果 y，即输入的多项式系数向量 a 的 DFT 向量。

![dft-fft-5](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-5.png)

### 在单位复数根处插值

插值是把一个多项式从(DFT)点值表达形式转换回系数表达形式。插值思路：把 DFT 写成一个矩阵方程，然后再观察其逆矩阵的形式。

![dft-fft-6](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-6.png)

![dft-fft-7](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-7.png)

## 高效的 FFT 实现

从渐近时间复杂度的角度来说，可以说 FFT 已经达到了极限。但是 DFT & FFT 的实际应用（如信号处理）中需要尽可能快的速度，因此考虑减小隐藏在渐近符号中的常数因子、提升实际运行速度。

### FFT 的一种迭代实现

在 `RECURSIVE_FFT` 中，第 10～13 行的 for 循环中包含了 2 次重复的 `w_n^k * y_k^{1}` 计算（在编译术语中，该值被称为**公用子表达式** (common subexpression)），而此计算并不像简单的加法那么迅速，因此考虑仅计算此表达式一次，并将其值存放在临时变量中。

```
10 for k = 0 to (n/2)-1
11     temp = w * y_k^{1}
12     y_k = y_k^{0} + temp
13     y_{k + (n/2)} = y_k^{0} - temp
14     w = w * w_n
```

![dft-fft-8](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-8.png)

![dft-fft-9](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-9.png)

```
1  for s = 1 to log_2 (n)
2      for k = 0 to n-1 by 2^s
3          combine the two 2^{s-1} element DFTs in
               A[k..k+2^{s-1}-1] and A[k+2^{s-1}..k+2^{s}-1]
               into one 2^{s} element DFT in A[k..k+2^{s}-1]
```

![dft-fft-10](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-10.png)

```
ITERATIVE_FFT(a)
1  BIT_REVERSE_COPY(a, A)
2  n = a.length  // n is a power of 2
3  for s = 1 to log_2 (n)
4      m = 2^{s}
5      w_m = e^{2 i \pi / n}
6      for k = 0 to n-1 by m
7          w = 1
8          for j = 0 to (m/2)-1
9              temp = w * A[k + j + (m/2)]
10             u = A[k + j]
11             A[k + j] = u + t
12             A[k + j + (m/2)] = u - t
13             w = w * w_n
14 return A
```

![dft-fft-11](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-11.png)

```
BIT_REVERSE_COPY(a, A)
1  n = a.length
2  for k = 0 to n-1
3      A[rev(k)] = a_k
```

![dft-fft-12](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-12.png)

## 并行 FFT 电路

![dft-fft-13](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-13.png)

![dft-fft-14](/img/info-technology/algorithm/other-topics/polynomial-fft/dft-fft-14.png)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/polynomial-fft/fast-fourier-transform.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 30

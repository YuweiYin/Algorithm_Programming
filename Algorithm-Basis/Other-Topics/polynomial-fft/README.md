# Algorithm - Polynomial & FFT

Algorithm - [YuweiYin](https://github.com/YuweiYin)

## 目录

- [多项式与快速傅立叶变换](./fft) Polynomial & FFT
    - 离散傅立叶变换 (Discrete Fourier Transform, DFT)
    - 快速傅立叶变换 (Fast Fourier Transform, FFT)

## 多项式与快速傅立叶变换

两个 n 次多项式相加的最直接方法所需的时间为 $ \Theta(n) $，但相乘的最直接方法所需的时间为 $ \Theta(n^2) $。而**快速傅立叶变换** (Fast Fourier Transform, FFT) 可以将多项式相乘的时间复杂度降低为 $ \Theta(n log n) $。

傅立叶变换的最常见用途是信号处理，这也是 FFT 的最常见用途。信号通常在**时间域**中给出：一个把时间映射到振幅的函数。傅里叶分析允许将时间域上的信号表示成**不同频率的相移正弦曲线的加权叠加**。和频率相关的权重和相位在**频率域**中刻画出信号的特征。

FFT 有很多日程应用，如压缩技术，可用于编码数字视频和音频信息，包括 MP3 文件等。

## 多项式

一个以 x 为变量的**多项式**定义在一个代数域 F (Field) 上，将函数 A(x) 表示为形式和：$ A(x) = \sum_{j=0}^{n-1} a_{j} x^{j} $

称 $ a_{0}, a_{1}, ..., a_{n-1} $ 为如上多项式的**系数**，所有系数都属于域 F，典型的情形是复数集合 C (Complex)。

如果一个多项式 A(x) 的**最高次的非零系数**是 $ a_{k} $，则称 A(x) 的**次数**是 k，记为 degree(A) = k。任何严格大于一个多项式次数的整数都是该多项式的**次数界**，因此对于次数界为 n 的多项式，其次数可以是 0～n-1 之间的任何整数（包括 0 和 n-1）。

在多项式上可以定义很多不同的运算。对于**多项式加法**，如果 A(x) 和 B(x) 都是次数界为 n 的多项式，那么他们的**和**也是一个次数界为 n 的多项式，记为 C(x)。对所有属于定义域的 x（这里的定义域是 A 和 B 的定义域的交集），都有 C(x) = A(x) + B(x)。

对于**多项式乘法**，如果 A(x) 和 B(x) 都是次数界为 n 的多项式，则它们的**乘积** C(x) 是一个次数界为 2n-1 的多项式，对所有属于定义域的 x（这里的定义域是 A 和 B 的定义域的交集），都有 C(x) = A(x)·B(x)。

多项式乘法最简单直接的做法，就是类似于数字乘法、逐位相乘的**竖式乘法**，如下例子：

![fft-1](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-1.png)

![fft-2](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-2.png)

## 多项式的表示

在没有特殊说明的情况下，本章节使用符号(字母) i 来表达虚数单位 $ \sqrt{-1} $。

从某种意义上，多项式的**系数表达**与**点值表达**是等价的，即用点值形式表示的多项式都对应唯一系数形式的多项式。而两种表达方式结合起来、互相转换，就能够使得两个次数界为 n 的多项式乘法运算在 $ \Theta(n log n) $ 时间内完成。

### 系数表达

![fft-3](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-3.png)

### 点值表达

![fft-4](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-4.png)

![fft-5](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-5.png)

![fft-6](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-6.png)

![fft-7](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-7.png)

![fft-8](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-8.png)

### 系数形式表示的多项式快速乘法

为了利用基于点值形式表达的多项式的线性时间乘法算法，来加速基于系数形式表达的多项式乘法，关键在于：能否快速地把一个多项式从系数形式转换为点值形式（**求值**），以及从点值形式转换为系数形式（**插值**）。

可以采用任何点作为求值点，但通过**精心地挑选求值点**，可以把两种表示之间转换所需的时间复杂度降到 $ \Theta(n log n) $。所谓的“精心挑选”，即选择“**单位复数根**”作为求值点。通过对系数向量进行**离散傅立叶变换** (Discrete Fourier Transform, DFT)，得到相应的点值表达。然后对点值对执行**逆 DFT**变换，从而获得相应的系数向量，这样就实现了求值运算的逆运算——插值。快速傅立叶算法 FFT 就是使用上述策略，在 $ \Theta(n log n) $ 完成 DFT 和逆 DFT 运算，从而快速实现多项式乘法。

![fft-9](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-9.png)

![fft-10](/img/info-technology/algorithm/other-topics/polynomial-fft/fft-10.png)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 30

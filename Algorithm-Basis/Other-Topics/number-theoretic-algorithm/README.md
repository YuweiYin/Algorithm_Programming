# Algorithm - Number-Theoretic Algorithm

Algorithm - [YuweiYin](https://github.com/YuweiYin)

## 目录

- 数论算法 Number-Theoretic Algorithm
	- 欧几里得算法 Euclidean Algorithm
	- 扩展的欧几里得算法 Extended Euclidean Algorithm
	- 求解模线性方程 Modular Linear Equation Solving
	- 中国剩余定理 Chinese Remainder Theorem
	- 元素的模取幂 Modular Exponentiation
	- (伪)素数测试 Fermat Pseudo Prime Test
	- Miller-Rabin 随机性素数测试方法
	- 整数的(素)因子分解 - Pollard-Rho 启发式算法

## 数论算法

数论曾经被视为一种优美但没什么实际用途的纯数学学科。如今，数论算法已经得到了广泛的使用。这很大程度上要归功于人们发明了**基于大素数的加密方法**。快速计算大素数的算法使得高效加密成为可能，而目前其安全性的保证则依赖于缺少高效地**将大合数分解为大素数之积**（或求解相关问题，如计算**离散对数**）方法的现状。

**量子计算**与量子通信是目前的前沿研究。在量子计算机中，有一种 Shor's Algorithm **秀尔算法**用于因子分解，可以很快地计算因子分解问题（而这个问题在目前流行的计算模型中 需要耗费指数渐近时间）。

在数论算法中，处理的对象是大整数。而且一般不像排序算法那样，是对大量整数的处理。因此，数论算法通常利用输入所需的**位数**来度量输入的大小，而不仅仅是输入中整数的数目。给定 k 个整数输入 $ a_{1}, ..., a_{k} $，如果算法可以在关于 $ log_{2} (a_1), ..., log_{2} (a_k) $ 的多项式时间完成（即算法在关于**整数的二进制形式的位数**的多项式时间内完成），则称算法称为**多项式时间算法**。

另外，由于当输入整数很大时，基本运算（乘法、除法、模运算等）也会变得较为耗时，因此数论算法通常使用所需的**位运算**数目作为基准来衡量算法的时间代价。例如，将两个 k (二进制)位整数用常规方法相乘 需要 $ \Theta(k^2) $ 次位运算。同样地，用朴素的方法计算一个 k (二进制)位整数除以另一个较短整数的商或求余数 也需要耗时 $ \Theta(k^2) $。

如今，人们已有了更快的数值计算方法。例如，一个简单的分支算法可以在两个 k (二进制)位整数相乘的问题上达到 $ \Theta(k^{log_{2} 3}) $ 的运行时间。而已知的最快算法则只需要 $ \Theta(k log_{2} {k} log_{2} log_{2} {k}) $。然而，在实际问题中，简单直接的 $ \Theta(k^2) $ 算法往往效果最好。

## 基础数论概念

这里简单回顾基础数论中关于整数集 Z = {..., -2, -1, 0, 1, 2, ...} 和自然数集 N = {0, 1, 2, ...} 的一些概念。

### 整除性与约数

![number-theory-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-1.png)

### 素数与合数

![number-theory-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-2.png)

### 除法定理、余数和等模

![number-theory-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-3.png)

### 公约数与最大公约数

![number-theory-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-4.png)

![number-theory-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-5.png)

![number-theory-6](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-6.png)

### 互质数

![number-theory-7](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-7.png)

![number-theory-8](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-8.png)

### 唯一因子分解定理

![number-theory-9](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-9.png)

### 其它相关性质

![number-theory-10](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-10.png)

### 素数的数量

可以用反证法，证明素数的个数有无穷多个

### 素数的分布

关于素数的分布，数论领域有许多研究，其中很著名的就有黎曼猜想，关于 Riemman Zeta function

## 最大公约数 GCD

**欧几里得算法** Euclidean Algorithm 可以高效地计算两个整数的最大公约数 (Greatest Common Divisor, GCD)。在对其运行时间进行分析的过程中，可以发现它与**斐波那契数列**存在一些联系，由此可知欧几里得算法最坏情况下的输入。

![number-theory-11](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-11.png)

### 欧几里得算法

欧几里得（约公元前 300 年）的《几何原本》描述了下列 gcd 算法，实际上这一算法出现的时间可能还要早些。可以直接利用前述定理 31.9 得到 GCD 递归程序，其输入 a 和 b 都是**任意非负整数**。

```
EUCLID(a, b)
1  if b == 0
2      return a
3  else
4      return EUCLID(b, a mod b)
```

计算过程举例：EUCLID(30, 21) = EUCLID(21, 9) = EUCLID(9, 3) = EUCLID(3, 0) = 3

另外，如果在输入时 a < b，那么首次递归后就会交换二者的位置。

前述 `EUCLID` 过程是尾递归，可以改成如下迭代形式：

```
EUCLID(a, b)
1  while b != 0
2      (a, b) = (b, a mod b)
3  return a
```

### 欧几里得算法的运行时间

![number-theory-12](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-12.png)

斐波那契数列：$ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... $

EUCLID(89, 55) = EUCLID(55, 34) = EUCLID(34, 21) = EUCLID(21, 13) = EUCLID(13, 8) = EUCLID(8, 5) = EUCLID(5, 3) = EUCLID(3, 1) = EUCLID(1, 0) = 1

$ gcd(F_{k+1}, F_{k}) = gcd(F_{k}, F_{k-1}) $

### 欧几里得算法的扩展形式

欧几里得算法不仅能计算最大公约数，利用其计算过程的系数，可以得出**(模)乘法的逆元**。此系数是满足下述条件的整系数 x 和 y：$ d = gcd(a, b) = ax + by $。这里 x 与 y 可能为 0 或负数。

下述伪代码描述的过程 `EXTENDED_EUCLID` 的输入为一对非负整数，并返回一个满足前述条件三元组 (d, x, y)：

```
EXTENDED_EUCLID(a, b)
1  if b == 0
2      return (a, 1, 0)
3  else
4      (d', x', y') = EXTENDED_EUCLID(b, a mod b)
5      (d, x, y) = (d', y' x' - \floor(a / b) * y')
6      return (d, x, y)
```

![number-theory-13](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/number-theory-13.png)

如果 `EXTENDED_EUCLID(a, b)` 返回 (d, x, y)，表示 a 和 b 的最大公约数是 d，即有 gcd(a, b) = d = ax + by

如果返回的 d 为 1，则表示 a 和 b 互素，且由于 1 = ax + by，可以得到如下结果：

- 1 = (ax + by) mod b，故有 1 = (ax) mod b，这意味着在 mod b 的情况下，a 与 x 互为乘法逆元
	- 同理，在 mod y 的情况下，也有 a 与 x 互为乘法逆元
- 1 = (ax + by) mod a，故有 1 = (by) mod a，这意味着在 mod a 的情况下，b 与 y 互为乘法逆元
	- 同理，在 mod x 的情况下，也有 b 与 y 互为乘法逆元
- 不过由于计算前往往不知道 x 和 y 值，所以一般是为了得到在 mod b 的情况下，a 的乘法逆元（以及在 mod a 的情况下，b 的乘法逆元）

因此运用 `EXTENDED_EUCLID` 可以高效地计算出 最大公约数 和 (模)乘法逆元。

## 模运算

模运算模型十分适合用群论结构（代数系统）来进行描述。

### 有限群

![group-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-1.png)

另，交换群又常被称为 Abel Group 阿贝尔群。

### 由模加法与模乘法所定义的群

通过对模 n 运用加法与乘法运算，可以得到两个有限交换群，其中 n 是正整数。这些群基于整数模 n 所形成的等价类。

![group-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-2.png)

![group-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-3.png)

![group-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-4.png)

![group-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-5.png)

![group-6](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-6.png)

### 子群

![group-7](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-7.png)

![group-8](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-8.png)

### 由一个元素生成的子群

![group-9](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-9.png)

![group-10](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-10.png)

![group-11](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/group-11.png)

## 求解模线性方程

![modular-linear-equation-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/modular-linear-equation-1.png)

![modular-linear-equation-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/modular-linear-equation-2.png)

下列算法可输出模方程 ax = b (mod n) 的所有解。输入 a 和 n 为任意正整数，b 为任意整数。

```
MODULAR_LINEAR_EQUATION_SOLVER(a, b, n)
1  (d, x', y') = EXTENDED_EUCLID(a, n)
2  if b mod d == 0  // also means $ b|d $
3      x = x'(b/d) mod n
4      for i = 0 to d-1
5          print (x + i(n/d)) mod n
6  else
7      print "no solutions"
```

![modular-linear-equation-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/modular-linear-equation-3.png)

## 中国剩余定理

中国剩余定理 (Chinese Remainder Theorem)

![chinese-remainder-theorem-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/chinese-remainder-theorem-1.png)

![chinese-remainder-theorem-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/chinese-remainder-theorem-2.png)

![chinese-remainder-theorem-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/chinese-remainder-theorem-3.png)

![chinese-remainder-theorem-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/chinese-remainder-theorem-4.png)

## 元素的模取幂

![element-power-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-1.png)

![element-power-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-2.png)

![element-power-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-3.png)

![element-power-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-4.png)

### 用反复平方法求数的幂

![element-power-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-5.png)

```
MODULAR_EXPONENTIATION(a, b, n)
1  c = 0
2  d = 1
3  let <b_{k}, b_{k-1}, ..., b_{0}> be the binary representation of b
4  for i = k downto 0
5      c = 2 * c
6      d = (d * d) mod n
7      if b_i == 1
8          c = c + 1
9          d = (d * a) mod n
10 return d
```

![element-power-6](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-6.png)

![element-power-7](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/element-power-7.png)

## RSA 公钥加密系统

RSA 公钥加密系统主要基于以下(在目前的计算模型中的)事实：寻求大素数是很容易的，但要把一个大合数分解为两个大素数的乘积却相当困难。

### 公钥加密系统

![rsa-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-1.png)

![rsa-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-2.png)

![rsa-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-3.png)

![rsa-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-4.png)

### RSA 加密系统

![rsa-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-5.png)

![rsa-6](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-6.png)

![rsa-7](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/rsa-7.png)

## 素数的测试

本节考虑**寻找大素数**的问题，首先讨论**素数的密度**，然后讨论一种**不完全可行**的测试素数的方法（利用费马(小)定理），最后介绍一种由 Miller 和 Rabin 发现的**有效的随机素数测试算法**。

### 素数的密度

![prime-test-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-1.png)

![prime-test-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-2.png)

### 伪素数测试过程

![prime-test-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-3.png)

```
PSEUDOPRIME(n)
1  if MODULAR_EXPONENTIATION(2, n-1, n) != 1 (mod n)
2      return COMPOSITE  // definitely
3  else
4      return PRIME      // wo hope!
```

![prime-test-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-4.png)

![prime-test-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-5.png)

### Miller-Rabin 随机性素数测试方法

![prime-test-6](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-6.png)

```
WITNESS(a, n)
1  let t and u be such that t >= 1, u is odd, and n-1 = u * 2^{t}
2  x_0 = MODULAR_EXPONENTIATION(a, u, n)
3  for i = 1 to t
4      x_i = x_{i-1}^2 mod n
5      if x_i == 1 and x_{i-1} != 1 and x_{i-1} != n-1
6          return True
7  if x_t != 1
8      return True
9  return False
```

![prime-test-7](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-7.png)

![prime-test-8](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-8.png)

```
MILLER_RABIN(n, s)
1  for j = 1 to s
2      a = Random(1, n-1)
3      if WITNESS(a, n)
4          return CONPOSITE  // definitely
5  return PRIME  // almost surely
```

![prime-test-9](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-9.png)

### Miller-Rabin 素数测试的出错率

如果 `MILLER_RABIN` 返回 True，则它仍有一种很小的可能性会产生错误。然而，它不像 `PSEUDOPRIME` 那样出错的概率依赖于 n。而且它也不存在坏的输入。相反，它的出错率取决于 s 的大小和在选取基值 a 时的“运气”。另外，由于每次测试都比简单地检查等式 (31.40) 更严格，因此从总体上，对随机选取的整数 n，判断 n 为素数的出错率应该是很小的。下面的两个定理阐述了更精确的论点，其证明过程详见《CLRS》Chapter 31.8。

《CLRS》**定理 31.38**：如果 n 是一个奇合数，则 n 为合数的证据的数目至少为 (n-1)/2。

《CLRS》**定理 31.39**：对于任意奇数 n > 2 和正整数 s，`MILLER_RABIN(n, s)` 出错的概率至多为 2^{-s}。

![prime-test-10](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-10.png)

![prime-test-11](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/prime-test-11.png)

## 整数的因子分解

假设希望将一个整数 n 进行**因子分解**，也就是分解为**素数的乘积**。同过前一节的素数测试，可以以很大概率地推测 n 是否为素数，也能断定 n 是否为合数。但当指出 n 为合数时，素数测试算法并不能指出 n 的素数因子。

对一个大整数 n 进行因子分解，似乎要比仅确定 n 是素数还是合数困难得多。即使用当今的超级计算机和现行的最佳算法，要对任意一个 1024 位的数进行因子分解也还是不实际的。

### Pollard 的 rho 启发式方法

对小于 R 的所有整数进行试除，保证完全获得小于 R^2 的任意数的因子分解。下列过程用相同的工作量，就能对小于 R^4 的任意数进行因子分解（除非运气不佳，否则可以完成）。由于该过程仅仅是一种启发式方法，因此既不能保证其运行时间 也不能保证其运行成功，尽管该过程在实际应用中非常有效。`POLLARD_RHO` 过程的另一个优点是：它只使用固定量的存储空间。（如果愿意，可以很容易地在一个可编程的掌上计算器上实现此过程，以找出较小整数的素因子）

```
POLLARD_RHO(n)
1  i = 1
2  x_1 = Random(0, n-1)
3  y = x_1
4  k = 2
5  while True
6      i = i + 1
7      x_i = (x_{i-1}^2 - 1) mod n
8      d = gcd(y - x_i, n)
9      if d != 1 and d != n
10         print(d)
11     if i == k
12         y = x_i
13         k = 2 * k
```

![pollard-rho-1](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/pollard-rho-1.png)

![pollard-rho-2](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/pollard-rho-2.png)

![pollard-rho-3](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/pollard-rho-3.png)

![pollard-rho-4](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/pollard-rho-4.png)

![pollard-rho-5](/img/info-technology/algorithm/other-topics/number-theoretic-algorithm/pollard-rho-5.png)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/number-theoretic-algorithm/number-theory.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 31

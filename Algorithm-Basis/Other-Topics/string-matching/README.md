# Algorithm - String Matching

Algorithm - [YuweiYin](https://github.com/YuweiYin)

## 目录

- 字符串匹配 String Matching
	- 朴素字符串匹配算法 Naive String Matching
	- Rabin-Karp 字符串匹配算法
	- Finite Automaton 有限自动机-字符串匹配算法
	- Knuth-Morris-Pratt - KMP 字符串匹配算法

## 字符串匹配

在编辑文本程序过程中，经常需要在文本中找到某个**模式** (pattern) 的所有出现位置。典型情况是，一段正在被编辑的文本构成一个文件，而所要寻找的模式是用户正在输入的特定的关键字。有效地解决这个问题的一类算法被称为**字符串匹配算法**，该类算法能够极大地提高编辑文本程序时的响应效率。字符串匹配算法也被应用在其它很多方面，例如在网络搜索引擎中的信息搜索，以及 DNA 序列中搜寻特定的一段序列（与使用动态规划求解 DNA 最长子序列问题有所不同，模式字符串是**下标连续的一段字符串**，而子序列只要求下标为严格增序）。

![string-matching-1](/img/info-technology/algorithm/other-topics/string-matching/string-matching-1.png)

![string-matching-2](/img/info-technology/algorithm/other-topics/string-matching/string-matching-2.png)

### 符号和术语

![string-matching-3](/img/info-technology/algorithm/other-topics/string-matching/string-matching-3.png)

![string-matching-4](/img/info-technology/algorithm/other-topics/string-matching/string-matching-4.png)

## 朴素字符串匹配算法

朴素字符串匹配算法是通过一个循环找到所有的有效偏移。该循环对 n-m+1 个可能的 s 值进行检测，看是否满足条件 P[1..m] == T[s+1..s+m]。

```
NAIVE_STRING_MATCHER(T, P)
1  n = T.length
2  m = P.length
3  for s = 0 to n-m
4      if P[1..m] == T[s+1..s+m]
5          print "Pattern occur with shift" s
```

![string-matching-5](/img/info-technology/algorithm/other-topics/string-matching/string-matching-5.png)

## Rabin-Karp 算法

在实际应用中，Rabin 和 Karp 所提出的字符串匹配算法能够较好地运行，并且还可以从中归纳出相关问题的其它算法，比如二维模式匹配。Rabin-Karp 算法的预处理时间是 $ \Theta(m) $，并且在最坏情况下，它的运行时间为 $ \Theta((n-m+1)m) $。基于一些假设，在平均情况下，它的运行时间还是比较好的。

该算法运用了一些初等数论的概念，比如两个数相对于第三个数模等价。并且此算法与哈希散列有相似之处。

![rabin-karp-1](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-1.png)

![rabin-karp-2](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-2.png)

![rabin-karp-3](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-3.png)

![rabin-karp-4](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-4.png)

```
RABIN_KARP_MATCHER(T, P, d, q)
1  n = T.length
2  m = P.length
3  h = d^{m-1} mod q
4  p = 0
5  t_0 = 0
6  for i = 1 to m    // preprocessing
7      p = (d * p + P[i]) mod q
8      t_0 = (d * t_0 + T[i]) mod q
9  for s = 0 to n-m  // matching
10     if p == t_s
11         if P[1..m] == T[s+1..s+m]
12             print "Pattern occur with shift" s
13     if s < n-m
14         t_{s+1} = (d * (t_s - T[s+1] * h) + T[s+m+1]) mod q
```

![rabin-karp-5](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-5.png)

![rabin-karp-6](/img/info-technology/algorithm/other-topics/string-matching/rabin-karp-6.png)

## 利用有限自动机进行字符串匹配

很多字符串匹配算法都要建立一个有限自动机（比如 AC 自动机、后缀自动机 SAM、回文自动机 PAM 等），它是一个处理信息的简单机器，通过对文本字符串 T 进行扫描，找出模式 P 的所有出现位置。

这些字符串匹配的自动机通常都非常有效：它们只对每个文本字符**检查一次**，并且检查每个文本字符时所用的时间为常数。因此，在模式预处理完成并建立好自动机后 进行匹配所需要的时间为 $ \Theta(m) $。但是如果字母表 $ \Gamma $ 很大，建立自动机所需的时间也可能很多，预处理时间为 $ O(m | \Gamma |) $。而后面介绍的 KMP 算法可以将预处理时间缩短为 $ \Theta(m) $。

下面先定义**有限自动机** (finite automaton)。然后，考察一种特殊的字符串匹配自动机，并展示如何用它找出一个模式在文本中出现的位置，最后，将说明对一个给定的输入模式，如何构造相应的字符串匹配自动机。

### 有限自动机

![finite-automaton-1](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-1.png)

![finite-automaton-2](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-2.png)

![finite-automaton-3](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-3.png)

### 字符串匹配自动机

![finite-automaton-4](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-4.png)

![finite-automaton-5](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-5.png)

![finite-automaton-6](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-6.png)

![finite-automaton-7](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-7.png)

```
FINITE_AUTOMATON_MATCHER(T, delta, m)
1  n = T.length
2  q = 0
3  for i = 1 to n
4      q = delta(q, T[i])
5      if q == m
6          print "Pattern occur with shift" i - m
```

![finite-automaton-8](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-8.png)

![finite-automaton-9](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-9.png)

![finite-automaton-10](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-10.png)

### 计算转移函数

下面的过程根据一个给定模式串 P[1..m] 来计算转移函数 $ \delta $。

```
COMPUTE_TRANSITION_FUNCTION(P, \Gamma)
1  m = P.length
2  for q = 0 to m
3      for each character a \in \Gamma
4          k = min(m + 1, q + 2)
5          repeat
6              k = k - 1
7          until P[1..k] is suffix of (P[1..q] join [a])
8          \delta(q, a) = k
9  return \delta
```

![finite-automaton-11](/img/info-technology/algorithm/other-topics/string-matching/finite-automaton-11.png)

## Knuth-Morris-Pratt 算法

Knuth-Morris-Pratt (KMP) 算法 是 Knuth、Morris 和 Pratt 三人设计的线性时间字符串匹配算法。这个算法无需像前述有限自动机那样计算转移函数 $ \delta $。KMP 算法的匹配时间也是 $ \Theta(n) $，只用到辅助函数 $ \pi $，并且可以在 $ \Theta(m) $ 时间内根据模式串进行预处理，辅助函数的值存储于数组 $ \pi[1..m] $ 中（后面用 p 代替符号 $ \pi $）。数组 p 使得匹配过程中可以按需要“即时”有效地(在摊还意义上)计算转移函数 $ \delta $。

KMP 的核心思想：当前匹配过程中，如果遇到了不匹配的字符，不是更换起点、从模式串首部重新匹配，而是根据之前已经匹配到的信息，回退到某个恰当的位置 继续进行匹配。

### 关于模式的前缀函数

![kmp-1](/img/info-technology/algorithm/other-topics/string-matching/kmp-1.png)

![kmp-2](/img/info-technology/algorithm/other-topics/string-matching/kmp-2.png)

![kmp-3](/img/info-technology/algorithm/other-topics/string-matching/kmp-3.png)

```
KMP_MATCHER(T, P)
1  n = T.length
2  m = P.length
3  p = COMPUTE_PREFIX_FUNCTION(P)
4  q = 0
5  for i = 1 to n
6      while q > 0 and P[q+1] != T[i]
7          q = p[q]
8      if P[q+1] == T[i]
9          q = q + 1
10     if q == m
11         print "Pattern occur with shift" i - m
12     q = p[q]
```

```
COMPUTE_PREFIX_FUNCTION(P)
1  m = P.length
2  let p[1..m] be a new array
3  p[1] = 0
4  k = 0
5  for q = 2 to m
6      while k > 0 and P[k+1] != P[q]
7          k = p[k]
8      if P[k+1] == P[q]
9          k = k + 1
10     p[q] = k
11 return p
```

![kmp-4](/img/info-technology/algorithm/other-topics/string-matching/kmp-4.png)

关于前缀函数计算 `COMPUTE_PREFIX_FUNCTION` 和 KMP 算法 `KMP_MATCHER` 的正确性，可以参考《CLRS》Chapter 32.4。

![kmp-5](/img/info-technology/algorithm/other-topics/string-matching/kmp-5.png)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/string-matching/string-algorithm.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 32

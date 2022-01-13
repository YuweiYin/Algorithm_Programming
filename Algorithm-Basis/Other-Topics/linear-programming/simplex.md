# Algorithm - Linear Programming - Simplex

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

线性规划 Linear Programming

单纯形算法 Simplex Algorithm

## 单纯形算法 Simplex Algorithm

单纯形算法是求解线性规划问题的经典方法。虽然它的运行时间在最坏情况下是指数级的，但它在实际中通常相当快速，此外，单纯形算法对深刻理解线性规划很有帮助。

单纯形算法与求解线性方程组的高斯消元法 (Gaussian Elimination) 有些类似。高斯消元法从一个解未知的线性等式系统开始，在每次迭代中，把这个系统重写为具有一些额外结构的等价形式。经过一定次数的迭代后，等式系统已经被重写到一个容易求解的形式了。单纯形算法以一种类似的方式进行，而且可以被看作是**在不等式上的高斯消元法**。

在单纯形算法的每轮迭代中，都关联一个“基本解”，很容易从线性规划的松弛型中得到此基本解：将每个非基本变量设为 0，并从等式约束中计算基本变量的值。每轮迭代把一个松弛型转换成一个等价的松弛型。

关联的基本可行解的目标值不会小于上一轮的迭代，通常会更大一些。为了增大目标值，选择一个非基本变量，使得如果从 0 开始增加变量值，目标值也会增加。变量值能够增加的幅度受限于其它的约束条件，将之增加 直到某基本变量变为 0。然后重写松弛型，交换此基本变量和选定的非基本变量。

### 单纯形算法的一个例子

![simplex-1](/img/info-technology/algorithm/other-topics/linear-programming/simplex-1.png)

![simplex-2](/img/info-technology/algorithm/other-topics/linear-programming/simplex-2.png)

![simplex-3](/img/info-technology/algorithm/other-topics/linear-programming/simplex-3.png)

![simplex-4](/img/info-technology/algorithm/other-topics/linear-programming/simplex-4.png)

![simplex-5](/img/info-technology/algorithm/other-topics/linear-programming/simplex-5.png)

![simplex-6](/img/info-technology/algorithm/other-topics/linear-programming/simplex-6.png)

### 转动

一个**转动**选取一个**非基本变量** xe（称为**替入变量**）和一个基本变量 xl（称为**替出变量**），然后替换二者的角色。

现在形式化主元的过程。下面的过程 `PIVOT` 以一个松弛型为输入，给定元组 `(N, B, A, b, c, v)`、替出变量 xl 的下标 l，以及替入变量 xe 的下标 e。过程返回描述新松弛型的元祖 `(N', B', A', b', c', v')`。m x n 阶矩阵 A 和 A' 的元素实际上都是松弛型中的系数的相反数。回顾各符号的意义如下：

![lp-6](/img/info-technology/algorithm/other-topics/linear-programming/lp-6.png)

```
PIVOT(N, B, A, b, c, v, l, e)
1  // Compute the coefficients of the equation for new basic variable x_e
2  let A' be a new m x n matrix
3  b'_e = b_l / a_le
4  for each j \in N-{e}
5      a'_ej = a_lj / a_le
6  a'_el = 1 / a_le
7  // Compute the coefficients of the remaining constraints
8  for each i \in B-{l}
9      b'_i = b_i - a_ie * b'_e
10     for each j \in N-{e}
11         a'_ij = a_ij - a_ie * a'_ej
12     a'_il = - a_ie * a'_el
13 // Compute the objective function
14 v' = v + c_e * b'_e
15 for each j \in N-{e}
16     c'_j = c_j - c_e * a'_ej
17 c'_l = - c_e * a'_el
18 // Compute new sets of basic and nonbasic variables
19 N' = (N - {e}) \cup {l}
20 B' = (B - {l}) \cup {e}
21 return (N', B', A', b', c', v')
```

算法过程描述如下：

1. 在 2～6 行，创建新系数矩阵 A'，并通过重写 `x_l` 在左边的等式将 `x_e` 置于等式左边，来计算 `x_e` 的新等式中的系数。
2. 在 8～12 行，通过将每个 `x_e` 替换为这个新等式的右边 来更新剩下的等式。
3. 在 14～17 行，对目标函数进行前述同样地替换。
4. 在 19～20 行，更新非基本变量集合 N 和基本变量集合 B。
5. 在 21 行，最后返回新的松弛型。

如果 `a_le == 0`，则 `PIVOT` 过程会有除 0 错误，因此仅当 `a_le != 0` 时调用此过程。

![simplex-7](/img/info-technology/algorithm/other-topics/linear-programming/simplex-7.png)

### 正式的单纯形算法

在使用单纯形算法解决线性规划问题前，还需思考当前问题的性质：

- 如何确定一个线性规划是不是可行的？
- 如果此线性规划是可行的，但初始基本解不可行，该怎么办？
- 如何确定一个线性规划是否无界？
- 如何选择替入变量和替出变量？

假设有一个过程 `INITIALIZE_SIMPLEX(A, b, c)`，输入为一个基本的线性规划，即一个 m x n 的矩阵 A = (aij)，一个 m 维向量 b = (bi)，一个 n 维向量 c = (cj)。如果这个问题是不可行的，此过程将报告此线性规划不可行，然后终止。否则此过程返回一个初始基本解可行的松弛型。

如前所述，子过程 `SIMPLEX` 以一个标准型的线性规划作为输入，返回一个 n 维向量 x' = (x'\_{j}) 为线性规划的一个最优解。

```
SIMPLEX(A, b, c)
1  (N, B, A, b, c, v) = INITIALIZE_SIMPLEX(A, B, c)
2  let \delta be a new vector of length m
3  while some index j \in N has c_j > 0
4      choose an index e \in N for which c_e > 0
5      for each index i \in B
6          if a_ie > 0
7              \delta_i = b_i / a_ie
8          else
9              \delta_i = inf
10     choose an index l \in B that minimizes \delta_l
11     if \delta_l == inf
12         return "unbounded"
13     else
14         (N, B, A, b, c, v) = PIVOT(N, B, A, b, c, v, l, e)
15 for i = 1 to n
16     if i \in B
17         x'_i = b_i
18     else
19         x'_i = 0
20 return (x'_1, x'2, ..., x'_n)
```

算法过程描述如下：

1. 在 1 行，调用过程 `INITIALIZE_SIMPLEX(A, b, c)`，要么确定这个线性规划是不可行的，要么返回一个初始基本解可行的松弛型。
2. 在 3～14 行的 while 循环是单纯形算法的主体部分，如果目标函数中所有系数 `c_j` 都是负值，那么 while 循环将终止。如果进入 while 循环内部，下面进行描述：
    - 在 4 行，在非基本变量集合 N 中选择一个变量 `x_e` 作为替出变量，其系数 `c_e` 在目标函数中为正值。
    - 在 5～10 行，检查每个约束，然后挑选出一个约束：此约束能够最严格地限制 `x_e` 值增加的幅度，而又不违反任何非负约束。与此约束相关联的基本变量是 `x_l`，它会作为替入变量。
    - 在 11～12 行，如果没有约束能够限制替入变量所增加的幅度，那么算法在 11 行返回“无界”。
    - 在 13～14 行，否则，调用 `PIVOT` 过程来交换替出变量与替入变量的角色。
3. 在 15～19 行，通过把所有的非基本变量设为 0 以及把每个基本变量 `x'_i` 设为 `b_i`，来计算初始线性规划的一个解向量 `(x'_1, x'2, ..., x'_n)`。
4. 在 20 行，最后返回解向量。

### 单纯形算法的正确性

下面给出一些引理、推论、定理来说明单纯形算法的正确性，包含如下方面：首先（引理 29.2）说明如果 `SIMPLEX` 有一个初始可行解 并且 最终会停止，则它要么返回一个可行解，要么确定此线性规划是无解的。然后（引理 29.3～引理 29.7）说明 `SIMPLEX` 过程会停止。最后（定理 29.10）说明返回的解是最优的。（关于这些引理和定理的证明，详见《CLRS》Chapter 29）

《CLRS》**引理 29.2**：给定一个线性规划 (A, b, c)。假设在 `SIMPLEX` 第 1 行中对 `INITIALIZE_SIMPLEX` 的调用返回一个基本解可行的松弛型。如果 `SIMPLEX` 在第 20 行返回一个解，则这个解是此线性规划的一个可行解。如果 `SIMPLEX` 在第 11 行返“无界”，则此线性规划是无界的。

---

单纯形算法的每次迭代会增加和基本解关联的目标值 v。`SIMPLEX` 的迭代也**不会减小**基本解相关联的目标值，但是可惜的是，可能会存在**保持目标值 v 不变**的一些迭代，这个现象被称为**退化**。

退化会阻止单纯形算法终止，因为它可以引起一种被称为**循环** (cycling) 的现象：`SIMPLEX` 的两次不同迭代中的松弛型完全一样。因为退化，`SIMPLEX` 会选择一个转动操作序列，让目标值不变，但是会在此序列中重复一个松弛型，从而永远循环下去、`SIMPLEX` 不会终止。

循环是 `SIMPLEX` 唯一可能不会终止的原因。下面先用引理 29.3 和 引理 29.4 证明一个性质，然后在 引理 29.5 证明这一点。

在每一次循环中，除了集合 N、B 以外，`SIMPLEX` 还维护了 A、b、c 和 v。尽管维护它们能够高效实现单纯形算法，但不维护它们也能得到最终的解向量。也即是说，基本变量和非基本变量的集合足以唯一确定松弛型。下面引理 29.3 和 引理 29.4 将证明这一点。

《CLRS》**引理 29.3**：设 I 是一个下标集合。对于每一个 j \in I，设 aj 和 bj 是实数，并令 xj 是一个实数变量。设 c 是任意的实数。假设对于变量 xj 的任何设置，都有 $ \sum_{j \in I} aj·xj == c + \sum_{j \in I} bj·xj $，那么对任意的 j \in I，有 aj == bj 且 c == 0。

《CLRS》**引理 29.4**：设 (A, b, c) 是一个线性规划的标准形式。给定基本变量的一个集合 B，那么关联的松弛型是唯一确定的。

现在可以说明循环是 `SIMPLEX` 可能不会终止的唯一原因。

《CLRS》**引理 29.5**：如果 `SIMPLEX` 在至多 $ C_{n+m}^{m} $ 次迭代内不终止，那么它是循环的。（这里 C 代表组合数）

循环在理论上是可能出现的，但在实际中非常罕见。可以通过小心地选择替入变量和替出变量来避免循环的发生。一种方法是 **对输入稍微进行扰动**，使得不太可能有两个解具有相等的目标值。另一种方法是通过 **总是选择下标最小的变量** 来打破相等的目标值，这种策略被称为 **Bland 规则**。

《CLRS》**引理 29.6**：如果 `SIMPLEX` 的第 4 行和第 10 行 **总是选择具有最小下标的变量** 来打破目标值不变的局面，那么 `SIMPLEX` **必然终止**。

下面的引理 29.7 进行了总结：

《CLRS》**引理 29.7**：假设 `INITIALIZE_SIMPLEX` 返回一个基本解可行的松弛型，则 `SIMPLEX` 要么报告一个线性规划是无界的，要么在至多 $ C_{n+m}^{m} $ 次迭代内终止，并得到一个可行解。

根据 Stirling 公式易知，组合数是指数级别的，因此在最坏情况下单纯形算法的渐近运行时间会达到指数阶。不过它在实际中运行高效。

## 对偶性

前面已经证明了在某些假设下 `SIMPLEX` 过程会终止，下面说明它计算出的解是线性规划的最优解。为此引入一个有力的概念：**线性规划对偶性**。

对偶性可以用于证明一个解的确是最优的。在最大流问题中的 **最大流最小切割定理** 就是对偶性的一个例子。假设给定最大流问题的一个实例，如何确定一个流 f 具有最大的流值 `|f|` 呢？根据最大流最小切割定理，如果能找到一个切割的值也为 `|f|`，那么就可以确定 f 的确是一个最大流。这样的关系提供了一个对偶性的例子：给定一个**最大化问题**，定义一个**相关的最小化问题**，使得这两个问题具有**同样的最优目标值**。

给定一个最大化目标的线性规划，考虑如何将其形式化为一个**对偶**线性规划，其目标是最小化，而且最优值与初始线性规划的最优值相同。当表示对偶线性规划时，称初始的线性规划为**原始** (primal) 线性规划。

![simplex-8](/img/info-technology/algorithm/other-topics/linear-programming/simplex-8.png)

![simplex-9](/img/info-technology/algorithm/other-topics/linear-programming/simplex-9.png)

![simplex-10](/img/info-technology/algorithm/other-topics/linear-programming/simplex-10.png)

### 弱对偶性

**弱对偶性**表明原始线性规划的任意可行解的值 不大于 对偶线性规划的任意可行解的对应值。

《CLRS》**引理 29.8**（**线性规划弱对偶性**）：设 x 表示式 (29.16)～(29.18) 中原始线性规划的任意一个可行解，y 表示式 (29.83)～(29.85) 中对偶问题的任意一个可行解。那么有 $ \sum_{j=1}^{n} cj·xj = \sum_{i=1}^{m} bi·yi $

《CLRS》**推论 29.9**：令 x 表示一个原始线性规划 (A, b, c) 的一个可行解，令 y 表示相应对偶问题的一个可行解。如果 $ \sum_{j=1}^{n} cj·xj = \sum_{i=1}^{m} bi·yi $，那么 x 和 y 分别是 原始线性规划 和 对偶线性规划 的最优解。

《CLRS》**定理 29.10**（**线性规划对偶性**）：假设 `SIMPLEX` 在原始线性规划 (A, b, c) 上返回值 x = (x1, x2, ..., xn)。令 N 和 B 分别表示最终松弛型的 非基本变量集合 和 基本变量集合，令 c' 表示最终松弛型中的系数，令 y = (y1, y2, ..., ym) 定义为：若 (n+i) \in N 则 yi = - c'\_{n+i}，否则 yi = 0。那么，x 是原始线性规划的一个最优解，y 是对偶线性规划的一个最优解，并且有 $ \sum_{j=1}^{n} cj·xj = \sum_{i=1}^{m} bi·yi $

上述引理、推论和定理的证明详见《CLRS》Chapter 29.4

## 初始基本可行解

### 找到一个初始解

假设有一个过程 `INITIALIZE_SIMPLEX`，它确定一个线性规划是否有任何的可行解，如果有，则给出一个基本解可行的松弛型。

一个线性规划是可行的，而其初始基本解是不可行的，这种情况是可能出现的。

![simplex-11](/img/info-technology/algorithm/other-topics/linear-programming/simplex-11.png)

```
INITIALIZE_SIMPLEX(A, b, c)
1  let k be the index of the minimum b_i
2  if b_k >= 0
3      return ({1, 2, ..., n}, {n+1, n+2, ..., n+m}, A, b, c, 0)
4  form L_{aux} by adding - x_0 to the left-hand side of each constraint
       and setting the objective function to - x_0
5  let (N, B, A, b, c, v) be the resulting slack form for L_{aux}
6  l = n + k
7  // L_{aux} has n+1 nonbasic variables and m basic variables
8  (N, B, A, b, c, v) = PIVOT(N, B, A, b, c, v, l, 0)
9  // The basic solution is now feasible for L_{aux}
10 iterate the while loop of lines 3~14 of SIMPLEX until an optimal solution
       to L_{aux} is found
11 if the optimal solution to L_{aux} sets x'_0 to 0
12     if x'_0 is basic
13         perform one (degenerate) pivot to make it nonbasic
14     from the final slack form of L_{aux}, remove x_0 from the constaints and
           restore the original objective function of L, but replace each basic
           variable in this objective function by the right-hand side of its
           associated constraint
15     return the modified final slack form
16 else
17     return "infeasible"
```

算法过程描述如下：

1. 在 1～3 行，在给定 N 和 B，对于所有 i \in B 有 `x'_i = b_i`，以及对于所有 j \in N 有 `x'_j = 0` 的条件下，隐含地测试 L 的初始松弛型的基本解。
    - 如果第 2 行中发现这个基本解是可行的，即对所有的 i \in N \cup B 有 `x'_j >= 0`，则第 3 行返回这个松弛型。
    - 否则，在第 4 行中，构造辅助线性规划 `L_{aux}`。
    - 因为 L 的初始基本解是不可行的，所以 `L_{aux}` 的松弛型的初始基本解也一定不可行。为了找到一个基本可行解，将执行一个主元 (pivot) 操作。
2. 在 6 行，选择 l = n+k 作为基本变量的下标，该基本变量将是下面一个主元操作的替出变量。
    - 因为基本变量是 `x_{n+1}, x_{n+2}, ..., x_{n+m}`，替出变量 `x_l` 将是负值最大的变量。
3. 在 8 行，执行对 `PIVOT` 的调用，以 `x_0` 为替入变量，`x_l` 为替出变量。由此 `PIVOT` 的调用产生的基本解是可行的。
4. 在 10 行，现在有了一个基本解可行的松弛型，可以在第 10 行重复调用 `PIVOT` 来完全求解出辅助线性规划。
5. 在 11 行，测试是否找到了一个 `x_0` 项为 0 的 `L_{aux}` 的最优解，如果找到了，进入分支：
    - 在 12～14 行，可以生成一个 L 的松弛型，其基本解是可行的。
    - 为了做到这一点，首先在第 12～13 行处理退化情形，其中 `x_0` 可能仍然是基本变量，其值为 `x'_0 = 0`。在此情形下，执行一个转动步骤把 `x_0` 从基本解中移除，采用任何满足 `a_0e != 0` 的 e \in N 作为替入变量。
    - 新的基本解仍然可行；退化转动没有改变任何变量的值。
    - 下面从约束中删除所有 `x_0` 项，并且恢复 L 的原始目标函数。原始目标函数可能包含了基本变量和非基本变量。
6. 在 15 行，返回前述修改后的松弛型。
7. 在 17 行，如果在 11 行发现初始线性规划 L 是不可行的，那么在第 16 行中返回这一信息。

### INITIALIZE_SIMPLEX 的正确性

《CLRS》**引理 29.12**：如果一个线性规划 L 没有可行解，那么 `INITIALIZE_SIMPLEX` 返回“不可行”；否则，它返回一个基本解可行的有效松弛型。

## 线性规划基本定理

这里说明过程 `SIMPLEX` 的却有效。特别地，任何线性规划要么是不可行的，要么是无界的，要么有一个有限目标值的最优解。在每种情况下，`SIMPLEX` 都能做出正确的操作。

《CLRS》**定理 29.13**（**线性规划基本定理**）：任何以标准型给出的线性规划 L 可能会是如下情形：

1. 有一个有限目标值的最优解。
2. 不可行。
3. 无界。

如果 L 是不可行的。`SIMPLEX` 返回“不可行”。如果 L 是无界的，`SIMPLEX` 返回无界。否则，`SIMPLEX` 返回一个有限目标值的最优解。

---

《CLRS》Chapter 29 思考题的一些概念：线性不等式的可行性、互补松弛性、整数线性规划、Farkas 引理、最小代价流通。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/linear-programming/simplex.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 29

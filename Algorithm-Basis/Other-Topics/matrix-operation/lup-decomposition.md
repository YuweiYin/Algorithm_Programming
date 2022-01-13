# Algorithm - Matrix Operation - LUP Decomposition

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

LUP 分解 (LUP Decomposition) 求解线性方程组

很多应用都需要求解一组线性方程组。可以把一个线性方程组的表示成(未知变量的)系数矩阵方程，其中每个矩阵或向量元素属于一个域，通常是实数域 R。可以用 LUP 分解方法来求解线性方程组。

![lup-1](/img/info-technology/algorithm/other-topics/matrix-operation/lup-1.png)

- 如果矩阵 A 的秩小于未知变量数目 n，那么此线性方程组为**欠定的** (underdetermined)。
    - 一个欠定方程组通常有无穷多解，但如果方程组不一致，则可能无解。
- 如果方程的数目超过未知变量数目 n，则该方程组为**超定的** (overdetermined)，且方程组可能无解。
    - 但有一些方法能够寻找超定方程组的一个较好的近似解。

这里主要考察 A 为非奇异矩阵的情况，即 A 的秩等于未知变量的个数 n（也即矩阵 A 的行列式 `|A|` 等于 0）。

求解关于 n 个等式 n 个未知变量的线性方程组 Ax=b，可以先计算出矩阵 A 的逆矩阵 A^{-1}，然后等式两边同时左乘 A^{-1} 得到 x = A^{-1} b。但是此方法在实践中会有**数值不稳定**的问题，而 LUP 分解具有数值稳定性，且在实践中运行速度往往比求逆矩阵的解法更快。

## LUP 分解综述

LUP 分解背后的思想就是找出三个 n x n 的矩阵 L、U 和 P，满足 **P·A = L·U**。其中，L (lower) 是一个**单位下三角矩阵**，U (upper) 是一个**上三角矩阵**，而 P (permutation) 是一个(可逆的/非奇异的)**置换矩阵**(或称“排列矩阵”)。称满足等式 P·A = L·U 的矩阵 L、U 和 P 为 矩阵 A 的 **LUP 分解**。可以证明，每一个非奇异矩阵 A 都存在 LUP 分解。

![lup-2](/img/info-technology/algorithm/other-topics/matrix-operation/lup-2.png)

计算矩阵 A 的一个 LUP 分解的优点是，当相应矩阵（如矩阵 L 和 U）为三角矩阵时，可以很容易地求解线性系统 Ax = b。在等式两边同时左乘 P，得到 PAx = Pb，这意味着置换矩阵 P 对原系数矩阵 A 进行了置换操作，得到 LUx = Pb。现在可以把问题转换为求解两个**三角形线性系统**的解。

1. 首先，定义 y = Ux，其中 x 就是 LUx = Pb 中的 x（待求解的向量）。
2. 然后，通过 **正向替换** 的方法求解 **下三角系统** Ly = Pb，得到向量 y 的解。
3. 最后，通过 **反向替换** 的方法求解 **上三角系统** Ux = y，得到待求解的目标向量 x。

### 正向替换 & 反向替换

在已知 L、P 和 b 的情况下，正向替换可以在 $ \Theta(n^2) $ 的时间内求解下三角系统 Ly = Pb。由于置换矩阵 P 每行每列有且仅有一个 1，其余位置均为 0，所以可以用一个长度为 n 的向量 p[1..n] 来简洁地表达：元素 p[i] 表示矩阵 P[i, p[i]] = 1。因此，矩阵乘积 PA 的第 i 行第 j 列的元素为 $ a_{p[i], j} $，而向量 Pb 的第 i 个元素为 $ b_{p[i]} $。

由于 L 是单位下三角矩阵（主对角线均为 1 的下三角矩阵），可以重写 Ly = Pb 如下：

![lup-3](/img/info-technology/algorithm/other-topics/matrix-operation/lup-3.png)

第一个等式可以直接得到 $ y1 = b_{p[1]} $，得到 y1 后代入第二个等式，可以很容易地求解出 y2，依此类推，把 y1, y2, ..., y_{i-1} “正向替换” 到第 i 个等式中，就可以求解出 $ yi = b_{p[i]} - \sum_{j=1}^{i-1} lij · yj $。据此可求得向量 y。求解了 y 之后，利用“反向替换”求解等式 Ux = y，得到向量 x。

![lup-4](/img/info-technology/algorithm/other-topics/matrix-operation/lup-4.png)

在已知 P、L、U 和 b 的情况下，可以调用下述过程 `LUP_SOLVE` 结合使用正向替换和反向替换，求出 x 的解。

```
LUP_SOLVE(L, U, p, b)
1  n = L.rows
2  let x and y be a new vector of length n
3  for i = 1 to n
4      y_i = b[p[i]] - \sum_{j=1}^{i-1} (l_ij * y_i) 
5  for i = n downto 1
6      x_i = (y_i - \sum_{j=i+1}^{n} (u_ij * x_j)) / u_ii
7  return x
```

过程 `LUP_SOLVE` 在第 3～4 行中通过正向替换求出 y 的解，然后在第 5～6 行中通过反向替换求出 x 的解。因为在每个 for 循环的求和中隐含了一个循环，所以算法的运行时间为 $ \Theta(n^2) $。

### 计算一个 LU 分解

前面说明了，对于非奇异矩阵 A，如果能创建出其 LUP 分解，则可以运用正向替换与反向替换，可求出线性方程组 Ax=b 的解。此小节介绍如何高效地计算出矩阵 A 的一个 LUP 分解。

先考虑 A 是 n x n 非奇异矩阵，且 P 不予考虑（或等价地，P = In 恒等方阵）。在这种情况下，分解 A = LU，称这两个矩阵 L 和 U 为 A 的一个 **LU 分解**。

这里采用**高斯消元法** (Gaussian Elimination) 来创建一个 LU 分解。首先从其它方程中减去第一个方程的倍数，以把那些方程中的第一个变量消去。然后，从第三个及以后的方程中减去第二个方程的倍数，以把这些方程的第一个和第二个变量都消去。继续上述过程，直到系统变为一个上三角矩阵形式，此矩阵就是 LU 分解中的 U (Upper) 上三角矩阵。而矩阵 L 是由消去变量所用的行的乘数组成。

![lup-5](/img/info-technology/algorithm/other-topics/matrix-operation/lup-5.png)

![lup-6](/img/info-technology/algorithm/other-topics/matrix-operation/lup-6.png)

但是如果元素 a11 == 0，**舒尔补** (Schur complement) A' 会有除 0 的问题。另外，如果 舒尔补 这个 (n-1) x (n-1) 矩阵的左上角元素为 0，上述分解方法也不可行，因为下一次递归就要除以此元素。

在 LUP 分解中，所除的元素被称为 **主元** (pivot)，它们处于矩阵 U 的主对角线上。在 LUP 中包含一个置换矩阵 P 正是为了避免递归分解过程中把 0 当作除数。采用置换来避免除数为 0（或者一个接近于 0 的很小的数，除以这样的数可能会引起数值不稳定性）的操作被称为 **选主元** (pivoting)。

保证 LU 分解总能进行的一类重要矩阵是**对称正定矩阵**。这一类矩阵无需选主元，因此可以不使用置换矩阵 P 就应用前述递归策略，无需担心除数为 0。

对一个矩阵 A 进行 LU 分解的代码根据上述递归策略设计，并且将尾递归（即最后的操作为自身递归调用的过程）改为迭代循环过程。初始化**上三角矩阵 U**，使其对角线以下元素均为 0；初始化**单位下三角矩阵 L**，使其对角线以上元素均为 0，并且主对角线元素均为 1。每次迭代都作用于一个子方阵，以其左上角元素为为**主元**来计算向量 v 和 w 以及舒尔补 A'，这样又会生成一个子方阵，以供下次迭代作用。

```
LU_DECOMPOSITION(A)
1  n = A.rows
2  let L and U be new n x n matrices
3  initialize U with 0s below the diagonal
4  initialize L with 1s on the diagonal and 0s above the diagonal
5  for k = 1 to n
6      u_kk = a_kk
7      for i = k+1 to n
8          l_ik = a_ik / u_kk    // a_ik holds vi
9          u_ki = a_ki           // a_ki holds wi
10     for i = k+1 to n
11         for j = k+1 to n
12             a_ij = a_ij - l_ik * u_kj
13 return L and U
```

算法过程描述如下：

1. 在 1 行，获取矩阵规模
2. 在 2～4 行，初始化单位下三角矩阵 L 和上三角矩阵 U。
3. 在 5～12 行的循环中，对不同规模的矩阵进行 LU 分解。
    - 在 6 行，选取主元为 `U[k][k] = A[k][k]`
    - 在 7～9 行的 for 循环（当 k == n 时，此循环不执行）中，采用向量 v 和 w^{T} 对 L 和 U 进行更新。
        - 在 8 行，把 `v[i]` 除以主元 `U[k][k]` 的结果存放在 `L[i][k]` 中（这里除以主元，第 12 行就不用除了）
        - 在 9 行，把 `w[i]` 存放在 `U[k][i]` 中
    - 在 10～12 行的 for 循环中，计算舒尔补中的元素，并把结果存放在 `A[i][j]` 中
4. 在 13 行，最终返回矩阵 L 和 U

由于该算法有三层循环嵌套，所以 `LU_DECOMPOSITION(A)` 的运行时间为 $ \Theta(n^3) $。另外，可以对上述算法的空间复杂度优化，不必新建 L 和 U 矩阵，而是直接利用矩阵 A 的空间来存储 L 和 U 的元素（因为不会重复利用之前的 A 中元素），做法只需把伪代码中的每处 l 和 u 用 a 取代即可。

![lup-7](/img/info-technology/algorithm/other-topics/matrix-operation/lup-7.png)

### 计算一个 LUP 分解

前面提到，如果 A 是**对称正定矩阵**，可以不使用置换矩阵 P 就应用前述递归策略，无需担心除数为 0。但对于任意的矩阵 A 而言，为了求解线性方程组 Ax=b，必须在 A 的非对角线元素中选主元以避免除数为 0。除数为 0 当然是灾难性的，但是也应避免除数很接近于 0（即便 A 是非奇异的），否则会产生数值不稳定。因此，需要选择一个较大的主元。

LUP 分解的数学原理与 LU 分解很类似。在对矩阵 A 进行划分之前，先把一个非零元素（比如 ak1）从第一列中某个位置移动到该矩阵的 (1, 1) 的位置上。为了保证数值稳定性，选择第 1 列中具有最大绝对值的元素为 ak1。（由于矩阵 A 是非奇异的，所以其任何列都不可能全为 0）为了使方程组仍然成立，把第 1 行与第 k 行互换，这等价于用一个置换矩阵 Q 乘以 A 的左边。

因此可以把 QA 写成：`QA = [[ak1, w^{T}], [v, A']]`。其中 `v = (a21, a31, ..., an1)^T`，除了 a11 取代 ak1；`w^{T} = (ak2, ak3, ..., akn)`；而舒尔补 A' 是一个 (n-1) x (n-1) 规模的矩阵。

![lup-8](/img/info-technology/algorithm/other-topics/matrix-operation/lup-8.png)

注意在上述推导中，与 LU 分解不同的是：必须把列向量 `v / ak1` 和 舒尔补 `A' - v·w^{T} / ak1` 都乘以置换矩阵 P'。下面是 LUP 分解的伪代码：

```
LUP_DECOMPOSITION(A)
1  n = A.rows
2  let p[1..n] be a new array
3  for i = 1 to n
4      p[i] = i
5  for k = 1 to n
6      p = 0
7      for i = k to n
8          if |a_ik| > p
9              p = |a_ik|
10             k' = i
11     if p == 0
12         error "A is a singular matrix"
13     exchange p[k] with p[k']
14     for i = 1 to n
15         exchange a_ki with a_k'i
16     for i = k+1 to n
17         a_ik = a_ik / a_kk
18         for j = k+1 to n
19             a_ij = a_ij - a_ik * a_kj
20 return A
```

作为 LU 分解的改进，动态维护置换矩阵呢 P 作为一个长度为 n 的数组 p，其中 p[i] == j 表示置换矩阵 P 的元素 `P[i][j] == 1`。上述算法在 6～10 行选择了主元，实现了在矩阵 A 中使用“合适的主元”来计算 L 和 U，并在 13 行维护置换矩阵 p。另外在 14～15 行，把置换操作应用在矩阵 A 上。

当过程 `LUP_DECOMPOSITION(A)` 结束时，矩阵 A 中同时保存了 L 和 U 的元素：

- 如果 i >  j，则 `A[i][j] == L[i][j]`
- 如果 i <= j，则 `A[i][j] == U[i][j]`

当然，如果不希望改变原矩阵 A，可以在算法一开始重新开辟一个二维数组，并赋值为 A 即可。

![lup-9](/img/info-technology/algorithm/other-topics/matrix-operation/lup-9.png)

因为 `LUP_DECOMPOSITION` 的三重循环结构，所以它的运行时间为 $ \Theta(n^3) $，与 `LU_DECOMPOSITION` 的渐近运行时间一样。选主元的操作至多花费常数因子时间。

## 矩阵求逆

虽然在实际应用中，一般不使用逆矩阵来求解线性方程组，而更倾向于运用一些数值稳定性更好的技术，如 LUP 分解。但是有时候需要计算一个矩阵的逆矩阵，来完成别的任务。而 LUP 分解也可以用于计算一个矩阵的逆。

另外，可以证明 矩阵乘法 和 计算逆矩阵问题 具有相同的渐近时间复杂度，可以用用于矩阵乘法的 [Strassen 算法](../../divide-conquer/matrix-strassen) 来求一个矩阵的逆矩阵。事实上，Strassen 原始论文的动机正是表明有比普通方法更快的求解线性方程组的方法。

### 通过 LUP 分解计算逆矩阵

假设有一个矩阵 A 的 LUP 分解，包括三个矩阵 L、U 和 P，满足 P·A = L·U。运用 `LUP_SOLVE` 过程，可以在 $ \Theta(n^2) $ 时间内求解一个具有 Ax=b 形式的方程。因为 LUP 分解取决于 A 而不是 b，所以改变向量 b，能够不必重算 LUP 分解，直接在第二个方程 Ax=b' 上运行 `LUP_SOLVE` 过程。

考虑方程 A·X = In（其中 In 为单位矩阵），它以一个含 n 个方程（每个方程的形式为 Ax=b）的方程组方式定义了矩阵 X，即 A 的逆矩阵。令 Xi 表示 X 的第 i 列，单位向量 ei 是 In 的第 i 列，于是可以利用 A 的 LUP 分解来求解方程 A·X = In 中的 X，即分别求解每一个方程 A·Xi = ei 中的 Xi 即可。

一旦以 $ \Theta(n^3) $ 运行时间得到矩阵 A 的 LUP 分解后，就可以在 $ \Theta(n^2) $ 时间内计算每个 Xi，因此总共可以在 $ \Theta(n^3) $ 的时间内求出矩阵 A 的逆矩阵 A^{-1}。

### 矩阵乘法和矩阵求逆

可以证明，矩阵乘法获得的理论上的加速比，矩阵求逆的运算同样可以达到。实际上，更进一步可以得到更强的结论：从下面描述的角度看来，矩阵求逆运算**等价于**矩阵乘法运算。

如果 M(n) 表示求两个 n x n 矩阵乘积所需的时间，那么可以在 O(M(n)) 时间内对一个 n x n 的非奇异矩阵求逆。此外，如果 I(n) 表示对一个非奇异的 n x n 矩阵求逆所需的时间（I 表示 Inverse），那么可以在 O(I(n)) 时间内对两个 n x n 矩阵求乘积。下面的两个定理用于证明前述结论。

《CLRS》**定理 28.1**（**矩阵乘法不比矩阵求逆更困难**）：如果能在 I(n) 时间内求出一个 n x n 的**非奇异矩阵的逆**，其中 I(n) = $ \Omega(n^2) $ 且 I(n) 满足**正则性条件** I(3n) = O(I(n))，那么可以在 O(I(n)) 时间内求出两个 n x n 矩阵的乘积。

![lup-10](/img/info-technology/algorithm/other-topics/matrix-operation/lup-10.png)

《CLRS》**定理 28.2**（**矩阵求逆不比矩阵乘法更困难**）：如果能在 M(n) 时间内求出两个 n x n 的**实数**矩阵的乘积，其中 M(n) = $ \Omega(n^2) $ 且 M(n) 满足**两个正则性条件**：1. 对**任意的 k** (0 <= k <= n) 有 M(n+k) = O(M(n))；2. 对**某个常数 c** < 1/2 有 M(n/2) <= c M(n)，那么可以在 O(M(n)) 时间内求出**任何一个** n x n **非奇异实数矩阵**的逆。

定理 28.2 的证明赖于**对称正定矩阵**的一些性质，证明详见《CLRS》Chapter 28.2 和 28.3。

定理 28.2 的证明过程还说明：只要 A 是**非奇异矩阵**，就可以通过 LU 分解求解方程 Ax=b，而**无需使用置换矩阵** P 来选取主元。在 A 是非奇异矩阵的情况下，把等式两边同时左乘 A^{T} 得到 (A^{T} A)x = A^{T} b。因为 A^{T} 是可逆的，所以这一变换不会影响解 x，于是可以通过计算 LU 的一个分解来分解**对称正定矩阵 A^{T} A**。然后就可以对方程右端的 A^{T} b 应用**正向替换**和**反向替换**来求解 x。

上述这样操作在理论上是能正确求解 x 的，但实际上过程 `LUP_DECOMPOSITION` 执行得更快。LUP 分解需要的算术运算次数要比上述方法少常数倍，并且 LUP 分解往往有更好的数值稳定性。

---

此外，可以推广定理 28.2 的矩阵求逆算法，使之能处理**复数矩阵**的情形。

方法：用 A 的 **共轭转置矩阵** (conjugate transpose) A\* 来替代 A 的转置矩阵（把 A 中的每个元素用其**共轭复数**来替代就得到矩阵 A\*）。并且用 **埃尔米特矩阵** (Hermitian Matrix) 来替代对称矩阵（埃尔米特矩阵就是满足 A = A\* 的矩阵 A）。

## 奇异值分解 SVD

奇异值分解 (Singular Value Decomposition, SVD) 是另一种重要的矩阵分解。

SVD 把一个 m x n 矩阵 A 分解成 $ A = P \Sigma Q $，其中 $ \Sigma $ 是一个只在主对角线上有非零元素的 m x n 矩阵（往往对应着矩阵 A 的各个**特征值**，从高到低放置），P 是一个**列**互相**标准正交**的 m x m 方阵，Q 是一个**列**互相**标准正交**的 n x n 方阵。（如果两个向量内积为 0 并且每个向量范数为 1，则它们是**标准正交**的。）

SVD 分解可用于矩阵的压缩，而由于图像等数据往往以矩阵方式存放，所以 SVD 可以用于压缩图像。“压缩”的实际做法就是保留下高特征值的部分，而舍去“不重要”的部分。普通的特征值分解仅针对于方阵，而 SVD 分解可以作用于一般的矩阵。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/matrix-operation/lup-decomposition.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 28

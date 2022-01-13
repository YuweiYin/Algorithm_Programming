# Algorithm - Matrix Operation

Algorithm - [YuweiYin](https://github.com/YuweiYin)

## 目录

- 矩阵运算 Matrix Operation
	- 矩阵检查
		- 合法性检查
		- 加/减法相容性检查 (两矩阵形状/规模相同)
		- 矩阵乘法相容性检查
	- 矩阵转置
	- 矩阵乘法
		- 普通矩阵乘法
		- 分治的矩阵乘法
		- [Strassen 算法](../../divide-conquer/matrix-strassen)
	- 矩阵分解
		- [LUP 三角分解](lup-decomposition) 求解线性方程组
		- SVD 奇异值分解
	- 矩阵求逆
		- 用 LUP 分解方法求矩阵的逆
	- 对称正定矩阵和最小二乘逼近
		- 求超定线性方程组的最小二乘解

## 矩阵运算

矩阵运算在科学计算中极为重要，所以处理矩阵的高效算法有很多实际应用。

## 对称正定矩阵和最小二乘逼近

对称正定矩阵有许多有趣和理想的性质。例如，它们都是非奇异矩阵，而且对其进行 LU 分解时无需担心出现除数为 0 的情形。

《CLRS》**引理 28.3**：任何对称正定矩阵都是非奇异矩阵。

《CLRS》**引理 28.4**：如果 A 是一个对称正定矩阵，那么 A 的每一个主子矩阵都是对称正定的。

《CLRS》**引理 28.5**（**舒尔补引理**）：如果 A 是一个对称正定矩阵，Ak 是 A 的 k x k 主子矩阵，那么 A 关于 Ak 的舒尔补湿对称正定的。

《CLRS》**引理 28.6**：一个对称正定矩阵的 LU 分解永远不会出现除数为 0 的情形。

### 最小二乘逼近

对给定一组数据的点进行**曲线拟合**是对称正定矩阵的一个重要应用。

假设已知 m 个数就点 (x1, y1), ..., (xm, ym)，其中已知 yi 受到**测量误差**的影响。目标是确定一个函数 F(x)，对 i = 1, 2, ..., m，使得**近似误差** $ \eta_{i} = F(x_{i}) - y_{i} $ 很小。

函数 F 的形式依赖于具体的问题，这里假设它为一个线性加权和 $ F(x) = \sum_{j=1}^{n} c_{j} f_{j}(x) $。其中和项的个数和特定的**基函数** (base function) fj 取决于对问题的先验知识。

一种很通常的选择是 $ f_{j}(x) = x^{j-1} $，从而使得 $ F(x) = c_{1} + c_{2} x + ... + c_{n} x^{n-1} $ 是一个 x 的 n-1 次多项式，目标是计算出 n 个系数 c1, ..., cn 似的误差 $ \eta_{1}, \eta_{2}, ..., \eta_{m} $ 最小。

通过选择 n == m，可以精确计算每个 yi。这样一个高次函数 F 吻合数据，但也“吻合噪声”，而且根据前所未知的 x 值来预测 y 值时，通常会给出很差的结果。（“过拟合”）

较好的做法是选择比 m 小很多的 n，即希望通过选择系数 cj 可以获得一个函数 F，从而发现数据点中的重要模式（数据挖掘、模式识别），而不过多地受噪声影响。

一旦选定了比 m 小的 n 值，就得到了一个**超定方程组**，目标是近似求解此方程组。

![matrix-operation-1](/img/info-technology/algorithm/other-topics/matrix-operation/matrix-operation-1.png)

![matrix-operation-2](/img/info-technology/algorithm/other-topics/matrix-operation/matrix-operation-2.png)

![matrix-operation-3](/img/info-technology/algorithm/other-topics/matrix-operation/matrix-operation-3.png)

![matrix-operation-4](/img/info-technology/algorithm/other-topics/matrix-operation/matrix-operation-4.png)

## 数值稳定性 Numerical Stability

在实际的**数值计算**中一个重要问题是**数值的稳定性** (Numerical Stability)。由于在实际的计算机中浮点数表示的精度有限，因此在数值计算过程中的**舍入误差**可能会被放大（例如在循环、递归的重复计算过程中被逐步放大），从而导致不正确的、误差很大的结果，称这样的计算是**数值不稳定的**。

关于数值稳定性的讨论，可以详见**数值计算**学科，此学科的核心问题之一 就是控制计算过程中的误差。

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 28

# 指数
基数^指数 = 对数

## 加法

- 数学表达式
$$ x^3x^3 = x^{3+3} $$

$$ X^AX^B = X^{A+B} $$

- python代码
```python
# 2 为基数(底数) 3为指数 8为对数
import math
math.pow(2, 3) * math.pow(2, 3) == math.pow(2, (3+3))
```


## 减法

- 数学表达式
$$ \frac{X^A}{X^B} = X^{A-B} $$

- Python代码
```python
from math import pow
pow(2, 6) / pow(2, 3) == pow(2, (6-3))
```

## 指数的幂

- 数学表达式
$$ (X^A)^B = X^{AB} $$

- Python代码
```python
from math import pow
pow(pow(2, 3), 3) == pow(2, (3*3))
```

## --


- 数学表达式
$$ X^N + X^N = 2X^N \neq X^{2N} $$

- Python代码
```python

In [1]: from math import pow

In [2]: pow(2, 3) + pow(2, 3) == pow(2,3) * 2
Out[2]: True

In [3]: pow(2, 3) + pow(2, 3)
Out[3]: 16.0

In [4]: pow(2, 6)
Out[4]: 64.0

In [6]: pow(2, 3) + pow(2, 3) == pow(2, (3 *2))
Out[6]: False


```

## 2 的指数

- 数学表达式
$$ 2^N + 2^N = 2^{N+1} $$

- Python代码
```python

In [5]: pow(2, 3) + pow(2, 3) == pow(2, (3+1))
Out[5]: True

```

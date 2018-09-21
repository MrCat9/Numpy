# -*- coding: utf-8 -*-
# 摘自 https://zhuanlan.zhihu.com/p/24309547
import numpy as np

a = np.array([3, 4])
np.linalg.norm(a)

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = np.array([1, 0, 1])

# 矩阵和向量之间的乘法
print(np.dot(b, c))         # [ 4 10 16]
print(np.dot(c, b.T))       # [ 4 10 16]

# 求矩阵的迹
print(np.trace(b))      # 15

# 求矩阵的行列式值
print(np.linalg.det(b))     # 0.0

# 求矩阵的秩
print(np.linalg.matrix_rank(b))     # 2    # 不满秩，因为行与行之间等差

print("----------------------")

d = np.array([
    [2, 1],
    [1, 2]
])

'''
对正定矩阵求本征值和本征向量
本征值为u，array([ 3.,  1.])
本征向量构成的二维array为v，
array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]])
是沿着45°方向
eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
'''
u, v = np.linalg.eig(d)
print(u)        # [3. 1.]
print(v)
'''
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
'''

print("----------------------")

# Cholesky分解并重建
l = np.linalg.cholesky(d)
print("l = ")
print(l)
'''
[[1.41421356 0.        ]
 [0.70710678 1.22474487]]
'''

print("np.dot(l, l.T) = ")
print(np.dot(l, l.T))
'''
np.dot(l, l.T) = 
[[2. 1.]
 [1. 2.]]
'''

print("----------------------")

e = np.array([
    [1, 2],
    [3, 4]
])

# 对不镇定矩阵，进行SVD分解并重建
U, s, V = np.linalg.svd(e)

S = np.array([
    [s[0], 0],
    [0, s[1]]
])
print("S = ")
print(S)
'''
S = 
[[5.4649857  0.        ]
 [0.         0.36596619]]
'''

np.dot(U, np.dot(S, V))
print("np.dot(U, np.dot(S, V)) = ")
print(np.dot(U, np.dot(S, V)))
'''
np.dot(U, np.dot(S, V)) = 
[[1. 2.]
 [3. 4.]]
'''
# -*- coding: utf-8 -*-
# 摘自 https://zhuanlan.zhihu.com/p/24309547
import numpy as np

# 绝对值
a = np.abs(-1)
print("a =", a)     # a = 1

print("----------------------")

# sin函数
b = np.sin(np.pi/2)
print("b =", b)     # b = 1.0

print("----------------------")

# tanh逆函数
c = np.arctanh(0.462118)
print("c =", c)     # c = 0.5000010715784053

print("----------------------")

# e为底的指数函数
d = np.exp(3)
print("d =", d)     # d = 20.085536923187668

print("----------------------")

# 2的3次方
f = np.power(2, 3)
print("f =", f)     # f = 8

print("----------------------")

# 点积，1*3+2*4=11
g = np.dot([1, 2], [3, 4])
print("g =", g)     # g = 11

print("----------------------")

# 开方
h = np.sqrt(25)
print("h =", h)     # h = 5.0

print("----------------------")

# 求和
l = np.sum([1, 2, 3, 4])
print("l =", l)     # l = 10

print("----------------------")

# 平均值
m = np.mean([4, 5, 6, 7])
print("m =", m)     # m = 5.5

print("----------------------")

# 标准差
p = np.std([1, 2, 3, 2, 1, 3, 2, 0])
print("p =", p)     # p = 0.9682458365518543

print("----------------------")
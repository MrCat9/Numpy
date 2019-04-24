# -*- coding: utf-8 -*-

import numpy as np


a = np.array([1,2,3,3,4,5])
print(a.shape)  # (6,)

a = np.array([[1,2,3,3,4,5]])
print(a.shape)  # (1, 6)

a = np.array([[[1,2,3,3,4,5]]])
print(a.shape)  # (1, 1, 6)

a = np.array([[[1,2,3,3,4,5]], [[1,2,3,3,4,5]]])
print(a.shape)  # (2, 1, 6)

a = np.array([[[1,2,3,3,4,5],[1,2,3,3,4,5]]])
print(a.shape)  # (1, 2, 6)


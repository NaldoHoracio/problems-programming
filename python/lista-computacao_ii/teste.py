# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:07:17 2021

@author: edvon
"""

import numpy as np

arr_2d = np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]])

# Check row wise
result = np.all((arr_2d == 0), axis=1)
print('Rows that contain only zero:')
for i in range(len(result)):
    if result[i]:
        print('Row: ', i)
        break
    else:
        print("Lines NO zeros!")

# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:40:33 2025

@author: Administrator
"""

import numpy as np
import overlap1

r_one = np.array([0.0, 0.0, 0.0], dtype=np.float64)
box_length = 10.0
r = np.random.rand(10, 3)*box_length

sigma = 1.0

result = overlap1.Overlap1(r_one, r, box_length, sigma)
print("Overlap:", result)

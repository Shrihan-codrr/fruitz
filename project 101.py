# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 18:41:38 2022

@author: Anupam
"""

import matplotlib
import matplotlib.pyplot as plt 

data = [[0,0,0,0,0,0,0,7,7,7,0,0,0,],
        [0,0,0,0,0,0,7,7,7,7,7,0,0,],
        [0,0,0,0,9,9,9,9,9,0,0,0,0,],
        [0,0,0,9,8,8,8,8,8,9,0,0,0,],
        [0,0,9,8,1,8,8,8,8,8,9,0,0,],
        [0,9,8,1,8,8,8,8,8,8,8,9,0,],
        [0,9,8,1,8,8,8,8,8,8,8,9,0,],
        [0,0,9,8,1,8,8,8,8,8,9,0,0,],
        [0,0,9,8,8,8,8,8,8,8,9,0,0,],
        [0,0,0,9,8,8,8,8,8,9,0,0,0,],
        [0,0,0,0,9,9,9,9,9,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,],
        ]


plt.imshow(data , cmap = "tab20b_r")
plt.show()
"""
8 = light blue
9 - darkblue
7 = darkgreen
6 - light green
"""

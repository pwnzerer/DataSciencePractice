# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#creating temp practice data

x = np.arange(0,100)
y = x*2
z = x**2

fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
#plotception
ax2 = fig1.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y)
ax2.plot(y,x,color='red')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('TITLE')

#subplots for 2 columns and 1 row
fig,axes = plt.subplots(1,2)
axes[0].plot(x,y,lw=5)
axes[1].plot(y,z,color='red')



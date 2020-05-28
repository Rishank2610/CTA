'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
#fig = plt.figure(figsize=plt.figaspect(0.5))
#ax = fig.gca(projection='3d')

#plot1
ax = fig.add_subplot(2, 2, 1, projection='3d')
X = [500,1000,2000,5000,10000]
Y = [-2, -1, 1]
X, Y = np.meshgrid(X, Y)
Z_index_mean = np.array([[2.220312195, 2.220193922, 2.22012838, 2.219883102, 2.219839644], [2.219842705, 2.220235432, 2.219804438, 2.219688481, 2.219619625], [2.216910196, 2.218558143, 2.218543419, 2.21881319, 2.218607128]])

surf = ax.plot_surface(X, Y, Z_index_mean, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(2.215, 2.221)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

#Plot2
ax = fig.add_subplot(2, 2, 2, projection='3d')
X = [500,1000,2000,5000,10000]
Y = [-2, -1, 1]
X, Y = np.meshgrid(X, Y)
Z_index_std = np.array([[0.009250108063, 0.008904217945, 0.00879843664, 0.009005902503, 0.008943996911], [0.01348043648, 0.01263336737, 0.01251351172, 0.01264026638, 0.01249817483], [0.03217920184, 0.03227131651, 0.0326440207, 0.03269495349, 0.03268050912]])

surf = ax.plot_surface(X, Y, Z_index_std, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(0.0088, 0.0327)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

#plot3
ax = fig.add_subplot(2, 2, 3, projection='3d')
X = [500,1000,2000,5000,10000]
Y = [-2, -1, 1]
X, Y = np.meshgrid(X, Y)
Z_flux_mean = np.array([[1.289643779, 1.289234866, 1.290207314, 1.290259548, 1.290319322], [1.289643779, 1.289234866, 1.290207314, 1.290259548, 1.290319322], [1.302369174, 1.297517598, 1.297008635, 1.296317397, 1.297018173]])

surf = ax.plot_surface(X, Y, Z_flux_mean, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(1.289, 1.3105)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

#plot4
ax = fig.add_subplot(2, 2, 4, projection='3d')
X = [500,1000,2000,5000,10000]
Y = [-2, -1, 1]
X, Y = np.meshgrid(X, Y)
Z_flux_std = np.array([[1.806115106, 1.852874394, 1.874085261, 1.871370957, 1.856881933], [3.018332627, 2.89267863, 2.881269441, 2.86175259, 2.835130098], [10.06700062, 10.0355245, 10.2197753, 10.23697792, 10.20893349]])

surf = ax.plot_surface(X, Y, Z_flux_std, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(1.8, 10.21)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

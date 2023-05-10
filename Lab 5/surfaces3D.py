import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Hyperbolic Paraboloid
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)           # make a mesh, two 2D arrays, and assign 2D arrays to X and Y
a, b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')
plt.show()

# Elliptic Paraboloid
ax1 = plt.axes(projection='3d')
r = np.linspace(0, 1, 30)
t = np.linspace(0, 2*np.pi, 30)
R, T = np.meshgrid(r, t)
X = R * np.cos(T)
Y = R * np.sin(T)
a, b, c = 0.75, 1, 1
Z = c*((X**2)/(a**2) + (Y**2)/(b**2))
ax1.contour3D(X, Y, Z, 50)
ax1.set_title('Elliptic Paraboloid')
plt.show()

# Ellipsoid
ax2 = plt.axes(projection='3d')
r = np.linspace(0, 1, 30)
t = np.linspace(0, 2*np.pi, 30)
R, T = np.meshgrid(r, t)
X = R * np.cos(T)
Y = R * np.sin(T)
a, b, c = 1, 1, 1
Z = np.sqrt((c**2 * (1 - (X**2/a**2 + Y**2/b**2))))
ax2.contour3D(X, Y, Z, 50)
ax2.set_title('Ellipsoid')
plt.show()

# Cone
ax3 = plt.axes(projection='3d')
r = np.linspace(0, 1, 30)
t = np.linspace(0, 2*np.pi, 30)
R, T = np.meshgrid(r, t)
X = R * np.cos(T)
Y = R * np.sin(T)
Z = np.sqrt(X**2 + Y**2)
ax3.contour3D(X, Y, Z, 50)
ax3.set_title('Cone')
plt.show()

# Square Pyramid
ax4 = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.zeros((30, 30))
for i in range(30//2):
    for j in range(i, 30-i):
        for h in range(i, 30-i):
            Z[j, h] = i

ax4.contour3D(X, Y, Z, 50)
ax4.set_title('Square Pyramid')
plt.show()

# Parallelepiped
ax5 = plt.axes(projection='3d')
Z = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
              [0, -1, 1], [2, -1, 1], [2, 1, 1], [0, 1, 1]])

verts = [[Z[0], Z[1], Z[2], Z[3]],
         [Z[4], Z[5], Z[6], Z[7]],
         [Z[0], Z[1], Z[5], Z[4]],
         [Z[2], Z[3], Z[7], Z[6]],
         [Z[1], Z[2], Z[6], Z[5]],
         [Z[4], Z[7], Z[3], Z[0]]]

ax5.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])
ax5.add_collection3d(Poly3DCollection(verts, facecolors='white', linewidths=1, edgecolors='black', alpha=0.75))
ax5.set_title('Parallelepiped')
plt.show()

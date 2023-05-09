import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b, c = 0.75, 1, 1
Z = c*((X**2)/(a**2) + (Y**2)/(b**2))
ax1.contour3D(X, Y, Z, 50)
ax1.set_title('Elliptic Paraboloid')
plt.show()

# Ellipsoid
ax2 = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b, c = 1, 1, 1
Z = np.sqrt((c**2 * (1 - (X**2/a**2 + Y**2/b**2))))  # fix warning
ax2.contour3D(X, Y, Z, 50)
ax2.set_title('Ellipsoid')
plt.show()

# Cone
ax3 = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
ax3.contour3D(X, Y, Z, 50)
ax3.set_title('Cone')
plt.show()

# Square Pyramid
ax4 = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
print(X.shape)
ax4.contour3D(X, Y, X, 50)
ax4.set_title('Square Pyramid')
plt.show()
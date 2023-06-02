import numpy as np
import matplotlib.pyplot as plt


def pyramid(base, height):
    r = np.array([0, 1])
    t = np.linspace(0, 2*np.pi, base+1)
    T, R = np.meshgrid(t, r)

    x = R * np.cos(T)
    y = R * np.sin(T)

    z = np.ones(x.shape)
    z[0] = z[0] * height
    z[1] = z[1] * 0

    return x, y, z


if __name__ == '__main__':
    fig = plt.figure(tight_layout=True)
    ax = fig.add_subplot(121, projection='3d')
    x, y, z = pyramid(4, 5)
    ax.contour3D(x, y, z, 50)
    ax = fig.add_subplot(122, projection='3d')
    x, y, z = pyramid(6, 10)
    ax.contour3D(x, y, z, 50)
    plt.show()

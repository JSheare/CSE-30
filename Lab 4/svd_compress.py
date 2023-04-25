import matplotlib.pyplot as plt
from numpy import linalg as la
import numpy as np
import matplotlib.image as mpimg


# Method 1
def compress(image, k):
    X, Y, Z = image.shape
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    colors = [red, green, blue]
    approx_colors = []
    for color in colors:
        U, s, Vt = la.svd(color)
        Sigma = np.zeros((X, Y))
        for i in range(X):
            Sigma[i, i] = s[i]

        color_approx = U @ Sigma[:, :k] @ Vt[:k, :]
        approx_colors.append(color_approx)

    image_approx = np.stack(tuple(approx_colors), axis=2)
    image_approx -= image_approx.min()
    image_approx /= image_approx.max()
    return image_approx


# Method 2
def compress2(image, k):
    X, Y, Z = image.shape
    image_transpose = np.transpose(image, (2, 0, 1))
    U, s, Vt = la.svd(image_transpose)
    Sigma = np.zeros((Z, X, Y))
    for j in range(3):
        np.fill_diagonal(Sigma[j, :, :], s[j, :])

    image_approx = U @ Sigma[:, :, :k] @ Vt[:, :k, :]
    image_approx = np.transpose(image_approx, (1, 2, 0))
    image_approx -= image_approx.min()
    image_approx /= image_approx.max()
    return image_approx


if __name__ == '__main__':
    # read the image file and display the image
    img = mpimg.imread('octopus.jpg')
    plt.imshow(img)
    plt.show()

    # analyze the image array
    print(img.ndim)
    print(img.shape)
    print(img.dtype)
    print(img.max())
    print(img.min())
    print('\n')

    img_approx = compress(img, 50)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)

    img_approx = compress2(img, 50)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new1.jpg", img_approx)

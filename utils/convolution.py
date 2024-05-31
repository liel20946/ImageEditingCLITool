import numpy as np


def convolve_md(image_array, kernel):
    """
    Apply a convolution kernel to a multi-dimensional image array.
    :param image_array: the image numpy array.
    :param kernel: the convolution kernel.
    :return: the convolved image array.
    """
    kernel = np.flipud(np.fliplr(kernel))

    image_height, image_width, channels = image_array.shape
    kernel_height, kernel_width = kernel.shape

    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image_array, ((pad_height, pad_height),
                                        (pad_width, pad_width), (0, 0)),
                          mode='constant')

    convolved_image = np.zeros_like(image_array)

    for c in range(channels):
        for i in range(image_height):
            for j in range(image_width):
                convolved_image[i, j, c] = np.sum(
                    padded_image[i:i + kernel_height,
                    j:j + kernel_width, c] * kernel)
    return convolved_image


def convolve_2d(image_array, kernel):
    """
    Apply a convolution kernel to a 2D image array.
    :param image_array: the image numpy array.
    :param kernel: the convolution kernel.
    :return: the convolved image array.
    """
    kernel = np.flipud(np.fliplr(kernel))

    image_height, image_width = image_array.shape
    kernel_height, kernel_width = kernel.shape

    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image_array, ((pad_height, pad_height),
                                        (pad_width, pad_width)),
                          mode='constant')

    convolved_image = np.zeros_like(image_array)

    for i in range(image_height):
        for j in range(image_width):
            convolved_image[i, j] = np.sum(
                padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)
    return convolved_image

import numpy as np


def convolve_md(image_array, kernel):
    """
    Apply a convolution kernel to an mD image array.

    Args:
        image_array (numpy.ndarray): The image array.
        kernel (numpy.ndarray): The convolution kernel.

    Returns:
        numpy.ndarray: The convolved image array.
    """
    # flip the kernel
    kernel = np.flipud(np.fliplr(kernel))
    # Get the dimensions of the image and kernel

    image_height, image_width, channels = image_array.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding needed
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Create a padded image array
    padded_image = np.pad(image_array, ((pad_height, pad_height),
                                        (pad_width, pad_width), (0, 0)),
                          mode='constant')

    # Create an empty image array to store the convolved image
    convolved_image = np.zeros_like(image_array)

    # Apply the convolution kernel to the image
    for c in range(channels):
        for i in range(image_height):
            for j in range(image_width):
                convolved_image[i, j, c] = np.sum(
                    padded_image[i:i + kernel_height,j:j + kernel_width, c] * kernel)

    return convolved_image


def convolve_2d(image_array, kernel):
    """
    Apply a convolution kernel to a 2D image array.

    Args:
        image_array (numpy.ndarray): The image array.
        kernel (numpy.ndarray): The convolution kernel.

    Returns:
        numpy.ndarray: The convolved image array.
    """
    # flip the kernel
    kernel = np.flipud(np.fliplr(kernel))
    # Get the dimensions of the image and kernel
    image_height, image_width = image_array.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding needed
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Create a padded image array
    padded_image = np.pad(image_array, ((pad_height, pad_height),
                                        (pad_width, pad_width)),
                          mode='constant')

    # Create an empty image array to store the convolved image
    convolved_image = np.zeros_like(image_array)

    # Apply the convolution kernel to the image
    for i in range(image_height):
        for j in range(image_width):
            convolved_image[i, j] = np.sum(
                padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)

    return convolved_image


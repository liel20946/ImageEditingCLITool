import numpy as np

# Constants
RGB_SHAPE_LENGTH = 3
RGBA_CHANNEL_SIZE = 4
GREYSCALE_SHAPE_LENGTH = 2
# weights for RGB to greyscale conversion
RED_WEIGHT = 0.2989
GREEN_WEIGHT = 0.5870
BLUE_WEIGHT = 0.1140
# rgb range
RGB_MIN_VALUE = 0
RGB_MAX_VALUE = 255
RGB_MIDDLE_VALUE = 128
# Indexes
CHANNEL_SIZE_INDEX = 2


def rgb_to_hsv(rgb):
    """ convert RGB to HSV color space
    :param rgb: np.ndarray
    :return: np.ndarray
    """
    rgb = rgb.astype('float') / RGB_MAX_VALUE
    max_v = np.amax(rgb, axis=2)
    max_c = np.argmax(rgb, axis=2)
    min_v = np.amin(rgb, axis=2)
    min_c = np.argmin(rgb, axis=2)
    hsv = np.zeros(rgb.shape, dtype='float')
    delta = max_v - min_v + np.spacing(1)

    max_c_0_0 = ((rgb[..., 1] - rgb[..., 2]) * 60.0 / delta) % 360.0
    max_c_1_0 = ((rgb[..., 2] - rgb[..., 0]) * 60.0 / delta) + 120.0
    max_c_2_0 = ((rgb[..., 0] - rgb[..., 1]) * 60.0 / delta) + 240.0
    max_v_eq_0_1 = np.zeros(hsv[max_v == 0, 1].shape)
    max_v_neq_0_1 = (1 - min_v / (max_v + np.spacing(1)))[max_v != 0]

    hsv = np.zeros(rgb.shape, dtype='float')
    hsv[max_c == min_c, 0] = np.zeros(hsv[max_c == min_c, 0].shape)
    hsv[max_c == 0, 0] = max_c_0_0[max_c == 0]
    hsv[max_c == 1, 0] = max_c_1_0[max_c == 1]
    hsv[max_c == 2, 0] = max_c_2_0[max_c == 2]
    hsv[max_v == 0, 1] = max_v_eq_0_1
    hsv[max_v != 0, 1] = max_v_neq_0_1
    hsv[..., 2] = max_v
    return hsv


def hsv_to_rgb(hsv):
    """ convert HSV to RGB color space
    :param hsv: np.ndarray
    :return: np.ndarray
    """
    hi = np.floor(hsv[..., 0] / 60.0) % 6
    hi = hi.astype('uint8')
    v = hsv[..., 2].astype('float')
    f = (hsv[..., 0] / 60.0) - hi
    p = v * (1.0 - hsv[..., 1])
    q = v * (1.0 - (f * hsv[..., 1]))
    t = v * (1.0 - ((1.0 - f) * hsv[..., 1]))

    rgb = np.zeros(hsv.shape)
    rgb[hi == 0, :] = np.dstack((v, t, p))[hi == 0, :]
    rgb[hi == 1, :] = np.dstack((q, v, p))[hi == 1, :]
    rgb[hi == 2, :] = np.dstack((p, v, t))[hi == 2, :]
    rgb[hi == 3, :] = np.dstack((p, q, v))[hi == 3, :]
    rgb[hi == 4, :] = np.dstack((t, p, v))[hi == 4, :]
    rgb[hi == 5, :] = np.dstack((v, p, q))[hi == 5, :]
    return rgb * RGB_MAX_VALUE

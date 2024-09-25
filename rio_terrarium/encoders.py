from __future__ import division
import numpy as np


def data_to_rgb(data):
    """
    Given an arbitrary (rows x cols) ndarray,
    encode the data into uint8 RGB from an arbitrary
    base and interval

    Parameters
    -----------
    data: ndarray
        (rows x cols) ndarray of data to encode

    Returns
    --------
    ndarray: rgb data
        a uint8 (3 x rows x cols) ndarray with the
        data encoded
    """
    data = data.astype(np.float64)

    rows, cols = data.shape

    datarange = data.max() - data.min()

    if _range_check(datarange):
        raise ValueError("Data of {} larger than 256 ** 3".format(datarange))

    rgb = np.zeros((3, rows, cols), dtype=np.uint8)

    data += 32768
    rgb[0] = np.floor(data /256)
    rgb[1] = np.floor(data % 256)
    rgb[2] = np.floor((data - np.floor(data)) * 256)

    return rgb

def _decode(rgb):
    """
    Given a uint8 (3 x rows x cols) ndarray,
    decode the data into an arbitrary base and interval

    Parameters
    -----------
    rgb: ndarray
        uint8 (3 x rows x cols) ndarray of data to decode

    Returns
    --------
    ndarray: data
        a (rows x cols) ndarray with the data decoded
    """
    rows, cols = rgb.shape[1:]

    data = np.zeros((rows, cols), dtype=np.float64)

    data += rgb[0] * 256
    data += rgb[1]
    data += rgb[2] / 256

    data -= 32768

    return data

def _range_check(datarange):
    """
    Utility to check if data range is outside of precision for 3 digit base 256
    """
    maxrange = 256 ** 3

    return datarange > maxrange

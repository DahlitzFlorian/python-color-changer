import cv2
import numpy as np


def red_green(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.array([image[i][j][0], image[i][j][2],
                                    image[i][j][1]])

    return image


def green_blue(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.array([image[i][j][1], image[i][j][0],
                                    image[i][j][2]])

    return image

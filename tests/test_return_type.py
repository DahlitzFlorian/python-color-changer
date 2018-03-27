from app import red_green, green_blue, blue_red
import numpy as np


def test_return_red_green():
    assert type(red_green(np.ndarray((360, 680, 3)))) == type(np.ndarray((100, 100, 3)))


def test_return_green_blue():
    assert type(green_blue(np.ndarray((360, 680, 3)))) == type(np.ndarray((100, 100, 3)))


def test_return_blue_red():
    assert type(blue_red(np.ndarray((360, 680, 3)))) == type(np.ndarray((100, 100, 3)))

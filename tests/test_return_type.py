from colorchanger.app import red_green, green_blue, blue_red
import numpy as np


def test_return_red_green():
    assert isinstance(red_green(np.ndarray((360, 680, 3))), np.ndarray)


def test_return_green_blue():
    assert isinstance(green_blue(np.ndarray((360, 680, 3))), np.ndarray)


def test_return_blue_red():
    assert isinstance(blue_red(np.ndarray((360, 680, 3))), np.ndarray)

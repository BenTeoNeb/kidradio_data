# -*- coding: utf-8 -*-

import pytest
from kidradio_data.skeleton import fib

__author__ = "Benjamin Farcy"
__copyright__ = "Benjamin Farcy"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

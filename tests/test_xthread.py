import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from memwin.xthread import XThread
import pytest

hwnd = 853298

def test_get_pid():
    xt = XThread(hwnd)
    pid = xt.get_pid()
    assert pid == 7700

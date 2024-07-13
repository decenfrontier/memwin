import pytest
from memwin.xmemory import XMemory

def test_read_int():
    value = XMemory(hwnd=329884).read_int(0x004000FC)
    print(value)
    assert value == 0x00006000
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from memwin.xmemory import XMemory


def test_read_int():
    value = XMemory(hwnd=329884).read_int(0x004000FC)
    print(value)
    assert value == 0x00006000
    
def test_read_string():
    value = XMemory(hwnd=329884).read_string(0x77070050)
    print(f"str value:", value)
    print(f"type of value:", type(value))
    assert value.startswith("is program cannot be run in DOS mode")
    
    
def test_get_module_func_addr():
    xm = XMemory(hwnd=329884)
    base_thread_init_thunk_address = xm.get_module_func_addr("kernel32.dll", "BaseThreadInitThunk")
    print(f"base_thread_init_thunk_address: {hex(base_thread_init_thunk_address)}")
    assert base_thread_init_thunk_address == 0x75fa7b90
    
def test_get_addr_from_expr():
    xm = XMemory(hwnd=329884)
    value = xm.get_value_from_addr_expr("0xDFF7C-0xA30+0x1F8+0x88+0xC+0x78+0x52C")
    print(f"value: {value}")
    assert value == 5472
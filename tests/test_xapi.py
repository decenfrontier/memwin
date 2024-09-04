
from ctypes import wintypes
import ctypes
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memwin.xapi import XWinAPI

user32 = ctypes.WinDLL('user32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)


def test_get_module_file_name():
    MAX_PATH = 260
    path_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    res = XWinAPI.GetModuleFileName(
        None,
        path_buffer,
        MAX_PATH
    )
    if res != 0:
        path = path_buffer[:res]
        print(f'path:{path}')  # D:\python38-32\python.exe
    assert res != 0


def test_load_cursor():
    cursor_id = "Idc_ARROW"  # 表示系统默认箭头光标
    cursor_handle = XWinAPI.LoadCursor(None, wintypes.LPCWSTR(cursor_id))
    print(f'cursor_handle: {cursor_handle}')
    assert cursor_handle is not None


def test_load_image():
    IMAGE_CURSOR = 2
    LR_LOADFROMFILE = 0x00000010
    path = os.path.join(os.getcwd(), 'tests', 'search.png')
    print(f'path:{path}')
    hCursor = XWinAPI.LoadImage(
        None,
        path,
        wintypes.UINT(IMAGE_CURSOR),
        0,0,
        wintypes.UINT(LR_LOADFROMFILE),
    )
    print(f"hCursor:{hCursor}")
    if hCursor is None:
        print('last error:', kernel32.GetLastError())
    assert hCursor is not None


def test_set_system_cursor():
    cursor_id = "IDC_ARROW"  # 表示系统默认箭头光标
    cursor_handle = XWinAPI.LoadCursor(None, wintypes.LPCWSTR(cursor_id))
    print(f'cursor_handle: {cursor_handle}')
    res = XWinAPI.SetSystemCursor(cursor_handle, 0)  # 0表示全局光标
    assert res == 1

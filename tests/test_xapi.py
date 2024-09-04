import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from memwin.utils import MAKEINTRESOURCE
from memwin.constants import XWinCon
from memwin.xapi import XWinAPI
from ctypes import wintypes
import ctypes
import pytest


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


def test_get_cursor():
    hCursor = XWinAPI.GetCursor()
    print(f'cursor_handle: {hCursor}')
    assert hCursor is not None


def test_load_image():
    path = os.path.join(os.getcwd(), 'tests', 'search.cur')
    print(f'path:{path}')
    hCursor = XWinAPI.LoadImage(
        None,
        path,
        wintypes.UINT(XWinCon.IMAGE_CURSOR),
        0, 0,
        wintypes.UINT(XWinCon.LR_LOADFROMFILE),
    )
    print(f"hCursor:{hCursor}")
    if hCursor is None:
        print('last error:', kernel32.GetLastError())
    assert hCursor is not None
    # 加载系统游标
    hCursor = XWinAPI.LoadImage(
        None,
        MAKEINTRESOURCE(32512),
        wintypes.UINT(XWinCon.IMAGE_CURSOR),
        0, 0,
        wintypes.UINT(XWinCon.LR_SHARED),
    )
    print(f"hCursor system:{hCursor}")
    assert hCursor is not None


def test_set_system_cursor():
    import time
    time.sleep(5)
    hCursorOld = XWinAPI.GetCursor()
    print(f'hCursorOld:{hCursorOld}')
    path = os.path.join(os.getcwd(), 'tests', 'search.cur')
    hCursor = XWinAPI.LoadImage(
        None,
        path,
        wintypes.UINT(XWinCon.IMAGE_CURSOR),
        0, 0,
        wintypes.UINT(XWinCon.LR_LOADFROMFILE),
    )
    print(f"hCursor:{hCursor}")
    res = XWinAPI.SetSystemCursor(hCursor, XWinCon.OCR_NORMAL)  # 0表示全局光标
    assert res == 1
    # 然后尝试恢复默认光标
    time.sleep(2)
    res = XWinAPI.SetSystemCursor(hCursorOld, XWinCon.OCR_NORMAL)
    assert res == 1

def test_window_from_point():
    hwnd = XWinAPI.WindowFromPoint(wintypes.POINT(150, 160))
    assert hwnd == 920638

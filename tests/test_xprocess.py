import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from memwin.xprocess import XProcess


def test_create_process():
    lpCommandLine = "notepad.exe"
    cwd = ""
    app_path = ""
    pid = XProcess.create_process(lpCommandLine, cwd, app_path)
    print(f"pid: {pid}")
    assert pid != 0
    
def test_get_hwnd_by_pid():
    pid = 26276
    hwnd = XProcess.get_hwnd_by_pid(pid)
    assert hwnd == 727028
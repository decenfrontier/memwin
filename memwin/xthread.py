from memwin.constants import XWinCon
from .structs import *
from .xapi import XWinAPI


class XThread:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd
        self.tid = 0  # 这里的线程指的都是主线程
        self.h_thread = 0
        self.pid = 0
        self.teb_addr = 0

    def __del__(self):
        if self.h_thread:
            kernel32.CloseHandle(self.h_thread)

    def get_tid(self) -> int:
        """
        获取线程ID
        """
        if self.tid:
            return self.tid
        pid = wintypes.DWORD()
        self.tid = XWinAPI.GetWindowThreadProcessId(
            self.hwnd, ctypes.byref(pid))
        self.pid = pid.value
        return self.tid

    def get_pid(self) -> int:
        """
        获取进程ID
        """
        if self.pid:
            return self.pid
        pid = wintypes.DWORD()
        self.tid = XWinAPI.GetWindowThreadProcessId(
            self.hwnd, ctypes.byref(pid))
        self.pid = pid.value
        return self.pid

    def get_h_thread(self) -> int:
        """
        获取线程句柄
        """
        if self.h_thread:
            return self.h_thread
        self.h_thread = kernel32.OpenThread(
            XWinCon.THREAD_ALL_ACCESS, False, self.get_tid())
        return self.h_thread

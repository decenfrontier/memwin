from memwin.constants import XWinCon
from memwin.xapi import XWinAPI
from .structs import *


class XProcess:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd
        self.pid = 0
        self.h_process = 0

    def __del__(self):
        if self.h_process:
            XWinAPI.CloseHandle(self.h_process)
        
    def get_pid(self) -> int:
        """
        获取进程ID
        """
        if self.pid:
            return self.pid
        process_id = wintypes.DWORD()
        user32.GetWindowThreadProcessId(self.hwnd, ctypes.byref(process_id))
        self.pid = process_id.value
        return self.pid
        
    def get_h_process(self) -> int:
        """
        获取进程句柄
        """
        if self.h_process:
            return self.h_process
        self.pid = self.get_pid()
        self.h_process = kernel32.OpenProcess(XWinCon.PROCESS_ALL_ACCESS, False, self.pid)
        return self.h_process

    @staticmethod
    def create_process(cmd_line: str, cwd="", app_path="") -> int:
        """
        创建进程, 返回新进程的PID
        """
        startupinfo = STARTUPINFOA()
        startupinfo.cb = ctypes.sizeof(startupinfo)
        process_info = PROCESS_INFORMATION()
        cwd = cwd.encode('ansi') if cwd else None
        cmd_line = cmd_line.encode('ansi')
        app_path = app_path.encode('ansi') if app_path else None
        res = XWinAPI.CreateProcess(app_path, cmd_line, None, None, False, 0, None, cwd, ctypes.byref(startupinfo), ctypes.byref(process_info))
        if not res:
            return 0
        return int(process_info.dwProcessId)
    
    @staticmethod
    def get_hwnd_by_pid(pid: int) -> int:
        def enum_windows_proc(hwnd, lParam):
            arg = ctypes.cast(lParam, ctypes.POINTER(EnumWindowsArg)).contents
            dwProcessID = ctypes.c_ulong()
            XWinAPI.GetWindowThreadProcessId(hwnd, ctypes.byref(dwProcessID))
            if dwProcessID.value == arg.dwProcessID:
                arg.hwnd = hwnd
                # 找到了返回False, 停止枚举
                return False
            # 没找到，继续找，返回True
            return True
        ewa = EnumWindowsArg()
        ewa.dwProcessID = ctypes.c_ulong(pid)
        ewa.hwnd = None
        XWinAPI.EnumWindows(ENUM_WND_PROC(enum_windows_proc), ctypes.addressof(ewa))
        if ewa.hwnd is None:
            return 0
        return ewa.hwnd

        
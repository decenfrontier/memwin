from memwin.xapi import XWinAPI
from .structs import *


class XProcess:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd
        self.pid = 0
        self.h_process = 0
        
    def get_pid(self) -> int:
        '''
        获取进程ID
        '''
        if self.pid:
            return self.pid
        process_id = wintypes.DWORD()
        user32.GetWindowThreadProcessId(self.hwnd, ctypes.byref(process_id))
        self.pid = process_id.value
        return self.pid
        
    def get_h_process(self) -> int:
        '''
        获取进程句柄
        '''
        if self.h_process:
            return self.h_process
        self.pid = self.get_pid()
        self.h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, self.pid)
        return self.h_process

    @staticmethod
    def create_process(cmd_line: str, cwd: str, app_path="") -> bool:
        """
        创建进程
        """
        startupinfo = STARTUPINFOA()
        startupinfo.cb = ctypes.sizeof(startupinfo)
        process_info = PROCESS_INFORMATION()
        cwd = cwd.encode('ansi') if cwd else None
        cmd_line = cmd_line.encode('ansi')
        app_path = app_path.encode('ansi') if app_path else None
        res = XWinAPI.CreateProcess(app_path, cmd_line, None, None, False, 0, None, cwd, ctypes.byref(startupinfo), ctypes.byref(process_info))
        return res == 1
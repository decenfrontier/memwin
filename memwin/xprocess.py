from .structs import *


class XProcess:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd
        self.pid = 0
        self.h_process = 0
        
    def get_pid(self) -> int:
        # 获取进程ID
        if self.pid:
            return self.pid
        process_id = wintypes.DWORD()
        user32.GetWindowThreadProcessId(self.hwnd, ctypes.byref(process_id))
        self.pid = process_id
        print("pid:", self.pid)
        return self.pid
        
    def get_h_process(self) -> int:
        # 获取进程句柄
        if self.h_process:
            return self.h_process
        self.pid = self.get_pid()
        self.h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, self.pid)
        print("h_process:", self.h_process)
        return self.h_process


    
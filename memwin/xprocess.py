from structs import *


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
        self.pid =user32.GetWindowThreadProcessId(self.hwnd, ctypes.byref(process_id))
        return self.pid
        
    def get_h_process(self) -> int:
        # 获取进程句柄
        if self.h_process:
            return self.h_process
        pid = self.get_pid()
        self.h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return self.h_process


    
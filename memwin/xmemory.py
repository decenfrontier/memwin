from structs import *
from xprocess import XProcess
from xthread import XThread

class XMemory:
    def __init__(self, hwnd: int):
        self.thread = XThread(hwnd)
        self.process = XProcess(hwnd)
        self.teb_addr = 0
    
    def read_int(self, addr: int, offset=0):
        self.h_process = self.process.get_h_process()
        # 读取指定地址的值, 读取4字节, 按int解析
        address = ctypes.c_void_p(addr + offset)
        # 定义缓冲区和读取的字节数
        buffer = ctypes.c_uint32()
        bytes_read = ctypes.c_size_t(0)
        # 读取内存
        if not kernel32.ReadProcessMemory(
            self.h_process,
            address,
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytes_read)
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        return buffer.value
    
    # ----------------------------- 进程相关 ----------------------------
    def get_module_base_addr(self, module_name) -> int:
        # 获取模块基址
        self.h_process = self.process.get_h_process()
        module_handle_array = (ctypes.c_ulong * 1024)()
        needed = ctypes.c_ulong()
        if not psapi.EnumProcessModulesEx(
            self.h_process, ctypes.byref(module_handle_array), ctypes.sizeof(module_handle_array), ctypes.byref(needed), 0x03
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        module_count = needed.value // ctypes.sizeof(ctypes.c_ulong)
        for i in range(module_count):
            h_module = module_handle_array[i]
            module_name_buffer = ctypes.create_unicode_buffer(256)
            if psapi.GetModuleBaseNameW(
                self.h_process, h_module, module_name_buffer, ctypes.sizeof(module_name_buffer) // ctypes.sizeof(ctypes.c_wchar)
            ):
                if module_name_buffer.value.lower() == module_name.lower():
                    return h_module
        raise Exception(f"Module {module_name} not found in process")
    
    def get_module_func_addr(self, module_name, func_name) -> int:
        # 获取模块内的函数地址
        pass
    
    # ----------------------------- 线程相关 -----------------------------
    def get_teb_addr(self) -> int:
        # 获取线程的TEB地址
        if self.teb_addr:
            return self.teb_addr
        tbi = THREAD_BASIC_INFORMATION()
        return_length = wintypes.ULONG(0)
        ThreadBasicInformation = 0
        status = ntdll.NtQueryInformationThread(
            self.get_h_thread(),
            ThreadBasicInformation,
            ctypes.byref(tbi),
            ctypes.sizeof(tbi),
            ctypes.byref(return_length)
        )
        if status != 0:
            raise ctypes.WinError(ctypes.get_last_error())
        self.teb_addr = ctypes.addressof(tbi.TebBaseAddress.contents)
        return self.teb_addr
    
    def get_thread_stack_top_addr(self):
        # 获取线程的栈顶的地址
        self.teb_addr = self.get_teb_addr()
        return self.read_int(self.teb_addr, 0x4)
    
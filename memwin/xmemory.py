from memwin.utils import read_until_terminator
from .structs import *
from .xprocess import XProcess
from .xthread import XThread
from .xapi import XWinAPI

class XMemory:
    def __init__(self, hwnd: int):
        self.thread = XThread(hwnd)
        self.process = XProcess(hwnd)
        self.teb_addr = 0
    
    def read_int(self, addr: int, offset=0):
        '''
        读取指定地址的值, 读取4字节, 按int解析
        '''
        self.h_process = self.process.get_h_process()
        # 定义缓冲区和读取的字节数
        buffer = ctypes.c_uint32()  # 读几字节跟这里有关
        bytes_read = ctypes.c_size_t()
        # 读取内存
        address = ctypes.c_void_p(addr + offset)
        if not kernel32.ReadProcessMemory(
            self.h_process,
            address,
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytes_read)
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        return buffer.value
    
    def read_short(self, addr: int, offset=0):
        '''
        读取指定地址的值, 读取2字节, 按int解析
        '''
        self.h_process = self.process.get_h_process()
        # 定义缓冲区和读取的字节数
        buffer = ctypes.c_uint16()  # 读几字节跟这里有关
        bytes_read = ctypes.c_size_t()
        # 读取内存
        address = ctypes.c_void_p(addr + offset)
        if not kernel32.ReadProcessMemory(
            self.h_process,
            address,
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytes_read)
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        return buffer.value
    
    def read_string(self, addr: int, size=256, encoding='ascii'):
        '''
        读取指定地址的值, 默认读取256字节, 按ascii解析
        '''
        self.h_process = self.process.get_h_process()
        # 定义缓冲区和读取的字节数
        buffer = ctypes.create_string_buffer(size)  # 读几字节跟这里有关
        bytes_read = ctypes.c_size_t(0)
        # 读取内存
        address = ctypes.c_void_p(addr)
        if not kernel32.ReadProcessMemory(
            self.h_process,
            address,
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytes_read)
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        return read_until_terminator(buffer.raw).decode(encoding=encoding, errors="ignore")
    
    def get_value_from_addr_expr(self, expr: str):
        '''
        解析地址表达式, 得到该地址对应的值
        表达式形如: 0xDFF7C-0xA30+0x1F8+0x88+0xC+0x78+0x52C
        '''
        arr = expr.split('+')
        addr = 0
        # i = 0
        for offset in arr:
            # print(f"----------{i} start----------")
            if '-' in offset:
                base, delta = offset.split('-')
                base = int(base, 16)
                delta = int(delta, 16)
                # print(f"base:{hex(base)}, delta:{hex(delta)}")
                offset = hex(base - delta)
            # print(f"offset: {offset}")
            this_addr = addr + int(offset, 16)
            # print(f"this_addr: {hex(this_addr)}")
            addr = self.read_int(this_addr)
            # print(f"addr: {hex(addr)}")
            # print(f"----------{i} end----------")
            # print()
            # i += 1
        value = addr
        return value
                
    # ----------------------------- 进程相关 ----------------------------
    def get_module_addr(self, module_name) -> int:
        '''
        获取模块的首地址
        '''
        self.h_process = self.process.get_h_process()
        module_addr_array = (ctypes.c_ulong * 1024)()
        needed = ctypes.c_ulong()
        if not psapi.EnumProcessModulesEx(
            self.h_process, ctypes.byref(module_addr_array), ctypes.sizeof(module_addr_array), ctypes.byref(needed), 0x03
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        module_count = needed.value // ctypes.sizeof(ctypes.c_ulong)
        for i in range(module_count):
            module_addr = module_addr_array[i]
            module_name_buffer = ctypes.create_unicode_buffer(256)
            if psapi.GetModuleBaseNameW(
                self.h_process, module_addr, module_name_buffer, ctypes.sizeof(module_name_buffer) // ctypes.sizeof(ctypes.c_wchar)
            ):
                if module_name_buffer.value.lower() == module_name.lower():
                    return module_addr
        raise Exception(f"Module {module_name} not found in process")
    
    def get_module_pe_addr(self, module_name) -> int:
        '''
        获取模块的PE结构地址
        '''
        module_addr = self.get_module_addr(module_name)
        pe_addr = module_addr + self.read_int(module_addr, 0x3c)
        return pe_addr
    
    def get_module_func_addr(self, module_name, func_name) -> int:
        '''
        获取模块内的函数地址
        '''
        # 先从PE结构中获取可选PE头的大小
        module_addr = self.get_module_addr(module_name)
        # print(f"module_addr: {hex(module_addr)}")
        pe_addr = self.get_module_pe_addr(module_name)
        # print(f"pe_addr: {hex(pe_addr)}")
        option_pe_header_size = self.read_short(pe_addr, 4+16)
        # print(f"option_pe_header_size: {hex(option_pe_header_size)}")
        # 定位到数据目录表的地址(从可选头最后128的字节开始)
        data_directory_addr = pe_addr + 4 + 20 + option_pe_header_size - 128
        # print(f"data_directory_addr: {hex(data_directory_addr)}")
        # 数据目录表的第1项是导出表的地址
        export_table_rva = self.read_int(data_directory_addr)
        export_table_addr = module_addr + export_table_rva
        # print(f"export_table_addr: {hex(export_table_addr)}")
        # 获取 函数地址表地址, 函数名称表地址, 函数序列表地址
        func_addr_table_rva = self.read_int(export_table_addr, 28)
        func_name_table_rva = self.read_int(export_table_addr, 32)
        func_ordinal_table_rva = self.read_int(export_table_addr, 36)
        func_addr_table_addr = module_addr + func_addr_table_rva
        func_name_table_addr = module_addr + func_name_table_rva
        func_ordinal_table_addr = module_addr + func_ordinal_table_rva
        # 遍历 函数名称表, 找到函数名对应的序号, 再根据序号获取函数地址
        func_count = self.read_short(export_table_addr, 24)
        for i in range(func_count):
            func_name_rva = self.read_int(func_name_table_addr, i*4)
            local_func_name = self.read_string(module_addr + func_name_rva)
            if local_func_name != func_name:
                continue
            func_ordinal = self.read_short(func_ordinal_table_addr, i*2)
            func_addr_rva = self.read_int(func_addr_table_addr, func_ordinal*4)
            func_addr = module_addr + func_addr_rva
            return func_addr
        return 0
    
    def inject_dll(self, dll_path: str):
        # 获取进程句柄
        self.h_process = self.process.get_h_process()
        # 在目标进程中分配内存, 存放dll路径
        path_bytes = str(dll_path).encode()
        path_size = len(path_bytes) + 1
        alloc_addr = XWinAPI.VirtualAllocEx(self.h_process, 0, path_size, MEM_COMMIT, PAGE_READWRITE)
        if not alloc_addr:
            print("VirtualAllocEx failed")
            return False
        # 写入dll路径到目标进程内存
        XWinAPI.WriteProcessMemory(self.h_process, alloc_addr, path_bytes, path_size, None)
        # 创建远程线程, 调用 LoadLibraryA
        load_lib_addr = self.get_module_func_addr("kernel32.dll", "LoadLibraryA")
        sa = SECURITY_ATTRIBUTES()
        sa.nLength = ctypes.sizeof(sa)
        sa.lpSecurityDescriptor = None
        sa.bInheritHandle = True
        lpThreadAttributes = LPSECURITY_ATTRIBUTES(sa)
        h_thread = XWinAPI.CreateRemoteThread(self.h_process, lpThreadAttributes, 0, load_lib_addr, alloc_addr, 0, None)
        if not h_thread:
            print("CreateRemoteThread failed")
            return False
        # 等待线程结束
        XWinAPI.WaitForSingleObject(h_thread, -1)
        # 释放内存
        XWinAPI.CloseHandle(h_thread)
        XWinAPI.VirtualFreeEx(self.h_process, alloc_addr, 0, MEM_RELEASE)
        return True
    
    # ----------------------------- 线程相关 -----------------------------
    def get_teb_addr(self) -> int:
        '''
        获取线程的TEB地址
        '''
        if self.teb_addr:
            return self.teb_addr
        tbi = THREAD_BASIC_INFORMATION()
        return_length = wintypes.ULONG(0)
        ThreadBasicInformation = 0
        status = ntdll.NtQueryInformationThread(
            self.thread.get_h_thread(),
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
        '''
        获取线程的栈顶的地址
        '''
        self.teb_addr = self.get_teb_addr()
        return self.read_int(self.teb_addr, 0x4)
    

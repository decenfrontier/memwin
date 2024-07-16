from .structs import *

class XWinAPI:
    @staticmethod
    @api_annotater(kernel32.CloseHandle)
    def CloseHandle(handle: wintypes.HANDLE) -> wintypes.BOOL:
        pass
    
    @staticmethod
    @api_annotater(kernel32.OpenProcess)
    def OpenProcess(
        access: wintypes.DWORD, inherit_handle: wintypes.BOOL, process_id: wintypes.DWORD
    ) -> wintypes.HANDLE:
        pass

    @staticmethod
    @api_annotater(kernel32.ReadProcessMemory)
    def ReadProcessMemory(
        handle: wintypes.HANDLE,
        base_address: wintypes.LPVOID,
        buffer: wintypes.LPCVOID,
        size: ctypes.c_size_t,
        size_ptr: ctypes.POINTER(ctypes.c_size_t),
    ) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(kernel32.WriteProcessMemory)
    def WriteProcessMemory(
        handle: wintypes.HANDLE,
        base_address: wintypes.LPVOID,
        buffer: wintypes.LPCVOID,
        size: ctypes.c_size_t,
        size_ptr: ctypes.POINTER(ctypes.c_size_t),
    ) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(kernel32.VirtualAllocEx)
    def VirtualAllocEx(
        handle: wintypes.HANDLE,
        address: wintypes.LPVOID,
        size: ctypes.c_size_t,
        allocation_type: wintypes.DWORD,
        protect: wintypes.DWORD,
    ) -> wintypes.LPVOID:
        pass

    @staticmethod
    @api_annotater(kernel32.VirtualFreeEx)
    def VirtualFreeEx(
        handle: wintypes.HANDLE,
        address: wintypes.LPVOID,
        size: ctypes.c_size_t,
        free_type: wintypes.DWORD,
    ) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(kernel32.WaitForSingleObject)
    def WaitForSingleObject(
        handle: wintypes.HANDLE, time_milliseconds: wintypes.DWORD
    ) -> wintypes.DWORD:
        pass

    @staticmethod
    @api_annotater(kernel32.TerminateProcess)
    def TerminateProcess(handle: wintypes.HANDLE, exit_code: wintypes.UINT) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(kernel32.CreateRemoteThread)
    def CreateRemoteThread(
        handle: wintypes.HANDLE,
        thread_attributes: ctypes.POINTER(LPSECURITY_ATTRIBUTES),
        stack_size: ctypes.c_size_t,
        start_address: wintypes.LPVOID,
        start_parameter: wintypes.LPVOID,
        flags: wintypes.DWORD,
        thread_id: wintypes.LPDWORD,
    ) -> wintypes.HANDLE:
        pass

    @staticmethod
    @api_annotater(kernel32.GetModuleHandleA)
    def GetModuleHandle(module_name: wintypes.LPCSTR) -> wintypes.HMODULE:
        pass

    @staticmethod
    @api_annotater(kernel32.GetProcAddress)
    def GetProcAddress(
        module_handle: wintypes.HMODULE, proc_name: wintypes.LPCSTR
    ) -> wintypes.LPVOID:
        pass

    @staticmethod
    @api_annotater(kernel32.VirtualProtectEx)
    def VirtualProtectEx(
        handle: wintypes.HANDLE,
        address: wintypes.LPVOID,
        size: ctypes.c_size_t,
        flags: wintypes.DWORD,
        old_protect: wintypes.PDWORD,
    ) -> wintypes.BOOL:
        pass


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
        thread_attributes: LPSECURITY_ATTRIBUTES,
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

    @staticmethod
    @api_annotater(kernel32.CreateProcessA)
    def CreateProcess(
        lpApplicationName: wintypes.LPCSTR,
        lpCommandLine: wintypes.LPSTR,
        lpProcessAttributes: LPSECURITY_ATTRIBUTES,
        lpThreadAttributes: LPSECURITY_ATTRIBUTES,
        bInheritHandles: wintypes.BOOL,
        dwCreationFlags: wintypes.DWORD,
        lpEnvironment: wintypes.LPVOID,
        lpCurrentDirectory: wintypes.LPCSTR,
        lpStartupInfo: LPSTARTUPINFOA,
        lpProcessInformation: LPPROCESS_INFORMATION,
    ) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(user32.EnumWindows)
    def EnumWindows(
        enum_func: ENUM_WND_PROC,
        param: wintypes.LPARAM,
    ) -> wintypes.BOOL:
        pass

    @staticmethod
    @api_annotater(user32.GetWindowThreadProcessId)
    def GetWindowThreadProcessId(
        hwnd: wintypes.HWND,
        pid: wintypes.LPDWORD
    ) -> wintypes.DWORD:
        """
        本API用于根据窗口句柄获取进程ID和线程ID
        - wintypes.HWND hwnd: [in]窗口句柄
        - wintypes.LPDWORD process_id: [out]返回的进程ID
        - 返回值: 0表示失败, 非0表示成功, 值为线程ID
        """

    @staticmethod
    @api_annotater(kernel32.GetModuleFileNameW)
    def GetModuleFileName(
        hModule: wintypes.HMODULE,
        lpFileName: wintypes.LPWSTR,
        nSize: wintypes.DWORD,
    ) -> wintypes.DWORD:
        """
        本API用于获取模块的完整路径
        - wintypes.HMODULE hModule: [in]模块句柄, NULL则为本进程
        - wintypes.LPSTR lpFileName: [out]返回的模块的完整路径
        - wintypes.DWORD nSize: [in]lpFilename 缓冲区的大小
        函数成功返回复制到缓冲区的字符长度, 失败返回0
        """
        pass

    @staticmethod
    @api_annotater(user32.GetCursor)
    def GetCursor(
    ) -> wintypes.HANDLE:
        """
        本API返回当前鼠标光标的句柄
        """

    @staticmethod
    @api_annotater(user32.CopyImage)
    def CopyImage(
        hImage: wintypes.HANDLE,
        type: wintypes.UINT,
        cx: ctypes.c_int,
        cy: ctypes.c_int,
        flags: wintypes.UINT,
    ) -> wintypes.HANDLE:
        """
        本API拷贝一份Cursor句柄, 返回一个新句柄
        - wintypes.HANDLE hImage: [in]要拷贝的句柄
        - wintypes.UINT type: [in]要拷贝的资源类型, IMAGE_CURSOR=2
        - wintypes.c_int cx: [in]新图片的宽度, 0表示与原始 hImage 相同
        - wintypes.c_int cy: [in]新图片的高度, 0表示与原始 hImage 相同
        - wintypes.UINT flags: [in]拷贝标志, LR_DEFAULTCOLOR=0
        """

    @staticmethod
    @api_annotater(user32.LoadImageW)
    def LoadImage(
        hInst: wintypes.HINSTANCE,
        name: wintypes.LPCWSTR,
        type: wintypes.UINT,
        cx: ctypes.c_int,
        cy: ctypes.c_int,
        fuLoad: wintypes.UINT
    ) -> wintypes.HANDLE:
        """
        本API用于加载图片, 返回一个句柄, 可以被用来设置为鼠标指针
        - HINSTANCE hInst: 实例句柄，NULL 表示从当前进程加载
        - LPCSTR    name: 图片文件的路径, 注意文件类型要是*.cur
        - UINT      type: 图像的类型 IMAGE_CURSOR=2, 加载为游标
        - int       cx: 指定宽度，0表示默认大小
        - int       cy: 指定高度，0表示默认大小
        - UINT      fuLoad: 加载标志 LR_LOADFROMFILE
        """

    @staticmethod
    @api_annotater(user32.SetSystemCursor)
    def SetSystemCursor(
        hCur: wintypes.HANDLE,
        cursorId: wintypes.DWORD
    ) -> wintypes.BOOL:
        """
        本API用于设置系统鼠标指针
        - hCur: 要设置的鼠标指针的句柄, 
        - cursorId: 替换指针的哪种形态, 一般都用普通选择OCR_NORMAL=32512
        """

    @staticmethod
    @api_annotater(user32.WindowFromPoint)
    def WindowFromPoint(
        pt: wintypes.POINT
    ) -> wintypes.HWND:
        """
        本API用于获取鼠标指向的窗口句柄
        - pt: 鼠标坐标
        """

    @staticmethod
    @api_annotater(user32.GetWindowTextW)
    def GetWindowText(
        hwnd: wintypes.HWND,
        lpString: wintypes.LPWSTR,
        nMaxCount: ctypes.c_int,
    ) -> int:
        """
        本API用于获取窗口句柄对应的窗口标题
        - hwnd: 窗口句柄
        - lpString: [out]窗口标题
        - nMaxCount: 窗口标题最大长度
        如果函数成功，则返回值为复制的字符串的长度（以字符为单位），不包括终止 null 字符。 
        如果窗口没有标题栏或文本，如果标题栏为空，或者窗口或控件句柄无效，则返回值为零。
        """

    @staticmethod
    @api_annotater(user32.GetClassNameW)
    def GetClassName(
        hwnd: wintypes.HWND,
        lpClassName: wintypes.LPWSTR,
        nMaxCount: ctypes.c_int,
    ) -> int:
        """
        本API用于获取窗口句柄对应的窗口类名
        - hwnd: 窗口句柄
        - lpClassName: [out]窗口类名
        - nMaxCount: 窗口类名最大长度
        如果函数成功，则返回值为复制的字符串的长度（以字符为单位），不包括终止 null 字符。 
        如果窗口没有标题栏或文本，如果标题栏为空，或者窗口或控件句柄无效，则返回值为零。
        """
<p align="center"><a href="" target="_blank" rel="noopener noreferrer"><img width="180" src="https://files.logomakr.com/8JOSeS-LogoMakr.png" alt="logo"></a></p>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-%3E%3D%203.8-blue" alt="Python >= 3.8">
  </a>
  <a href="https://github.com/decenfrontier/memwin/stargazers">
    <img src="https://img.shields.io/github/stars/decenfrontier/memwin?logo=ReverbNation&logoColor=rgba(255,255,255,.6)" alt="GitHub stars">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  </a>
  <a href="https://en.wikipedia.org/wiki/Win32">
    <img src="https://img.shields.io/badge/platform-win32-blue" alt="win32">
  </a>
</p>


<h2 align="center">memwin</h2>

# 介绍
一个python操作windows的 进程 线程 内存读写 HOOK的库, 暂仅支持32位进程  

为什么需要创建这个库?   
因为Python尽管已经有pywin32, psutil等库可以操作windows的进程线程内存,   
但这些库都只是操作windows的原生api, 自己用python写的话效率低下, 要定义很多结构体才能用,   
如果封装好, 就能更方便地通过hwnd来操作任意窗口进程的内存  

出于效率考虑, 大家只需要传入hwnd, 就可以操作任意窗口的内存,   
已经查过的ID, 句柄信息会存储在实例对象中,   
只要查过一次, 下次就能直接获取, 无需再次查询, 大大提高CPU的执行效率
但在使用过程中要注意, 一定要调用方法来获取对象的属性, 不要直接读属性


欢迎各位大佬, 动动手点个Star, 共同完善这个库~


# 安装
```sh
pip install memwin
```

# 快速开始
下面演示三个子模块的常用操作, 其它的方法在左侧GitHub中的开源代码
## 进程操作示例
```python
from memwin.xprocess import XProcess

hwnd=329884
xp = XProcess(hwnd)
h_process = xp.get_h_process()
print(f"h_process: {h_process}")
```

## 线程操作示例
```python
from memwin.xthread import XThread

hwnd=329884
xt = XThread(hwnd)
h_thread = xt.get_h_thread()
print(f"h_thread: {h_thread}")
```

## 内存读写操作示例
```python
from memwin.xmemory import XMemory

hwnd=329884
xm = XMemory(hwnd)
teb_addr = xm.get_teb_addr()
print(f"TEB地址: {teb_addr}")
stack_top_addr = xm.read_int(teb_addr, 0x4)
print(f"栈顶指针: {stack_top_addr}")
```


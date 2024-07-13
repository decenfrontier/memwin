# memwin介绍
一个python操作windows的 进程 线程 内存读写 HOOK的库, 暂时只支持32位进程, 64位进程未测试.
为什么需要创建这个库? 因为python尽管已经有win32process, win32api, pywin32等库可以操作windows的进程线程内存, 但这些库都只是操作windows的原生api, 自己用python写的话效率低下, 要多定义很多结构体才能用, 如果封装好, 就能更方便地通过hwnd来操作任意窗口进程的内存

# 安装
```sh
pip install memwin
```

# 文档
## 进程操作示例
```python

```

## 线程操作示例
```python

```

## 内存读写操作示例
```python

```

# 单元测试
```sh
pip install pytest
pytest -s
```
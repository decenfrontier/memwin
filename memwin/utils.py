import functools
import itertools
import ctypes
from typing import *

T = TypeVar("T")

def read_until_terminator(data: bytes, terminator: int = 0) -> bytes:
    return bytes(itertools.takewhile(lambda char: char != terminator, data))

def api_annotater(func_ptr: Any) -> Callable[
        [Callable[..., T]], Callable[..., T]
    ]:
    def wrap(function: Callable[..., T]) -> Callable[..., T]:
        annotations = get_type_hints(function)
        return_type = annotations.pop("return", None)
        if return_type:
            func_ptr.restype = return_type
        argument_types = list(annotations.values())
        if argument_types:
            func_ptr.argtypes = argument_types

        @functools.wraps(function)
        def handle_call(*args) -> T:
            return func_ptr(*args)
        return handle_call
    return wrap


def MAKEINTRESOURCE(id: int):
    return ctypes.cast(id, ctypes.wintypes.LPCWSTR)

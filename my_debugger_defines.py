#coding:utf8

from ctypes import *
from _subprocess import CREATE_NEW_CONSOLE

# Microsoftの型とctypesとの対応を定義して明快にする
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p
WCHAR = c_wchar_p

# 定数
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# 関数CreateProcess()のための構造体
class STARTUPINFO (Structure):
    _fields_ = [
            ("cb",  DWORD),
            ("lpReserved",  LPTSTR),
            ("lpDesktop",   LPTSTR),
            ("lpTiltle",    LPTSTR),
            ("dwX", DWORD),
            ("dwY", DWORD),
            ("dwXSize", DWORD),
            ("dwYSize", DWORD),
            ("dwXCountChars",   DWORD),
            ("dwYCountChars",   DWORD),
            ("dwFileAttribute", DWORD),
            ("dwFlag",  DWORD),
            ("wShowWindw", WORD),
            ("cbReserved2", WORD),
            ("lpReserved2", LPBYTE),
            ("hStdInput",   HANDLE),
            ("hStdOutput",  HANDLE),
            ("hStdError",   HANDLE),
        ]

class PROCESS_INFOMATION(Structure):
    _fields_ = [
            ("hProces", HANDLE),
            ("hThread",  HANDLE),
            ("dwProcessId", DWORD),
            ("dwThreadId",  DWORD),
        ]



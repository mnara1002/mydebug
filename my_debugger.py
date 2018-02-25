#coding:utf8
from ctypes import *
from my_debugger_defines import *
from _ctypes import byref
from __builtin__ import int

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        """
        dwCreateFlagsによってプロセスをどのように生成するか決まる。
        例として電卓のGUIを見る場合、以下のようにパラメータを設定する。
        Creation_flags = CREATE_NEW_CONSOLE
        """
        Creation_flags = DEBUG_PROCESS

        #構造体をインスタンス化する
        startupinfo = STARTUPINFO()
        process_infomation = PROCESS_INFOMATION()

        """
        次のオプションを指定することで、起動されたプロセスは別ウィンドウで表示される。
        """
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        #STARTUPINFO構造体のサイズを表す変数cbを初期化する。
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    Creation_flags,
                                                    None,
                                                    None,
                                                    byref(startupinfo),
                                                    byref(process_infomation)
                                                    ):
            print "[*] We have successfully launched the process!"
            print "[*] PID: %d"  % process_infomation.dwProcessId

        else:
            print "[*] Error: 0x%08x." % kernel32.GetLastError()

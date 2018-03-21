#coding:utf8
from ctypes import *
from my_debugger_defines import *


kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_process = None #対象プロセスのハンドルを格納する
        self.pid = None #対象プロセスのPIDを格納する
        self.debugger_active = False #デバッガの状態を示す


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

            #将来の利用に備え、プロセスのハンドルを取得したら保存する
            self.h_process = self.open_process(process_infomation.dwProcessId)

        else:
            print "[*] Error: 0x%08x." % kernel32.GetLastError()

    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
        return h_process

    def attach(self,pid):
        self.h_process = self.open_process(pid)

        #プロセスにアタッチしてみる。失敗した際は呼び出し元に戻る
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)

        else:
            print "[*] Unable to attach to the process."

    def run(self):
        #デバッグ対象プロセスからのデバッグイベントを待機する
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE


        if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
            #まだイベントハンドラは実装していないので、プロセスを再開させるだけに留まる。
            raw_input("Press a key to continue...")
            self.debugger_active = False
            kernel32.ContinueDebugEvent(
                debug_event.dwProcessId,
                debug_event.dwThreadId,
                continue_status
                )

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print "[*] Finished debugging. Exiting..."
            return True
        else:
            print "There was an error"
            return False

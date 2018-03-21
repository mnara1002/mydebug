#coding:utf8
import my_debugger

if __name__ == '__main__':
    debugger = my_debugger.debugger()

    pid = raw_input("Enter the PID of the process to attach to: ")

    debugger.attach(int(pid))
    debugger.run()
    debugger.detach()
    #debugger.load("C:\\Windows\\System32\\calc.exe")


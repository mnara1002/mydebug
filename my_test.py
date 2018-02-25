#coding:utf8
from ctypes import *
import my_debugger

if __name__ == '__main__':
    debugger = my_debugger.debugger()
    debugger.load("C:\\Windows\\System32\\calc.exe")


# -*- coding: utf-8 -*-
from timerloop import TimeList
from taskrunutils import runTaskFile
import dateUtils as du

def updateWork():
    if not du.isWorkDay():
        return
    runTaskFile("updateAndMakeConfigTask2.json")
    
def myWork():
    timeL=TimeList()
    #timeL.addTask("15:09:50",None,"hihi")
    timeL.addTask("16:00:50",updateWork,"updateWork")
    timeL.beginRun();

myWork()
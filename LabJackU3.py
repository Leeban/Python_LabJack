# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:40:53 2022

@author: LeebanRoy
"""
import time
import u3
import sys
import traceback


def Connect():
    Dev = None
    error = ''
    try:
        Dev = u3.U3()   # U3 class will try to automatically open the first found U3.
                        # This is good if you only have one U3 connected.
                        
        Dev.getCalibrationData()
        
        '''Set the first four (0-3) to analog (15 = 1111 binary) and the rest to digital'''
        Dev.configIO(FIOAnalog = 15)
        
        '''Set FIOx to digital Output = 1 and Input = 0'''
        Dev.getFeedback(u3.BitDirWrite(4, 1))
        Dev.getFeedback(u3.BitDirWrite(5, 1))
        Dev.getFeedback(u3.BitDirWrite(6, 1))
        Dev.getFeedback(u3.BitDirWrite(7, 1))
        
    except BaseException:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()
    
        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)
    
        # Format stacktrace
        stack_trace = list()
    
        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
    
        # print("Exception type : %s " % ex_type.__name__)
        # print("Exception message : %s" %ex_value)
                
        # print(e)
        error = str(ex_value)    
    return Dev, error
    
def Read_Analog(Dev, ANIX_PortNo_int): # Choose No from 0 to 3 since "d.configIO(FIOAnalog = 15)"
    error = ''
    ANIX_Value = float()
    try:
        """Read from AIN0 in one function"""
        ANIX_Value = Dev.getAIN(ANIX_PortNo_int)
        
    except BaseException:
        
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        # print("Exception type : %s " % ex_type.__name__)
        # print("Exception message : %s" %ex_value)
                
        # print(e)
        error = str(ex_value)
        
    return ANIX_Value, error

def SetBit_On(Dev, FIO_PortNo_int):
    error = ''
    FIOx_Bit_State = int()
    try:
        '''Set FIO4 output Low = 0'''
        Dev.getFeedback(u3.BitStateWrite(FIO_PortNo_int, 0))
        '''Read The Status of selected I/O Bit i.e. On/Off'''
        FIOx_Bit_State = Dev.getFeedback(u3.BitStateRead(IONumber = FIO_PortNo_int))[0]
        
    except BaseException:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        # print("Exception type : %s " % ex_type.__name__)
        # print("Exception message : %s" %ex_value)
                
        # print(e)
        error = str(ex_value)
    
    return FIOx_Bit_State, error

def SetBit_Off(Dev, FIO_PortNo_int):
    error = ''
    FIOx_Bit_State = int()
    try:
        '''Set FIO4 output High = 1'''
        Dev.getFeedback(u3.BitStateWrite(FIO_PortNo_int, 1))
        '''Read The Status of selected I/O Bit i.e. On/Off'''
        FIOx_Bit_State = Dev.getFeedback(u3.BitStateRead(IONumber = FIO_PortNo_int))[0]
        
    except BaseException:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        # print("Exception type : %s " % ex_type.__name__)
        # print("Exception message : %s" %ex_value)
                
        # print(e)
        error = str(ex_value)

    return FIOx_Bit_State, error

def Disconnect(Dev):
    error = ''
    try:
        '''Set FIO4 output High = 1'''
        Dev.getFeedback(u3.BitStateWrite(4, 1))
        Dev.getFeedback(u3.BitStateWrite(5, 1))
        Dev.getFeedback(u3.BitStateWrite(6, 1))
        Dev.getFeedback(u3.BitStateWrite(7, 1))
        
    except BaseException:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        # print("Exception type : %s " % ex_type.__name__)
        # print("Exception message : %s" %ex_value)
                
        # print(e)
        error = str(ex_value)

    Dev.close()
    return error
    
    

""" ------------------- Test_code_Here -------------------------- """

# Device , Error = Connect()
# print("------------------------------------------")
# print("Error : ", Error)
# print("------------------------------------------\n")
# time.sleep(0.5)

# if Device != None:
#     Serial = Device.configU3()['SerialNumber'] 
#     Name =  Device.configU3()['DeviceName']
#     print("Device Name : ", Name, "\nSerial No : ", Serial)

#     # Analog_PortNo_int = 0 # """Port no to read"""
#     # Analog_Reading, Error = Read_Analog(Device, Analog_PortNo_int)
#     # print("Analog Reading = ", Analog_Reading)
#     # print("------------------------------------------")
#     # print("Error : ", Error)
#     # print("------------------------------------------\n")
    
#     time.sleep(0.5)
    
#     Digital_port = 6
    
#     Digi_Port_Status, Erorr = SetBit_On(Device, Digital_port)
#     print("Port Status = ", Digi_Port_Status)
#     print("------------------------------------------")
#     print("Error : ", Error)
#     print("------------------------------------------\n")
    
    # time.sleep(2)
    
    # Digi_Port_Status, Erorr = SetBit_Off(Device, Digital_port)
    # print("Port Status = ", Digi_Port_Status)
    # print("------------------------------------------")
    # print("Error : ", Error)
    # print("------------------------------------------\n")
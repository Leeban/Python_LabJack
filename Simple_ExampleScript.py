#Test Script for LabJack usage

"""
install dependend module "pip install LabJackPython" for using accesing u3 and
install LabJack driver files provided by manufacturer "https://labjack.com/support/software/installers/ud/archive/ud-setup-basic" for windows
"""

import u3

d = u3.U3() # U3 class will try to automatically open the first found U3.
            # This is good if you only have one U3 connected.

#Get the LabJacks device Configuration. This only needs to be performed once after opening your device.
#The calibration data will be used by functions that convert binary data to voltage/temperature and vice versa
d.getCalibrationData()

'''Set the first four (0-3) ports to analog (15 = 1111 binary) and the rest to digital'''
d.configIO(FIOAnalog = 15)

"""Read from AIN0 in one function"""
ainValue = d.getAIN(0)
print(ainValue) 

'''Set FIO4 to digital Output = 1 and Input = 0'''
d.getFeedback(u3.BitDirWrite(4, 1))


'''Set FIO4 output Low = 0'''
d.getFeedback(u3.BitStateWrite(4, 0))

'''Read The Status of selected I/O Bit i.e. On/Off'''
d.getFeedback(u3.BitStateRead(IONumber = 4))

d.close()

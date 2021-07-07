import wmi

ports = wmi.WMI ()

for serialPort in ports.Win32_SerialPort ():
    print ("Name : %s" % (serialPort.Name))

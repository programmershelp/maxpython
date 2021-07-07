import wmi
myWMI = wmi.WMI ()

for processer in myWMI.Win32_Processor ():
    print ("Current Clock Speed : %s" % (processer.CurrentClockSpeed))
    print ("Name : %s" % (processer.Name))
    print ("Cores : %s" % (processer.NumberOfCores))

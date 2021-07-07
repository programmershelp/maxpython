import wmi
myWMI = wmi.WMI ()

for myTime in myWMI.Win32_LocalTime ():
    print (myTime.Hour,myTime.Minute,myTime.Second)
    print ("%s:%s:%s" % (myTime.Hour, myTime.Minute, myTime.Second))

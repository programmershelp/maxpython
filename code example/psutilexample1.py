import psutil,datetime

def printLine():
    print('----------------')

printLine()
print('CPU:')
print(str(psutil.cpu_times()))

printLine()
print('Memory:')
mem = psutil.virtual_memory()
memTotal = mem.total
memUsed = mem.used
memFree = mem.free
swap = psutil.swap_memory()
print('total memory -> ' + str(memTotal))
print('used  memory -> ' + str(memUsed))
print('free  memory -> ' + str(memFree))
print('swap:')
print(str(swap))

printLine()
print('Disk Info:')
diskInfoList = psutil.disk_partitions()
print(str(diskInfoList))
print("")
diskUsage = psutil.disk_usage('/')
print(str(diskUsage))
print("")
diskIOCounter = psutil.disk_io_counters()
print(str(diskIOCounter))
print("")
diskIOCounterPartition = psutil.disk_io_counters(perdisk=True)
print(str(diskIOCounterPartition))
print("")
printLine()

print('Network:')
netInfo = psutil.net_io_counters(pernic=True)
print(str(netInfo))
print("")
printLine()

print('System Users:')
print(str(psutil.users()))
print('System Uptime:')
uptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print(uptime)
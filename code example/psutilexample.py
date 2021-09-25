import psutil

# Retrieving information regarding the CPU
## Returns the system CPU times as a named tuple
print(psutil.cpu_times())

## Returns the system-wide CPU utilization as a percentage
print(psutil.cpu_percent())

## Returns the number of logical CPUs in the system
print(psutil.cpu_count())

## Returns the various CPU statistics as a tuple
print(psutil.cpu_stats())

## Returns the CPU frequency as a nameduple
print(psutil.cpu_freq())

# Retrieving information regarding the Memory
## Returns statistics about system memory usage as a named tuple
print(psutil.virtual_memory())

## Returns system swap memory statistics as a named tuple
print(psutil.swap_memory())

# Retrieving information regarding the Disks
## Returns all mounted disk partitions as a list of named tuples
print(psutil.disk_partitions())

## Returns disk usage statistics about the partition
print(psutil.disk_usage('/'))

## Returns system wide disk I/O statistics as a named tuple
print(psutil.disk_io_counters())

# Retrieving information regarding the Network
## Returns System wide network I/O statistics as a named tuple
print(psutil.net_io_counters())

## Returns system wide socket connections as a list of named tuples
print(psutil.net_connections())

## Returns addresses associated to each network interface card
print(psutil.net_if_addrs())

## Returns information regarding each network interface card
print(psutil.net_if_stats())

# Retrieving information regarding the Sensors
## Returns battery status information as a named tuple
print(psutil.sensors_battery())

# Retrieving information regarding Other System information
## Returns the system boot time
print(psutil.boot_time())

## Return users currently connected on the system
print(psutil.users())
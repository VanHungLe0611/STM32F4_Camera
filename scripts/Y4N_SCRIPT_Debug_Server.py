import os

#################################################################
# variable
#################################################################
server = "JLinkGDBServer"
interface = "swd"
#device = input('Device/MCU= ')
device = "STM32F429ZI"
endian = "little"
speed = "4000"
port = "2338"
swoport = "2339"
localhostonly = "1"
timeout = "0"
#################################################################
# flags
#################################################################
endian_flag = "-endian "+endian
device_flag = "-device " + device
interface_flag = "-if " + interface
speed_flag = "-speed " + speed
port_flag = '-port ' + port
swoport_flag = "-swoport " + swoport
other_flags_1 = "-vd -ir"
timeout_flag = "-timeout " + timeout
localhostonly_flag = "-localhostonly " + localhostonly
other_flags_2 = "-singlerun -strict"

options = server + ' ' + interface_flag + ' ' + device_flag + ' ' + endian_flag + ' ' + speed_flag + ' ' + port_flag + ' ' + swoport_flag + ' ' + other_flags_1 + ' ' + localhostonly_flag + ' ' + other_flags_2 + ' ' + timeout_flag

os.system(options)

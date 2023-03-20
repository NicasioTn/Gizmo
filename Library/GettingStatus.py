# import platform
 
# my_system = platform.uname()
 
# print(f"System: {my_system.system}")
# print(f"Node Name: {my_system.node}")
# print(f"Release: {my_system.release}")
# print(f"Version: {my_system.version}")
# print(f"Machine: {my_system.machine}")
# print(f"Processor: {my_system.processor}")
# import module
import subprocess

# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

# arrange the string into clear info
for item in Id:
	new.append(str(item.split("\r")[:-1]))
for i in new:
	print(i[2:-2])

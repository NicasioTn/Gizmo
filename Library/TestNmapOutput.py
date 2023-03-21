import nmap

# สร้างตัวแปร nm เพื่อใช้งาน nmap
nm = nmap.PortScanner()

# กำหนด target IP หรือชื่อโดเมนที่ต้องการสแกน
target = 'isanmsu.com'

# ใช้งานฟังก์ชัน scan() เพื่อสแกนพอร์ตทั้งหมด
nm.scan(hosts=target, arguments='')

# สร้าง output ทั้งหมด
output_all = nm.all_hosts()

# สร้าง output ตาม port, service, version, state
output_port = []
output_service = []
output_version = []
output_state = []

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            port_info = nm[host][proto][port]
            output_port.append(port)
            output_service.append(port_info['name'])
            output_version.append(port_info['version'])
            output_state.append(port_info['state'])

# แสดงผลลัพธ์
print('Output all hosts:', output_all)
print('Output by port:', output_port)
print('Output by service:', output_service)
print('Output by version:', output_version)
print('Output by state:', output_state)

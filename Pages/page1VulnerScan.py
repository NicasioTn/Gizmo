import csv

# Sample text data
text = """Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-12 14:25 EDT
Nmap scan report for isanmsu.com (203.159.92.102)
Host is up (0.012s latency).
Not shown: 986 filtered tcp ports (no-response)
PORT      STATE  SERVICE           VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp               Pure-FTPd
22/tcp    open   ssh               OpenSSH 8.0 (protocol 2.0)
53/tcp    open   domain            ISC BIND 9.11.36 (RedHat Enterprise Linux 8)
80/tcp    open   http              Apache/2
110/tcp   open   pop3              Dovecot DirectAdmin pop3d
143/tcp   open   imap              Dovecot imapd
443/tcp   open   ssl/https         Apache/2
465/tcp   open   ssl/smtp          Exim smtpd 4.96
587/tcp   open   smtp              Exim smtpd 4.96
993/tcp   open   imaps?
995/tcp   open   pop3s?
2222/tcp  open   ssl/EtherNetIP-1?
35500/tcp closed unknown
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :"""

# Split the text into lines
lines = text.split("\n")

# Extract the relevant information
host = lines[1].split()[-1]
port_data = lines[4:]

# Create a CSV writer object
with open("output.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the column headers
    csv_writer.writerow(["Host", "Port", "State", "Service", "Version"])

    # Loop through each port and extract the information
    for port in port_data:
        port_info = port.split()
        csv_writer.writerow([host, port_info[0], port_info[1], port_info[2], " ".join(port_info[3:])])


keys = ["Host", "Port", "State", "Service", "Version"]
result = []

import csv

filename = "./output.csv"

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

keys = ["Host", "Port", "State", "Service", "Version"]
result = []

for row in data[1:]:
    d = dict(zip(keys, row))
    d["Host"] = data[0][0]
    result.append(d)

print(result)

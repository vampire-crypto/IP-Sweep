import os 

OldHost = input("Please enter IP in xxx.xxx.xxx. format:") # in format 127.0.0. or 192.168.0. or 192.168.1.

for ip in range(0,255):
    NewHost = OldHost + str(ip)
    response = os.system("ping -c 1 -w 1 " + NewHost + ">/dev/null")
    if response == 0:
        print(NewHost, 'is up!')
    else:
        print(NewHost, 'is down!')

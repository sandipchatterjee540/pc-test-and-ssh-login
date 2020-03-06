import socket
import subprocess
import sys
import datetime


def command(ip,cmd):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username='support',password='password@123')
    stdin, stdout, stderr = client.exec_command(cmd)
    for line in stdout:
        print (line.strip('\n'))
        print(stdin)
        print(stderr)
    client.close()

def execute(ip):
    # remoteserver=input("Enter your IP : ")
    remoteserverIp=socket.gethostbyname(ip)
    port=22
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((remoteserverIp,port))
    while True:
        cmd=input("sandip-bash:$>")
        if result==0:
            command(remoteserverIp,cmd)
        else:
            print ('ssh service is not running')
        if cmd=='exit':
            break

remoteserver=input("Enter your IP : ")
print("-"*100)
print (''' Welcome to sandip terminal Connection Establish Sucessfully Type exit To Out of This Session  ''')
print("-"*100)
execute(remoteserver)






# -------------------------------------------------------------------

# subprocess.call('clear', shell=True)
# remoteserver = input("Enter your IP : ")
# remoteserverIP = socket.gethostbyname(remoteserver)

# t1 = datetime.datetime.now()
# print("-"*60)
# print("Scan is running " + str(remoteserverIP))
# print("-"*60)

# try:
#     for port in range(1, 999):
#         #print("1st stage")
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         #print("2nd stage")
#         #print (datetime.datetime.now())
#         result = sock.connect_ex((remoteserverIP, port))
#         #print("3rd stage")
#         #print (datetime.datetime.now())
#         if result == 0:
#             print("PORT: {} Open".format(port))
#         else:
#             print("PORT: {} Close".format(port))
#     #print("stage complete.......")

# except:
#     print("connection not establish")

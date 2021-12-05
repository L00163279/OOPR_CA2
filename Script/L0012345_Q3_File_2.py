# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

"Paramiko used to makes a connection with a remote device through SSH"
import paramiko
import time
import re


"SSH connection to the virtual machine"
def ssh_connection(ip):
    try:
        "Read VM id and Password"
        username = "l00163279"  # In an automation script read data from file
        password = "1122"  # never hard code

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, port=22, username=username, password=password)
        connection = session.invoke_shell()

        connection.send("ls > dir_contents.txt\n")  # unix command to list
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        ssh_connection("http://192.168.40.128")
    except Exception as err:
        print(err)


ssh_connection('192.168.40.128')
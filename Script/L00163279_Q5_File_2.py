# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

import time
import re
import paramiko

IP = '192.168.40.128'

def ssh_connection():
    """Function to open SSH connection to the device"""

    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(IP, username='l00163279', password='1122')
        connection = session.invoke_shell()
        connection.send("mkdir test\n")  # unix command to list
        connection.send('mkdir test/test1\n')
        connection.send('mkdir test/test2\n')
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(IP))
        else:
            print("Commands successfully executed on {}".format(IP))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        ssh_connection()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    ssh_connection()
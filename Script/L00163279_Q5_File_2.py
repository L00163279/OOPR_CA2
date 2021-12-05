# .............................

# File         :L00163279_Q3_File_2.py
# Author       :Muhammed Shafeeq Thottathil
# Version      :v1.0
# Created Date :05/12/2021
# Modified Date:05/12/2021
# Description  :Python script to connect to an Linux server and create folders via Python.
# Licensing    :Muhammed Shafeeq Thottathil

# ...............................

import time
import re
import paramiko

IP = '192.168.40.128'

"SSH connection to the virtual machine"
def vm_ssh_connection():

    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(IP, username='l00163279', password='1122')
        session.exec_command("sudo-S apt-get install curl")
        connection = session.invoke_shell()

        "Creation of Labs Directory"
        connection.send("mkdir Labs\n")  # unix command to list
        connection.send('mkdir Labs/Lab1\n')
        connection.send('mkdir Labs/Lab2\n')
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)

        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(IP))
        else:
            print("Commands successfully executed on {}".format(IP))
        session.close()

    #Exception for authentication error
    except paramiko.AuthenticationException:
        print("Authentication Error")
        vm_ssh_connection()

    except Exception as err:
        print(err)

"function call"
if __name__ == '__main__':
    vm_ssh_connection()
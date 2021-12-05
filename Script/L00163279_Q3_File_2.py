# .............................

# File         :L00163279_Q3_File_2.py
# Author       :Muhammed Shafeeq Thottathil
# Version      :v1.0
# Created Date :05/12/2021
# Modified Date:05/12/2021
# Description  :Connect virtual machine using python script using the ssh port.
# Licensing    :Muhammed Shafeeq Thottathil

# ...............................


import paramiko   #Paramiko used to makes a connection with a remote device through SSH
import time       #Time package used handle various operations regarding time
import re         #Package for the Regular Expression


"SSH connection to the virtual machine"
def vm_ssh_connection(ip):
    try:
        "VM User id and Password"
        username = "l00163279"    # In an automation script read data from file
        password = "1122"         # never hard code

        print("Establishing a connection.......\n")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, port=22, username=username, password=password)
        connection = session.invoke_shell()

        "list directory contens to a printable and readable TXT file"
        connection.send("ls > directory_contents.txt\n")  # unix command to list
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)

        "Connection checking condition"
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {} and connection was successful".format(ip))
        session.close()

    #Exception for authontication error
    except paramiko.AuthenticationException:
        print("Authentication Error")
        vm_ssh_connection("http://192.168.40.128")

    except Exception as err:
        print(err)

"Function call"
vm_ssh_connection('192.168.40.128')
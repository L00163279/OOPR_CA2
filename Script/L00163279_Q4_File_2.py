# .............................

# File         :L00163279_Q3_File_2.py
# Author       :Muhammed Shafeeq Thottathil
# Version      :v1.0
# Created Date :05/12/2021
# Modified Date:05/12/2021
# Description  :Python script to determine which ports are open.
# Licensing    :Muhammed Shafeeq Thottathil

# ...............................

import socket
import sys

"The Port to scan and check in VM environment"
PORT_TO_SCAN = [22, 80]

"Function to check remote ports"
def port_check():
    " read remote host address "
    remote_server = input("Enter a remote host to scan: ")
    remote_server_ip = socket.gethostbyname(remote_server)

    "Scanning Remote host"
    print("scanning remote host {}.........".format(remote_server_ip))
    print("--------------------------------------------\n")

    "Checking ports in remote server"
    try:
        for port in PORT_TO_SCAN:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))

            if result == 0:
                if(port == 22):
                    print("SSH")
                elif(port ==80):
                    print("HTTP")

                print("Port {}:    Open\n".format(port))
            sock.close()

    #Exception for the KeyboardInterrupt
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    #Exception for the host
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    #Exception for socket error
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

"Function Call"
if __name__ == "__main__":
    port_check()
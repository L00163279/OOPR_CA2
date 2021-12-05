# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

import socket
import sys
from datetime import datetime

PORT_TO_SCAN = [22, 80]

def port_scan():
    # Ask for input
    remote_server = input("Enter a remote host to scan: ")
    remote_server_ip = socket.gethostbyname(remote_server)

    # Print a nice banner with information on which host we are about to scan
    print_banner("Please wait, scanning remote host {}".format(remote_server_ip))

    # Check what time the scan started
    t1 = datetime.now()
    try:
        for port in PORT_TO_SCAN:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                if(port == 22):
                    print("SSH")
                elif(port ==80):
                    print("HTTP")

                print("Port {}:    Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

        # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


def print_banner(text):
    print("-" * 60)
    print()
    print("-" * 60)


if __name__ == "__main__":
    port_scan()
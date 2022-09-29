#!/usr/bin/env python3
"""Amazon Company | AMorales
   Conditionals - strings test true"""

def main():

    # this line now prompts the user for input
    ipchk = input("Apply an IP address: ")

    # a string tests as True
    if ipchk == "192.168.0.1" :
       print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("You did not provide input.") # indented under else
main()

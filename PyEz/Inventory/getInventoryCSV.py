#!/usr/bin/python3
# Purpose: Login to each Junos device in a list and print key information (suitable for import into MS Excel).
##################################################################################################################

## Load Required Modules
import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError


## Variables
factDict = {}
devices = [
	'100.123.12.0',
	'100.123.12.1',
	'100.123.12.2',
	'100.123.1.0'
        ]
passwd = getpass("Enter Password:")

## Main
print("HOSTNAME;MGMT-IP;MODEL;SERIAL-NUMBER;JUNOS-VERSION;UP-TIME")
for device in devices:
        dev = Device(host=device, user="jcluser", password=passwd)

        try:
                dev.open()

        except ConnectError as err:
                print ("Cannot connect to device: {0}".format(err))
                sys.exit(1)

        factDict = dev.facts['RE0']
        print(dev.facts['hostname'] + ";" + device + ";" + dev.facts['model'] + ";" + dev.facts['serialnumber'] + ";" + dev.facts['version'] + ";" + factDict['up_time'])
        dev.close()

## end of script ##


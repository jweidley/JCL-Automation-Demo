#!/usr/bin/python3
# Purpose: PrettyPrint dev.facts for 1 device
##################################################################################################################

## Load Required Modules
import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from pprint import pprint

## Variables
factDict = {}
devices = [
	'100.123.12.0'
        ]
passwd = getpass("Enter Password:")

## Main
for device in devices:
        dev = Device(host=device, user="jcluser", password=passwd)

        try:
                dev.open()

        except ConnectError as err:
                print ("Cannot connect to device: {0}".format(err))
                sys.exit(1)

        pprint (dev.facts)
        dev.close()

## end of script ##


#!/usr/bin/python3
# Purpose: Login to each Junos device in a list and print key information (suitable for import into MS Excel).
##################################################################################################################

## Load Required Modules
import sys
from prettytable import PrettyTable
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

print("########################################################################")
print(" Gathering Device Inventory Information....")
print("########################################################################")
print(" ")

## Main
table = PrettyTable()
table.field_names = ["HOSTNAME", "Mgmt-IP", "MODEL", "SERIAL_NUMBER", "OS_VERSION", "UP_TIME"]
for device in devices:
        dev = Device(host=device, user="jcluser", password="Juniper!1")

        try:
                dev.open()

        except ConnectError as err:
                print ("Cannot connect to device: {0}".format(err))
                sys.exit(1)

        factDict = dev.facts['RE0']
        table.add_row([dev.facts['hostname'],
                        device,
                        dev.facts['model'],
                        dev.facts['serialnumber'],
                        dev.facts['version'],
                        factDict['up_time']])

        dev.close()

print(table)

## end of script ##

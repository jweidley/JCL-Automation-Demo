#!/usr/bin/python3

# Modules
import yaml
from datetime import date
from jnpr.junos import Device
from lxml import etree
from pprint import pprint

# Variables
deviceFile = open('devices.yml', 'r')
today = date.today()
timestamp = today.strftime("%Y-%m-%d")

# Main
print("================================================")
print(" - Device Backup - ")
print("================================================")
print("  - Loading device list from YAML...")
deviceList = yaml.full_load(deviceFile)
#pprint(deviceList)

for device in deviceList:
    print("  - Logging into device: " + device)
    dev = Device(host=device, user="jcluser", password="Juniper!1")
    dev.open()
    outfile = open(device + "_" + timestamp + ".txt","w")
    config = dev.rpc.get_config(options={'format':'set'})
    outfile.write(etree.tostring(config).decode("utf-8"))
    outfile.close()
    print("    + Writing configuration to file")

print("!....Backups Completed....!")

## End of File ##

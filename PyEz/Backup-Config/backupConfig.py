#!/usr/bin/python3
from jnpr.junos import Device
from lxml import etree

# Create output files
setfile = open("vMX1-config-backup.set","w")
txtfile = open("vMX1-config-backup.native","w")

dev = Device(host="100.123.1.0", user="jcluser", password="Juniper!1")
dev.open()

# Format: set
config = dev.rpc.get_config(options={'format':'set'})
setfile.write(etree.tostring(config).decode("utf-8"))
setfile.close()

# Format: native
config = dev.rpc.get_config(options={'format':'text'})
txtfile.write(etree.tostring(config).decode("utf-8"))
txtfile.close()

dev.close()

## End of file ##

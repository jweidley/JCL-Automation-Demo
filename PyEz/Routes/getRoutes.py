#!/usr/bin/python3
from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.routes import RouteTable
 
with Device(host='100.123.1.0', user="jcluser", password="Juniper!1") as dev:

        routes = RouteTable(dev)
        routes.get()

        print("Route Table by Keys")
        pprint (routes.keys())

        print("Route Table by Items")
        pprint (routes.items())

dev.close()

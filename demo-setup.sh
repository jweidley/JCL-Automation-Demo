#!/bin/bash
# Purpose: Run this script first to setup the environment
# Version: 0.1
# Author: John Weidley
################################################################################

############
# Variables
############
JSNAPY_DIR="/home/jcluser/jsnapy"
SNAPSHOT_DIR="/home/jcluser/jsnapy/snapshots"

############
# Main
############
echo "################################################################"
echo " JCL Automation Demo: Initial Setup"
echo "################################################################"

# Download the Github repo
#echo "  - Downloading Github repo..."
#git clone https://github.com/jweidley/JCL-Automation-Demo.git /home/jcluser/

# Create required directories to store Jsnapy snapshots
echo "  - Creating directories for JSnapy Snapshots..."
if [ ! -d "/home/jcluser/jsnapy" ]
then
	echo "    + INFO: Creating $JSNAPY_DIR"
	mkdir /home/jcluser/jsnapy
else
	echo "    + INFO: Directory already exists: $JSNAPY_DIR"
fi


if [ ! -d "/home/jcluser/jsnapy/snapshots" ]
then
	echo "    + INFO: Creating $SNAPSHOT_DIR"
	mkdir /home/jcluser/jsnapy/snapshots
else
	echo "    + INFO: Directory already exists: $SNAPSHOT_DIR"
fi


# Install required Python3 libraries
echo "  - Installing required Python3 libraries..."
echo "    + Upgrading PIP..."
/bin/python3 -m pip install --upgrade pip
echo
echo "    + Installing PrettyTables..."
pip3 install prettytable

# Create fake upgrade image for large file transfer
echo "  - Create large file for large transfer demo..."
dd if=/dev/zero of=pseudo-junos-image.tgz bs=1M count=5
echo
echo "  - Move file to playbook directory..."
mv pseudo-junos-image.tgz /home/jcluser/JCL-Automation-Demo/Ansible/Secure-Copy/

### Done ###
echo
echo
echo "!...Demo Setup is Complete...!"

## End of Script ##

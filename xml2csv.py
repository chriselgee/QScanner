#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

# Take the input filename from command line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py nmap_output.xml")
    sys.exit(1)

nmap_xml_file = sys.argv[1]

def parse_nmap_xml_to_stdout(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall('host'):
        # Check if the host is up
        if host.find('status').get('state') == 'up':
            ip_address = host.find('address').get('addr')
            
            for port in host.findall('.//port'):
                state = port.find('state').get('state')
                if state == 'open':
                    portid = port.get('portid')
                    # Print each IP address and open port to standard out
                    print(f"{ip_address},{portid}")

parse_nmap_xml_to_stdout(nmap_xml_file)

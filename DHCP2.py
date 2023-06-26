#!python
'''Script to set Dynamic IP to the WiFi adaptor of laptop
 so that it auto configure to have an IP address that
 belongs to the same network address as that of the iiscwlan WAP.'''

import subprocess
dhcpCommand = '''netsh interface ip set address "WiFi" dhcp'''
command = dhcpCommand.split()
subprocess.run(command)
import serial

'''
Usage:

from command line and in directory containing script:

python mount_test_wisrd.py


Inputs:
	The dev path:
		Change the device path by replacing '/dev/ttyUSB1' with your device path, an example path would be '/dev/ttyUSB0'
		If you don't know your mount's path, it can be found using trial and error by running in terminal:
		python -m serial.tools.list_ports
		This will give you a list of active serial communication ports. The mount will have a USB device path of the form /dev/ttyUSB, followed by a number
		Try communicating with each port.
	Baud rate:
		The second input in line ___ is 9600, which is the baudrate. It can be changed to any value, namely 115200 for CEM40 mounts
	Commands:
		Every mount_port.write(b'<command>') sends a request to the mount to do something, and the mount will always send serial information back
		Any <command> can be sent to the mount this way. The available commands are from the iOptron RS-232 Command Langauge. For an IEq30Pro mount with 
		the most recent firmware, the documentation can be found at: http://www.ioptron.com/v/ASCOM/RS-232_Command_Language2014_V2.5.pdf
		If your mount doesn't meet these specs, go to github.com/panoptes/POCS/resources/mounts and look in the .yaml files for links to pdfs.

Outputs:
	Using the example commands with an IEq30Pro mount, the first output printed to console should be:
	'0030'

	The second depends on the version of your firmware.

	If you've added / changed the command sent to the mount, all you can expect is a response in the form stated by the documentation pdf. 
'''


with serial.Serial('/dev/ttyUSB1', 9600, timeout=3) as mount_port:
	print(mount_port)
	mount_port.write(b':MountInfo#')
	out = mount_port.read(4)
	print(out)
	mount_port.write(b':FW2#')
	out = mount_port.read(13)
	print(out)


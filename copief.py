import shutil
import os
from glob import glob
from subprocess import check_output
from shutil import copyfile

# File to be copied
src="/home/urbanhello/208/update.bin"

#Check if the USB is a REMI
def check_if_is_remi(name):
	if len(name)!=11:
		return False
	for character in list(name):
		if ord(character)<48:
			return False
		if ord(character)>57:
			return False
	return True
var=1	
while var==1:
#Check the computer devices
	sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
	usb_devices = (dev for dev in sdb_devices if 'usb' in dev.split('/')[5])
	devices = dict((os.path.basename(dev),dev) for dev in usb_devices)
	output = check_output(['mount']).splitlines()
	is_usb=lambda path: any(dev in path for dev in devices)
	usb_info= (line for line in output if is_usb(line.split()[0]))
	result=[(info.split()[0], info.split()[2]) for info in usb_info]

#copy file




	try:
		for r in result:
			if check_if_is_remi(r[1].split('/')[3]):
				print r[1]
				copyfile(src, r[1] +'/update.bin')

 # E.g. source and destination is the same location
	except shutil.Error as e:
		print("Error: %s" % e)
   # E.g. source or destination does not exist
	except IOError as e:
		print("Error: %s" % e.strerror)

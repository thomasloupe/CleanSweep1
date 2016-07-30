import sys
import shutil
import getpass
import time
import argparse
import logging
import os
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Provides additional logging", action="store_true")
args = parser.parse_args()


verbose = getattr(args, "verbose", False)
username = getpass.getuser()
tempfolder = 'C:/Users/%s/AppData/Local/Temp' % (username)


def user_input():
    print "This program will quickly remove any unwanted trash files from your computer."
    print "Would you like to proceed?"
    prompt = raw_input("Y/N: ")
    if prompt.lower() == "y":
        return True
    elif prompt.lower() == "n":
        return False
    else:
        sys.exit(1)

		
def get_size(start_path = tempfolder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def delete_the_files_verbose():
	#Calculate and display size before.
	size_before = get_size(tempfolder)
	
	
	#Delete the files.
	shutil.rmtree(tempfolder, ignore_errors=True)
	print "\n======================================================================"
	print "\nDone.\nNow running cleanmgr task. Please wait..."
	subprocess.check_call(['c:\windows\system32\cleanmgr.exe', '/autoclean /s /d C:'])
	print "Cleanmgr task has finished."
	

	# Calculate and display size after.
	size_after = get_size(tempfolder)
	deleted_stuff = size_before - size_after
	print "\n======================================================================"
	print "\nBefore: %s bytes.\nAfter: %s bytes.\nRemoved: %s bytes\n" % (size_before, size_after, deleted_stuff)
	
	try:
		#Let user know which files can't be deleted if verbose mode is on.
		print "======================================================================"
		print "INFO: Could not delete these files because they are in use!", os.listdir(tempfolder)
		print "======================================================================"
		done = raw_input("\nOperation complete. Press enter to exit: ")
		if len(done) > 0:
			sys.exit(0)
	except: 
		#Suppress the exception when a user hits enter.
		sys.exit(0)
	time.sleep(1)


def delete_the_files_quick():
	print "Please wait. Operation in progress."
	shutil.rmtree(tempfolder, ignore_errors=True)
	subprocess.check_call(['c:\windows\system32\cleanmgr.exe', '/autoclean /s /d C:'])
	try:
		done = raw_input("\nOperation complete. Press enter to exit: ")
		if len(done) > 0:
			sys.exit(0)
	except: 
		#Suppress the exception when a user hits enter.
		sys.exit(0)
	time.sleep(1)  	


if verbose == True:
    if user_input() == True:
        print "Now removing temp files at: %s." % (tempfolder)
	#Print file list to console because verbose mode is enabled.
	print os.listdir(tempfolder)
	delete_the_files_verbose()
	#Print message if user declines to continue then exit.
    elif user_input() == False:
        print "Operation aborted. No files have been modified."
        time.sleep(1)
        try:
            done = raw_input("Press enter to exit")
            sys.exit(0)
        except SyntaxError:
        #Suppress the exception when a user hits enter.
            sys.exit(0)
            

elif verbose == False:
    delete_the_files_quick()
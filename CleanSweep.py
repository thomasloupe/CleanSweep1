import sys
import shutil
import getpass
import time
import argparse
import logging
import os

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


def delete_the_files_verbose():
	# Calculate and display size before
	size_before = os.stat(tempfolder).st_size
	print "Size before removal: %s " % (size_before)
	
	# delete the files
	shutil.rmtree(tempfolder, ignore_errors=True)
	del(os); import os	
	# Calculate and display size after
	size_after = os.stat(tempfolder).st_size
	deleted_stuff = size_before - size_after
	print '%s removed. Before: %s | After: %s' % (deleted_stuff, size_before, size_after)
	
	try:
		#Let user know which files can't be deleted if verbose mode is on.
		print "======================================================================"
		print "INFO: Could not delete: %s because the files are in use!" % os.listdir(tempfolder)
		print "======================================================================"
		done = raw_input("\nOperation complete. Press enter to exit: ")
		if len(done) > 0:
			sys.exit(0)
	except: 
		#Suppress the exception when a user hits enter
		sys.exit(0)
	time.sleep(1)


def delete_the_files_quick():
    shutil.rmtree(tempfolder, ignore_errors=True)
    try:
		done = raw_input("\nOperation complete. Press enter to exit: ")
		if len(done) > 0:
			sys.exit(0)
    except: 
        #Suppress the exception when a user hits enter
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
        #Suppress the exception when a user hits enter		
            sys.exit(0)
            

elif verbose == False:
    delete_the_files_quick()
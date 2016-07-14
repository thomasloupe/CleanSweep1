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


def delete_the_files():
	#Get the file stats of the tempfolder.
	filestats = os.stat(tempfolder)
	
	#Tell user the size of the temp folder before removal.
	print "Size before removal: %s " % (filestats.st_size)
	
	#Bind it to a var for comparison later.
	oldsize = (filestats.st_size)
	
	#Delete the files.
	shutil.rmtree(tempfolder, ignore_errors=True)
	
	#Get the new size of the tempfolder.
	filestats = os.stat(tempfolder)
	
	#Bind it to another variable.
	newsize = (filestats.st_size)
	
	#Now calculate the difference between old and new sizes and bind result to "currentsize" var.
	currentsize = oldsize - newsize
	
	#Tell the user how much space they saved.
	print "\nSize after removal: %s " % (newsize)
	print "You saved %s bytes of data.\n" % (currentsize)
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


def delete_the_files1():
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
	delete_the_files()
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
    delete_the_files1()
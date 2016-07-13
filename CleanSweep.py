import sys
import shutil
import getpass
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Provides additional logging", action="store_true")
args = parser.parse_args()


verbose = getattr(args, "verbose", False)
username = getpass.getuser()
tempfolder = 'C:/Users/%s/AppData/Local/Temp' % (username)


def user_input():
    print "This program will quickly remove any unwanted trash files from your computer."
    print "Would you like to proceed?"
    prompt = raw_input("y/n: ")
    if prompt.lower() == "y":
        return True
    elif prompt.lower() == "n":
        return False
    else:
        sys.exit(1)
        
        
def delete_the_files():
    shutil.rmtree(tempfolder, ignore_errors=True)
    try: 
        done = raw_input("Operation complete. Press enter to exit")
        if len(done) > 0:
            sys.exit(0)
    except: 
        #suppress the exception when a user hits enter
        sys.exit(0)
    time.sleep(2)  


if verbose == True:
    if user_input() == True:
        print "Now removing temp files at %s" % (tempfolder)
        delete_the_files()
    elif user_input() == False:
        print "See you next time!"
        time.sleep(2)
        try:
            done = raw_input("Press enter to exit")
            sys.exit(0)
        except SyntaxError:  
            sys.exit(0)
            

elif verbose == False:
    delete_the_files()
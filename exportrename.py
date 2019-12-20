import os
import shutil
from os import path
import datetime

def main():
	# make a duplicate of an existing file
    if path.exists("OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt"):
	# get the path to the file in the current directory
        src = path.realpath("OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt");
		
    

	# rename the original file
        os.rename("OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt","career.guru99.txt")
		
if __name__ == "__main__":
    main()

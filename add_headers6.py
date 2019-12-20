import os
import shutil
from os import path
import datetime
import pandas as pd


def main():

    with open('file.csv', 'w') as f_output:
    my_file = "OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt"
    df = pd.read_csv(my_file, sep='|', names = ["HCM_Person_Number", "AD_Username", "OTM_Alias_GLUser", "OTM_Alias_Update_Date", "Extract_Date"])
    df.to_csv(my_file, sep='|', index = False)
    w = csv.writer(f_output, delimiter='|')


    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print (now.strftime("%Y%m%d%H%M%S"))
    newfile = ("OIM_USER_ALIAS."+now.strftime("%Y%m%d%H%M%S"))
    
	# make a duplicate of an existing file
    if path.exists("OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt"):
	# get the path to the file in the current directory
        src = path.realpath("guru99.txt");
		
	# rename the original file
        os.rename("OIM_USER_ALIAS.YYYYMMDDHHMMSS000.txt",newfile)
		
if __name__ == "__main__":
    main()

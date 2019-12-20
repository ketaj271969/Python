import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print (now.strftime("%Y%m%d%H%M%S"))
newfile = ("OIM_USER_ALIAS."+now.strftime("%Y%m%d%H%M%S"))
print(newfile)
import os
import difflib
f=open('file1.csv','r')  #open a file
f1=open('file2.csv','r') #open another file to compare
str1=f.read()
str2=f1.read()
str1=str1.split()  #split the words in file by default through the spce
str2=str2.split()
d=difflib.Differ()     # compare and just print
diff=list(d.compare(str1,str2))
print '\n'.join(diff)

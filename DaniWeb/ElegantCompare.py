import os
# Read in the original and new file          
orig = open('file1.csv','r')
new = open('file2.csv','r')
#in new but not in orig
bigb = set(new) - set(orig)
# To see results in console if desired
print(bigb)
# Write to output file    
with open('different.csv', 'w') as file_out:
    for line in bigb:
        file_out.write(line)
#close the files  
orig.close()    
new.close()    
file_out.close()

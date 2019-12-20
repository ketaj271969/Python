import os
# Read in the original and new file          
orig = open('Combine.csv','r')
new = open('HGD-TMT.csv','r')
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

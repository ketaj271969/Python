import pandas as pd
A=set(pd.read_csv("Combine.csv", index_col=False, header=None)[0]) #reads the csv, takes only the first column and creates a set out of it.
B=set(pd.read_csv("HGD-TMT.csv", index_col=False, header=None)[0]) #same here
print(A-B) #set A - set B gives back everything thats only in A.
print(B-A) # same here, other way around.

import pandas as pd
my_file = "my_file.csv"
df = pd.read_csv(my_file, sep='\t', names = ["a", "b", "c", "d", "e", "f"])
df.to_csv(my_file, sep='\t', index = False)

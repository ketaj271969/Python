import csv

with open('OIM_USER_ALIAS.YYYYMMDDHHMMSS000-template.txt') as f_input, open('file.csv', 'w') as f_output:
    r = csv.reader(f_input, delimiter='\t')
    w = csv.writer(f_output, delimiter='\t')

    w.writerow(['a', 'b','c','d','e','f'])
    w.writerows(r)

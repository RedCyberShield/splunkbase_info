import glob
import re 
import sys 
import os 


## DEF CREATION
def find(substr, infile, outfile):
    with open(infile) as a, open(outfile, 'a') as b:
        b.write('\n' + '\n' + infile + '\n')
        for line in a:
            for find in substr:
                if find in line:
                    b.write(line + '\n') 


# CREATE OUTPUT FILE
file1 = open("splunkbase_info_output.txt", "w")  # write mode
file1.write("Splunk App & TA Info \n" + '\n' + '\n')
file1.close()


## VAR CREATION
file_path = []
substr = ['label','id','version']


## CREATE FILE LIST
for file_name in glob.iglob('./**/app.conf', recursive=True):
    file_path.append(file_name)
print(file_path)


## ITERATE THROUGH FILE LIST TO FIND STRINGS
for file in file_path:
    print(file)
    find(substr, file, 'splunkbase_info_output.txt')


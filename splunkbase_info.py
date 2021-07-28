import glob
import re 
import sys 
import os 

def find(substr, infile, outfile):
    with open(infile) as a, open(outfile, 'a') as b:
        for line in a:
            b.write('\n' + '\n' + infile + '\n')
            if substr in line:
                b.write(line + '\n') 

file_path = []

## CREATE FILE LIST
for file_name in glob.iglob('./**/app.conf', recursive=True):
    file_path.append(file_name)

print(file_path)

## ITERATE THROUGH FILE LIST TO FIND STRINGS
for file in file_path:
    print(file)
    find('label', file, 'splunkbase_info_output.txt')
    find('id', file, 'splunkbase_info_output.txt')
    find('version', file, 'splunkbase_info_output.txt')
    # print(file.startswith("label"))
    # print(file.startswith("id"))
    # print(file.startswith("version"))

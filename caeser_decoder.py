#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import os,sys,io

decrp=""

try:
    file,shift,d_file=sys.argv[1:]
    shift=int(shift)
except ValueError:
    print('Command arguments: {} <encoded_file> <shift> <decoded_file>'.format(
        os.path.basename(sys.argv[0]))
    )
    sys.exit(1)
    

f_in = io.open(file,'r',encoding='ascii',errors='ignore')
txt= f_in.read()

for char in txt:
    value= ord(char) - shift
    decrp+= chr(value%128)
    
with open(d_file,'w') as f_out:
    f_out.write(decrp)

print("Succesfully decoded, saved into: " + d_file)
sys.exit(0)




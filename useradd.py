#!usr/bin/python3
import os
import crypt
count=0 
string=input()
for i in string :
        if i.isdigit() :
                count=1
if count == 0 : 
        par="hello"+string
        encPass = crypt.crypt(par,"22") 
        os.system("useradd -m -p" + encPass +" "+string)

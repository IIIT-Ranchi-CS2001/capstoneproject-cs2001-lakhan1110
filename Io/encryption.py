import io
import os

file=input("ENTER THE NAME OF THE TXT FILE AS XYZ.txt : ")

#READING THE FILE

with open(file,'r') as f:
    while True:
        s=f.readlines()
        if not s:
            break
        text=""
        for i in range(len(s)):
            text=text+s[i]
    f.close()


text2=""  

for i in range(len(text)):
        text2=text2+(text[i])

      

text3=""

for i in range(len(text2)):
    text3=text3+text2[i]+"|"


def encrypt(k):
    enc=""
    for i in range(0,len(k)):
        if(k[i]!="\n"):
            enc=enc+str(ord(k[i]))
        else:
            enc=enc+"\n"
        
    return enc

e=encrypt(text3)
#creating a backup if key is forgotten
backup=text2


#creating a key

key=(input("ENTER A KEY FOR THE ENCRYPTED FILE : "))


key="$"+key
enckey=""
for i in range(len(key)):
    enckey=enckey+key[i]+"|"

e=e+encrypt(enckey)


#encrypting the file
with open(file,'w')as f:
    f.write(e)
    f.close()
    
print("YOUR FILE HAS BEEN SUCCESSFULLY ENCRYPTED....")




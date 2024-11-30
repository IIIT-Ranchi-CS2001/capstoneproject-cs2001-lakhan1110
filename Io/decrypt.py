import io
import os


file=input("ENTER THE NAME OF THE FILE YOU WANT TO DECRYPT AS XYZ.txt : ")

#READING THE ENCRYPTED FILE

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
        

e=text2

#DECRYPTING THE FILE
       
l=e.split("124")
l.pop()

d=[]
for i in range(len(l)):
    if l[i]!="\n":
        d.append(chr(int(l[i])))
    else:
        d.append(l[i])
    

def verify(k):
    
    decode="".join(d)
    key2=(input("TO DECODE YOUR FILE PLEASE ENTER THE KEY : "))
    key=""
    for i in range(len(decode)-1,0,-1):
        key=decode[i]+key
        if(decode[i]=="$"):
            break

    vkey=key[1:len(key)]

    decode=decode.strip(key)

    if(key2!=vkey):
        if(k!=5):
            print("KEY IS INCORRECT, TRY AGAIN : ")
            verify(k+1)

        else:
            print("YOU HAVE BEEN BANNED FROM ACCESSING THE FILE")
            with open(file,'w') as f:
                f.write(" ")
                f.close()
    else:
        print("YOUR FILE HAS BEEN SUCCESSFULLY DECRYPTED :)")
        with open(file,'w')as f:
                f.write(decode)
                f.close()

verify(1)
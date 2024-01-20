fh=open('Output3.txt','w')
import random
length=int(input("Enter the length of password required : "))
char_included="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i=0
password=''
while(i<length):
    password=password+random.choice(char_included)
    i=i+1
print("Password =",password)
fh.write(f'length of password is {length} and random password is {password}')
fh.close()


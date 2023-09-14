s=input("Enter string to encrypt: \n")
sh=int(input("enter shift: \n"))
result=""
#def encrypt(s):
for i in range(len(s)):
    result+=chr(((ord(s[i])+sh-65)%26)+65)   
print(f"{result} \n")
re=0
for i in range(len(result)):
    re+=chr(((ord(result[i]-sh-65))%26)+65)
print(f"{re} \n")   
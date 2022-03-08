f=open("meraki2q.txt","r")
b=f.read()
f.close()
print(b)
i=0
c=0
while i<len(b):
    if b[i]=="\n":
        c+=1
    i+=1
print(c)



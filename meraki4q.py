f=open("meraki4q.txt","r")
d=f.read()
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
b=d.split("\n")
i=0
while i<len(b):
    if "delhi" in b[i]:
        file1.write(b[i])
        file1.write("\n")
    elif "shimla" in b[i]:
        file2.write(b[i])
        file2.write("\n")
    else:
        file3.write(b[i])
        file3.write("\n")
    i+=1
f.close()
file1.close()
file2.close()
file3.close()
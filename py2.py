file = open('countries.txt','r')
c=0
for line in file:
    c=c+1
    print(c,line,end = "")

file.close()
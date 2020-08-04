file=open("fengyue3.txt", 'r')
s=file.read()

yi=[]
er=[]
san=[]
si=[]

file1=open("yi.txt", 'r')
yii=file1.read()
file2=open("er.txt", 'r')
err=file2.read()
file3=open("san.txt", 'r')
sann=file3.read()
file4=open("si.txt", 'r')
sii=file4.read()

for a in yii:
     yi.append(a)
for a in err:
     er.append(a)
for a in sann:
     san.append(a)
for a in sii:
     si.append(a)


i=0
while i < len(s):
     you = 0
     for a in yi:
          if a==s[i]:
               you = 1
               
     for a in er:
          if a==s[i]:
               you = 1
               
     for a in san:
          if a==s[i]:
               you = 1
               
     for n in si:
          if n==s[i]:
               you = 1
               
     if you==0:
          print(s[i])
          xxx =input("输入:")
          if int(xxx)==1:
               yi.append(s[i])
          elif int(xxx)==2:
               er.append(s[i])
          elif int(xxx)==3:
               san.append(s[i])
          elif int(xxx)==4:
               si.append(s[i])
     

     i+=1

print("1:")
print(yi)
print("2:")
print(er)
print("3:")
print(san)
print("4:")
print(si)

          
          
          
          
     

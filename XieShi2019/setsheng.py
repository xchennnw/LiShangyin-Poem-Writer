from py2neo import *
graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')

file1=open("yi.txt", 'r')
s1=file1.read()
for x in s1:
     sss = "MATCH (a:Char) where a.name='"+x+"' set a.sheng = 1"
     graph.run(sss)

file2=open("er.txt", 'r')
s2=file2.read()
for x in s2:
     sss = "MATCH (a:Char) where a.name='"+x+"' set a.sheng = 2"
     graph.run(sss)

file3=open("san.txt", 'r')
s3=file3.read()
for x in s3:
     sss = "MATCH (a:Char) where a.name='"+x+"' set a.sheng = 3"
     graph.run(sss)

file4=open("si.txt", 'r')
s4=file4.read()
for x in s4:
     sss = "MATCH (a:Char) where a.name='"+x+"' set a.sheng = 4"
     graph.run(sss)

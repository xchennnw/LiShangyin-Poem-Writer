import random
from py2neo import *

class liyishan:
     theMark = 1

     def _init_(self):
          self.theMark =1
          

     def sevenChar(self, slist, char):
          graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')
          x=char
          aaa=[]
          s = "MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
          aaa=graph.run(s).data()
          if len(aaa)==0:
               s2="MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:two]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
               aaa.extend(graph.run(s2).data())
               s3="MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:two]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
               aaa.extend(graph.run(s3).data())
               if len(aaa)==0:
                    s4="MATCH (a:Char)-[:three1]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
                    aaa.extend(graph.run(s4).data())
                    s5="MATCH (a:Char)-[:three2]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
                    aaa.extend(graph.run(s4).data())
                    if len(aaa)==0:
                         s6="MATCH (a:Char)-[:next]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
                         aaa.extend(graph.run(s6).data())
                         s7="MATCH (a:Char)-[:next]->(b:Char)-[:two]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
                         aaa.extend(graph.run(s7).data())
          i=0
          while i < len(aaa):           
               jia = aaa[i]['a.name']
               yi = aaa[i]['b.name']
               bing = aaa[i]['c.name']
               ding = aaa[i]['d.name']
               wu = aaa[i]['e.name']
               ji = aaa[i]['f.name']
               geng = aaa[i]['g.name']
               uuu = jia+yi+bing+ding+wu+ji+geng
               slist.append(uuu)
               i+=1

     def sevenChar2(self, slist, char):
          graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')
          x=char
          aaa=[]
          s = "MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
          aaa=graph.run(s).data()
          i=0
          while i < len(aaa):           
               jia = aaa[i]['a.name']
               yi = aaa[i]['b.name']
               bing = aaa[i]['c.name']
               ding = aaa[i]['d.name']
               wu = aaa[i]['e.name']
               ji = aaa[i]['f.name']
               geng = aaa[i]['g.name']
               uuu = jia+yi+bing+ding+wu+ji+geng
               slist.append(uuu)
               i+=1


     def fourteenChar(self, char):
          self.theMark=0
          xxx=char
          graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')
          n1 = len(graph.nodes.match('Char', name = xxx))

          if n1==0:
               print("数据库中暂无此字，请等更新")
               self.theMark=0
          else:
               sss=[]
               tt=[]
               ttt=[]
               self.sevenChar(sss, xxx)
               if len(sss)==0:
                    self.theMark=1
               else:
                         
                    ran = random.randrange(len(sss))
                    shang = sss[ran]
                    theD = graph.nodes.match('Char', name = shang[6]).first()                  
                    for r1 in graph.match((theD, ), r_type="next"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)
              
                    for r1 in graph.match((theD, ), r_type="three1"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)

                    for r1 in graph.match((theD, ), r_type="three2"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)
                         

                    
                    theD = graph.nodes.match('Char', name = shang[0]).first()
                    for r1 in graph.match((theD, ), r_type="next"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three1"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three2"):
                         xxx=r1.end_node["name"]
                         self.sevenChar2(tt, xxx)
              
                    

                    if len(tt) == 0:      
                         self.theMark=1
                    else:

                         for t in tt:
                              aaa=0
                              i = 0
                              while i<7:
                                   j=0
                                   while j<7:
                                        if t[i]==shang[j]:
                                             aaa = 1
                                        j+=1
                                   i+=1
                              if aaa==0:
                                   ttt.append(t)
                         
                         if len(ttt)==0:
                              self.theMark=1
                         else:
                              ran2 = random.randrange(len(ttt))
                              xia = ttt[ran2]

                              self.theMark = 0
                              print(shang)
                              print(xia)
                              

     def twenty_eightChar(self, x):
          graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')
          xxx=x
          while self.theMark == 1:
               self.fourteenChar(xxx)
     
          vvv=[]
          xxxxx = graph.nodes.match('Char', name = xxx).first()
          for r1 in graph.match((xxxxx, )):
               vvv.append(r1.end_node["name"])

               
          ran3 = random.randrange(len(vvv))
          self.fourteenChar(vvv[ran3])

     
         
yishan = liyishan()
xxx =input("输入一字:")
print()
while yishan.theMark == 1:
     yishan.twenty_eightChar(xxx)
     




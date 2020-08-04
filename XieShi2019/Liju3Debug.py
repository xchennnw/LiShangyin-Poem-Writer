import random
from py2neo import *
graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')

def sevenChar( slist, char):
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

def sevenChar2( slist, char):
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

def sevenChar3( slist, char):
     x=char
     aaa=[]
     s = "MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
     aaa=graph.run(s).data()
     if len(aaa)==0:
          s2="MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:two]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
          aaa.extend(graph.run(s2).data())
          s3="MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:two]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
          aaa.extend(graph.run(s3).data())
          if len(aaa)==0:
               s4="MATCH (a:Char)-[:three1]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
               aaa.extend(graph.run(s4).data())
               s5="MATCH (a:Char)-[:three2]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
               aaa.extend(graph.run(s4).data())
               if len(aaa)==0:
                    s6="MATCH (a:Char)-[:next]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
                    aaa.extend(graph.run(s6).data())
                    s7="MATCH (a:Char)-[:next]->(b:Char)-[:two]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=3 or g.sheng=4) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
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

def sevenChar4( slist, char):
     x=char
     aaa=[]
     s = "MATCH (a:Char)-[:two]->(b:Char)-[:next]->(c:Char)-[:two]->(d:Char)-[:next]->(e:Char)-[:three1]->(f:Char)-[:three2]->(g:Char) WHERE a.name='"+x+"' and (g.sheng=1 or g.sheng=2) RETURN a.name, b.name, c.name, d.name, e.name, f.name, g.name"
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


def fourteenChar(char):
     xxx=char

     n1 = len(graph.nodes.match('Char', name = xxx))

     if n1==0:
          p="*数据库中暂无此字，请等更新"
          return p
     else:
          sss=[]
          tt=[]
          ttt=[]
          sevenChar(sss, xxx)
          if len(sss)==0:
               p="*数据库暂无此字诗句，请换个常见一些的字"
               return p
          else:
                    
               ran = random.randrange(len(sss))
               shang = sss[ran]
               theD = graph.nodes.match('Char', name = shang[6]).first()

             
             
               for r1 in graph.match((theD, ), r_type="next"):
                    xxx=r1.end_node["name"]
                    sevenChar2(tt, xxx)
         
               for r1 in graph.match((theD, ), r_type="three1"):
                    xxx=r1.end_node["name"]
                    sevenChar2(tt, xxx)

               for r1 in graph.match((theD, ), r_type="three2"):
                    xxx=r1.end_node["name"]
                    sevenChar2(tt, xxx)
                    

               if len(tt) == 0:
                    theD = graph.nodes.match('Char', name = shang[0]).first()
                    for r1 in graph.match((theD, ), r_type="next"):
                         xxx=r1.end_node["name"]
                         sevenChar2(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three1"):
                         xxx=r1.end_node["name"]
                         sevenChar2(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three2"):
                         xxx=r1.end_node["name"]
                         sevenChar2(tt, xxx)
         
               

               if len(tt) == 0:      
                    
                    p="!暂无此字诗句，请换个常见一些的字"
                    return p
                 
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
                              p="!暂无此字诗句，请换个常见一些的字"
                              return p 
                              

                         else:
                    
                        
                              ran2 = random.randrange(len(ttt))
                              xia = ttt[ran2]


                              
                              p=shang+xia
                              return p


def fourteenChar2(char):
     xxx=char

     n1 = len(graph.nodes.match('Char', name = xxx))

     if n1==0:
          
          p="!暂无此字诗句，请换个常见一些的字"
          return p
     else:
          sss=[]
          tt=[]
          ttt=[]
          sevenChar3(sss, xxx)
          if len(sss)==0:
               
               p="!暂无此字诗句，请换个常见一些的字"
               return p
          else:
                    
               ran = random.randrange(len(sss))
               shang = sss[ran]
               theD = graph.nodes.match('Char', name = shang[6]).first()

             
             
               for r1 in graph.match((theD, ), r_type="next"):
                    xxx=r1.end_node["name"]
                    sevenChar4(tt, xxx)
         
               for r1 in graph.match((theD, ), r_type="three1"):
                    xxx=r1.end_node["name"]
                    sevenChar4(tt, xxx)

               for r1 in graph.match((theD, ), r_type="three2"):
                    xxx=r1.end_node["name"]
                    sevenChar4(tt, xxx)
                    

               if len(tt) == 0:
                    theD = graph.nodes.match('Char', name = shang[0]).first()
                    for r1 in graph.match((theD, ), r_type="next"):
                         xxx=r1.end_node["name"]
                         sevenChar4(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three1"):
                         xxx=r1.end_node["name"]
                         sevenChar4(tt, xxx)
                    for r1 in graph.match((theD, ), r_type="three2"):
                         xxx=r1.end_node["name"]
                         sevenChar4(tt, xxx)
         
               

               if len(tt) == 0:
                    p="!暂无此字诗句，请换个常见一些的字"
                    return p
                    
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
                              p="!暂无此字诗句，请换个常见一些的字"
                              return p
                              

                         else:
                    
                        
                              ran2 = random.randrange(len(ttt))
                              xia = ttt[ran2]


                              
                              p=shang+xia
                              return p

def is_Chinese(word):
     for ch in word:
          if '\u4e00' <= ch <= '\u9fff':
               return True
     else:
          return False



xxx =input("输入一字:")

print()
iii = is_Chinese(xxx)
if iii==True:


     you1 = fourteenChar(xxx)

     if  you1[0] == '*':
          print(you1)
     else:
          while you1[0]=='!':
               you1 = fourteenChar(xxx)
          
          vvv=[]
          xxxxx = graph.nodes.match('Char', name = you1[6]).first()
          for r1 in graph.match((xxxxx, )):
               vvv.append(r1.end_node["name"])
               
          if len(vvv)==0:
               xxxxx = graph.nodes.match('Char', name = you1[4]).first()
               for r1 in graph.match((xxxxx, )):
                    vvv.append(r1.end_node["name"])
                    
               if len(vvv)==0:
                    xxxxx = graph.nodes.match('Char', name = you1[11]).first()
                    for r1 in graph.match((xxxxx, )):
                         vvv.append(r1.end_node["name"])

                    if len(vvv)==0:
                         xxxxx = graph.nodes.match('Char', name = you1[0]).first()
                         for r1 in graph.match((xxxxx, )):
                              vvv.append(r1.end_node["name"])
                              
          
                    
          else:
               ran=random.randrange(len(vvv))
               you2 = fourteenChar2(vvv[ran])

          while you2[0]=='!':
               ran=random.randrange(len(vvv))
               you2 = fourteenChar2(vvv[ran])

          print(you1)
          print(you2)

else:
     print("输入了无效字符")
          
          

          
     

     
         



     




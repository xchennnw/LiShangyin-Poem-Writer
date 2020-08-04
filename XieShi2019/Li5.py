from py2neo import Graph, Node, Relationship, NodeMatcher, PropertyDict
graph = Graph("http://localhost:7474", username="neo4j", password='Chen0225')


file=open("fengyue2.txt", 'r')
s=file.read()

length = len(s)



def luru( iii, jjj, ForS, rName):
     i = iii
     while i < length:
          j=1
          
          n1 = len(graph.nodes.match('Char', name = s[i]))
          
          if n1==0:
               a=Node("Char", name=s[i])
               graph.create(a)
          
          matcher = NodeMatcher(graph)
          a = matcher.match(name = s[i]).first()
               
          while j < jjj :
               
               n2 = len(graph.nodes.match('Char', name = s[i+j] ))

               if n2==0:
                    b=Node("Char", name=s[i+j])
                    graph.create(b)

               matcher = NodeMatcher(graph)
               b = matcher.match(name = s[i+j]).first()
                           
               r = Relationship(a, rName, b)
               graph.create(r)
               a=matcher.match(name = s[i+j]).first()
               j+=1

                      
          i+= ForS

luru( 0, 2 , 5, "two")
luru( 2, 2 , 5, "three1")
luru( 3, 2 , 5, "three2")
luru( 1, 2 , 5, "next")


file.close()



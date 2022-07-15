##adjacency list
def new_node(v):
    global node_count
    if v in nodes:
        print('Node already present in graph')
        return
    node_count+=1
    nodes.append(v)
    temp=[]
    graph[v]=temp
def add_edge(v1,v2):
    if v1 and v2 in nodes:
        graph[v1].append(v2)
    else:
        print('Node not present in graph')
def dis_adj_list(graph):
    print('******')
    for i in graph:
        print(i,graph[i])
    print('******')
def deletion(v):
    global node_count
    if v in nodes:
        graph.pop(v)
        for i in graph:
            temp=graph[i]
            for j in temp:
                if j==v:
                    temp.remove(j)
        nodes.remove(v)
        node_count-=1
    else:
        print('vertex node found')
def BFS(s_v):
  visited=[False]*(node_count)
  queue=[]
  queue.append(s_v)
  visited[s_v in nodes]=True
  while queue:
     s_v=queue.pop(0)
     print(s_v,end='  ')
     temp=graph[s_v]
     for i in range(node_count):
        for j in temp:
         if nodes[i]==j:
             queue.append(j)
             visited[i]=True 
def DFS(s_v):
    visited=[False]*node_count
    stack=[]
    stack.append(s_v)
    visited[s_v in nodes]=True
    while stack:
     s_v=stack.pop()
     print(s_v,end='  ')
     temp=graph[s_v]
     for i in range(node_count):
        for j in temp:
         if nodes[i]==j:
             stack.append(j)
             visited[i]=True 
nodes=[]
graph={}
node_count=0
print(graph)
print(nodes)
new_node('A')
new_node('B')
new_node('C')
new_node('F')
new_node('D')
new_node('G')
new_node('H')
print(nodes)
print(graph)
dis_adj_list(graph)
add_edge('A','B')
add_edge('C','B')
add_edge('C','A')
add_edge('C','D')
add_edge('C','H')
add_edge('D','F')
add_edge('A','G')
dis_adj_list(graph)
deletion('B')
dis_adj_list(graph)
BFS('C')
print()
DFS('C')
##adjacency matrix
def add_vertex(v):
    global node_count
    if v in nodes:
        print(f'{v} is already present in graph')
        return
    node_count+=1
    nodes.append(v)
    for i in adj_mat:
        i.append(0)
    temp=[]
    for i in range(node_count):
        temp.append(0)  
    adj_mat.append(temp)
def add_edge(n1,n2):
    if n1 and n2 in nodes:
        for i in range(node_count):
            if nodes[i]==n1:
                j=i
            if nodes[i]==n2:
                k=i
        adj_mat[j][k]=1
        adj_mat[k][j]=1
    else:
        print('Nodes are not present operation terminated')
def disp_adj_matrix(adj_matrix):
    for i in adj_matrix:
        print(i)
def deletion(v):
    global node_count
    if v in nodes:
        for i in range(node_count):
            if nodes[i]==v:
                j=i
        adj_mat.pop(j)
        for i in adj_mat:
            i.pop(j)
        nodes.remove(v)
        node_count=node_count-1
    else:
        print('given vertex is not in graph')
nodes=[]
adj_mat=[]
node_count=0
print(nodes)
print(adj_mat)
add_vertex('A')
add_vertex('B')
add_vertex('C')
print(nodes)
print(adj_mat)
disp_adj_matrix(adj_mat)
add_edge('A','C')
add_edge('A','B')
add_edge('B','C')
disp_adj_matrix(adj_mat)
deletion('C')
disp_adj_matrix(adj_mat)
add_vertex('D')
disp_adj_matrix(adj_mat)
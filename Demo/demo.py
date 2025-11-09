import networkx as nx
import numpy as np
from sklearn import preprocessing

G = nx.Graph()
G.add_node('0')
G.add_node('1')
G.add_node('2')
G.add_node('3')
G.add_node('4')
G.add_node('5')
G.add_node('6')
G.add_node('7')
G.add_node('8')
G.add_node('9')
G.add_edge('0','1')
G.add_edge('0','2')
G.add_edge('0','3')
G.add_edge('0','4')
G.add_edge('1','2')
G.add_edge('1','3')
G.add_edge('1','5')
G.add_edge('2','4')
G.add_edge('3','4')
G.add_edge('4','7')
G.add_edge('5','6')
G.add_edge('6','7')
G.add_edge('7','8')
G.add_edge('8','9')
print(G.nodes)
print(len(G.edges))
adj_matrix = nx.adjacency_matrix(G).toarray()
Attr = np.array([
    [1,1,1,1],
    [1,0,0,1],
    [1,0,1,0],
    [0,1,1,1],
    [1,1,0,1],
    [1,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,0,1,1],
    [0,0,0,1]
])
#求节点的邻居
def get_neighbors(u):
    return list(nx.neighbors(G,str(u)))

#求节点的公共邻居
def get_common_neighbors(u,v):
    return list(nx.common_neighbors(G,str(u),str(v)))
# print(get_common_neighbors(0,3))

#求节点的邻居并集
def get_union_neighbors(u,v):
    u_neighbors = get_neighbors(u)
    v_neighbors = get_neighbors(v)
    union_neighbors = set(u_neighbors).union(v_neighbors)
    return list(union_neighbors)

#求节点的度
def get_degree(u):
    return nx.degree(G,str(u))

#获取每个节点的度
def get_everynodedegree(G):
    node_degree = []
    for node in sorted(list(G.nodes())):
        node_degree.append(nx.degree(G,node))
    return node_degree

#变形jaccard相似度，节点间的相似度用节点邻居交集度除以并集度
def get_Sim(G):
    n = len(G.nodes)
    T = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1,n):
            if i != j:
                inter = get_common_neighbors(i,j)
                union = get_union_neighbors(i,j)
                inter_degree = sum([get_degree(i) for i in inter])
                union_degree = sum([get_degree(i) for i in union])
                if inter_degree != 0 and union_degree != 0:
                    T[i][j] = inter_degree / union_degree
                    T[j][i] = inter_degree / union_degree
                else:
                    T[i][j] = 0
                    T[j][i] = 0
    return T
#计算两个向量的余弦相似度
def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x)*np.linalg.norm(y)
    return num/denom


#属性的余弦相似度矩阵
def get_AttrSim(Attr):
    n = len(G.nodes)
    Attr_Sim = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Attr_Sim[i][j] = cosine_similarity(Attr[i],Attr[j])
    return Attr_Sim
T = get_Sim(G)
A = get_AttrSim(Attr)
print(T)
print('----------------------------')
print(A)
print('-------------------------------')
W = 0.7*T + 0.3*A
print(W)
#得到偏向社区内部节点间游走的转移概率矩阵
def get_InsideTransitionMatrix(W,nodes_degree_list):
    n = W.shape[0]
    nodes_degree = nodes_degree_list
    Inside_Matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            Inside_Matrix[i][j] = W[i][j] * nodes_degree[j]
    Inside_Transition_Matrix = preprocessing.normalize(Inside_Matrix, 'l1')
    return Inside_Transition_Matrix

#得到偏向社区边界节点间游走的转移概率矩阵
def get_BoundaryTransitionMatrix(W,nodes_degree_list):
    #把转移概率矩阵中的值除以每个节点的度，使边界节点中相似度更高的节点有更大的转移概率
    n = W.shape[0]
    nodes_degree = nodes_degree_list
    Boundary_Matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            Boundary_Matrix[i][j] = W[i][j] / nodes_degree[j]
    Boundary_Transition_Matrix = preprocessing.normalize(Boundary_Matrix,'l1')
    return Boundary_Transition_Matrix

nodes_degree_list = get_everynodedegree(G)
print(nodes_degree_list)

W1 = get_InsideTransitionMatrix(W,nodes_degree_list)
W2 = get_BoundaryTransitionMatrix(W,nodes_degree_list)
print(W1)
print('--------------------------------')
print(W2)
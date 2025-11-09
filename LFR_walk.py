from gensim.models import Word2Vec
from tqdm import tqdm
import random
import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from evaluate import Metrics

# from Transition_Matrix import get_JaccardSim,get_AttrSim,get_BoundaryTransitionMatrix,get_InsideTransitionMatrix

np.seterr(divide='ignore',invalid='ignore')


#得到图的所有节点
def get_nodes(G):
    return G.nodes()
# print(get_nodes())

#求图中所有节点的度
def get_totaldegree(G):
    sum = 0
    for node in list(G.nodes()):
        sum += nx.degree(G,node)
    return sum

#获取每个节点的度
def get_everynodedegree(G):
    node_degree = []
    for node in sorted([int(node) for node in G.nodes()]):
        node_degree.append(nx.degree(G,str(node)))
    return node_degree

'''#获得每个属性值被多少个节点拥有的个数(矩阵按列求和，当axis=1时按行求和）
def get_attrdegree(atrr):
    attr_degree = np.sum(atrr,axis=0)
    return list(attr_degree)'''

#获得每个节点的属性数
def get_attrdegree(atrr):
    attr_degree = np.sum(atrr,axis=1)
    return list(attr_degree)

#求节点的邻居
def get_neighbors(u):
    return list(nx.neighbors(G,str(u)))
# print(get_neighbors(3))

#求节点的二阶邻居节点
def get_secondneighbors(u):
    second_neighbors = []
    first_neighbors = get_neighbors(u)
    second = []
    for i in first_neighbors:
        second_neighbors.append(i)
        l = get_neighbors(i)
        second.append(l)
    for i in second:
        for j in i:
            second_neighbors.append(j)
    second_neighbors_set = set(second_neighbors)
    second_neighbors = list(second_neighbors_set)
    return second_neighbors

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
# print(get_degree('3'))

#求节点的所有邻居节点的度
def get_neighbordegree(n):
    sum = 0
    for i in n:
        sum += get_degree(i)
    return sum

#求节点的邻接矩阵和属性矩阵非0元素集合
def get_AttrList(n):
    fet = []
    for k, v in enumerate(n):
        f = []
        for i, j in enumerate(v):
            if j != 0:
                f.append(i)
        fet.append(f)
    return fet

#sigmod函数
def sigmod(x):
    return 1 / (1 + np.exp(x))

#计算两个向量的余弦相似度
def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x)*np.linalg.norm(y)
    return num/denom

#计算图节点的度矩阵
def get_degreematrix(adj):
    degree_matrix = np.zeros_like(adj)
    fet = get_AttrList(adj)
    for i in range(len(fet)):
        degree_matrix[i][i] = len(fet[i])
    return degree_matrix

#属性的余弦相似度矩阵
def get_AttrSim(Attr):
    n = len(G.nodes)
    Attr = Attr[np.argsort(Attr[:, 0])]
    Attr = Attr[:, 1:]
    Attr_Sim = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Attr_Sim[i][j] = cosine_similarity(Attr[i],Attr[j])
    return Attr_Sim


# 拓扑节点的jaccard相似度
def get_JaccardSim(G):
    n = len(G.nodes)
    Jcd_Sim = np.zeros((n, n))
    for i in tqdm(range(n)):
        for j in range(i + 1, n):
            inter = get_common_neighbors(i, j)
            union = get_union_neighbors(i, j)
            if len(union) > 0:
                Jcd_Sim[i][j] = len(inter) / len(union)
                Jcd_Sim[j][i] = len(inter) / len(union)
    return Jcd_Sim


# 计算节点间的高阶(二阶)jaccard相似度
def get_HighOrderJaccardSim(G):
    n = len(G.nodes)
    High_Order_JcdSim = np.zeros((n, n))
    for i in tqdm(range(n)):
        for j in range(i + 1, n):
            if get_common_neighbors(i, j) != 0:
                High_Order_JcdSim[i][j] = len(get_common_neighbors(i, j)) / len(get_union_neighbors(i, j))
                High_Order_JcdSim[j][i] = len(get_common_neighbors(i, j)) / len(get_union_neighbors(i, j))
            else:
                second1 = get_secondneighbors(i)
                second2 = get_secondneighbors(j)
                second_inter = second1.intersection(second2)
                second_union = second1.union(second2)
                High_Order_JcdSim[i][j] = len(second_inter) / len(second_union)
                High_Order_JcdSim[j][i] = len(second_inter) / len(second_union)
    return High_Order_JcdSim


# 变形jaccard相似度，节点间的相似度用节点邻居交集度除以并集度
def get_DegreeSim(G):
    n = len(G.nodes)
    T = np.zeros((n, n))
    for i in tqdm(range(n)):
        for j in range(i + 1, n):
            if i != j:
                inter = get_common_neighbors(i, j)
                union = get_union_neighbors(i, j)
                inter_degree = sum([get_degree(i) for i in inter])
                union_degree = sum([get_degree(i) for i in union])
                if inter_degree != 0 and union_degree != 0:
                    T[i][j] = inter_degree / union_degree
                    T[j][i] = inter_degree / union_degree
                else:
                    T[i][j] = 0
                    T[j][i] = 0
    return T


'''#得到偏向社区内部节点间游走的转移概率矩阵
def get_InsideTransitionMatrix(W):
    # W = para * T + (1 - para) * A
    Inside_Transition_Matrix = preprocessing.normalize(W, 'l1')
    return Inside_Transition_Matrix'''

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

'''#获取每个节点的度
def get_everynodedegree(G):
    node_degree = []
    for node in sorted(list(G.nodes())):
        node_degree.append(nx.degree(G,node))
    return node_degree'''


#获得每个节点的游走次数
def get_numwalks(G,Attr):
    d = get_everynodedegree(G)
    Attr = Attr[np.argsort(Attr[:, 0])]
    # print(Attr)
    Attr = Attr[:, 1:]
    a = get_attrdegree(Attr)
    length = []
    for i in range(len(d)):
        # length.append(d[i] + a[i])
        length.append(max(d[i],a[i]))
    return length

#获得每个节点的游走长度
def get_walklength(G,Attr):
    d = get_everynodedegree(G)
    Attr = Attr[np.argsort(Attr[:, 0])]
    # print(Attr)
    Attr = Attr[:, 1:]
    a = get_attrdegree(Attr)
    num = []
    for i in range(len(d)):
        sum = d[i] + a[i]
        num.append(math.ceil(sum/2))
    return num

def get_NumLength(G):
    d = get_everynodedegree(G)
    return d


#对转移概率矩阵中每行元素进行从大到小排序，并返回转移概率对应的节点序号
def get_NodesTransitionSorted(matrix):
    nodes_transition_sorted = []
    for k,v in enumerate(matrix):#将转移概率矩阵中非零元素保存成字典
        f = {}
        for i,j in enumerate(v):
            if j != 0:
                f[i] = j
        nodes_transition_sorted.append(f)
    key_value = []
    for i in nodes_transition_sorted:#对转移概率矩阵的字典按value进行排序
        new_dict = sorted(i.items(), key=lambda x: x[1], reverse=True)#对字典按值进行从大到小排序
        key_value.append(new_dict)
    nodes_index = []
    for i in key_value:#对排序后的value返回其key值
        key = []
        for j in i:
            key.append(str(j[0]))
        nodes_index.append(key)
    return nodes_index#最终返回转移概率矩阵中每行非零元素从大到小排序的索引值

#对转移概率矩阵中非零元素的节点PageRank值进行从大到小排序，并返回节点索引
def get_NodesPageRankSorted(transition_matrix,G):
    pg_rank = nx.pagerank(G)
    fet = []
    for k, v in enumerate(transition_matrix):
        f = {}
        for i, j in enumerate(v):
            if j != 0:
                # f.append(pg_rank[str(i)])
                f[str(i)] = pg_rank[str(i)]
        fet.append(f)
    print(fet)
    nodes_pg_sorted = []
    for dict in fet:
        new_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        nodes_pg_sorted.append(new_dict)
    print(nodes_pg_sorted)
    indexs = []
    for i in nodes_pg_sorted:
        key = []
        for j in i:
            key.append(j[0])
        indexs.append(key)
    return indexs

def get_randomwalk(G,start_node,walk_length_list,Lmax,transition_matrix):
    '''
    输入起始节点和随机游走长度，生成随机游走序列
    :param node:
    :param path_length:
    :return:
    '''
    walk = [start_node]
    walk_length = min(walk_length_list[int(start_node)],Lmax)
    while len(walk) < walk_length:
        curr_node = walk[-1]
        next_nodes = transition_matrix[int(curr_node)]
        next_nodes = next_nodes[:math.ceil(len(transition_matrix[int(curr_node)]) * 0.1)]
        if len(next_nodes) > 0:
            walk.append(random.choice(next_nodes))
        else:
            break
    return walk



def get_totalwalks(num_walks_list,walk_length_list,Lmax,G,nodes,nodes_transition_inside,nodes_transition_boundary):
    # num_walks_list = get_numwalks(G,Attr)
    # all_nodes = list(G.nodes())
    node_degree = get_everynodedegree(G)
    l = []
    for i in range(len(node_degree)):
        l.append((i,node_degree[i]))
    l = sorted(l, key=lambda x: x[1],reverse=True)
    ll = [str(i[0]) for i in l]
    in_nodes = node_degree[:math.ceil(len(ll)*0.6)]
    bd_nodes = node_degree[math.ceil(len(ll)*0.6):]
    walks = []
    for node in tqdm(nodes):
        num_walks = num_walks_list[int(node)]
        if node in in_nodes:
            for i in range(num_walks):
                walks.append(get_randomwalk(G=G,start_node=node,walk_length_list=walk_length_list,Lmax=Lmax,transition_matrix=nodes_transition_inside))
        else:
            for i in range(num_walks):
                walks.append(get_randomwalk(G=G,start_node=node,walk_length_list=walk_length_list,Lmax=Lmax,transition_matrix=nodes_transition_boundary))
    return walks


if __name__ == '__main__':
    # 读取边集文件，构造图，得到邻接矩阵
    G = nx.read_edgelist("D:\CodeData\PaperCode\DataSet\LFR2000\LFR0.7\\network.txt", create_using=nx.DiGraph())
    G = G.to_undirected()
    adj_matrix = nx.adjacency_matrix(G).toarray()
    # 读取属性文件，得到属性矩阵
    Attr = np.loadtxt('D:\CodeData\PaperCode\DataSet\LFR2000\LFR0.7\\feature.txt', dtype=int)
    num_walks_list = get_numwalks(G,Attr)#节点的度跟属性数之和的均值
    walk_length_list = get_walklength(G,Attr)#节点的度跟属性数之和
    Attrs = Attr[np.argsort(Attr[:, 0])]
    Attrs = Attrs[:, 1:]
    T = get_JaccardSim(G)
    A = get_AttrSim(Attrs)

    node_degree_list = get_everynodedegree(G)
    para = 0.7
    W = para * T + (1 - para) * A
    Inside_Transition_Matrix = get_InsideTransitionMatrix(W,node_degree_list)
    # Inside_Transition_Matrix = get_InsideTransitionMatrix(W)
    Boundary_Transition_Matrix = get_BoundaryTransitionMatrix(W,node_degree_list)
    nodes_transition_inside = get_NodesTransitionSorted(Inside_Transition_Matrix)
    nodes_transition_boundary = get_NodesTransitionSorted(Boundary_Transition_Matrix)
    # walk_length = 100
    # num_walks = 50
    Lmax = 100
    nodes = list(G.nodes)

    # walks = get_totalwalks(walk_length,num_walks,G,nodes,Attr,Inside_Transition_Matrix,Boundary_Transition_Matrix)
    walks = get_totalwalks(walk_length_list=walk_length_list, num_walks_list=num_walks_list, Lmax=Lmax, G=G, nodes=nodes, nodes_transition_inside=nodes_transition_inside, nodes_transition_boundary=nodes_transition_boundary)
    # print(walks)
    print(len(walks))
    model = Word2Vec(walks, vector_size=128, window=5, min_count=0, sg=1, workers=8, epochs=4)
    X = model.wv.vectors
    np.savetxt('D:\CodeData\PaperCode\\visual_emb\LFR_2000_0.7',X)







'''import networkx as nx
from networkx.generators.community import LFR_benchmark_graph
from collections import defaultdict
from numpy.random import choice
import matplotlib.pyplot as plt

n = 1000
tau1 = 2
tau2 = 1
mu = 0.1
k_min = 5
k_max = 100
min_community = 100
max_community = 150
n_communities = 10
n_attrs = 5

# 生成网络
G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=50, min_degree=k_min, max_degree=k_max, min_community=min_community, max_community=max_community, n_communities=n_communities)

# 生成节点属性
for node in G.nodes():
  attrs = choice([0, 1], size=n_attrs)
  G.node[node]['attrs'] = attrs

# 可视化网络
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()

# 可视化节点属性
color_map = {0: 'b', 1: 'r'} # 将二进制属性0和1的显示颜色分别赋为蓝色和红色
node_color = [color_map[G.node[node]['attrs'][0]] for node in G.nodes()]
node_size = [G.degree(node) * 5 for node in G.nodes()] # 节点大小与度数有关
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size)
plt.show()'''
import numpy as np
import networkx as nx
from numpy.random import choice
from sklearn.cluster import KMeans

'''attr = 100
G = nx.read_edgelist('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\\network.dat',create_using=nx.DiGraph())
G = nx.to_undirected(G)
label = np.loadtxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\community.dat',dtype=int)
k = max(label[:,-1])
print(k)
n = len(G.node())
A = np.zeros((n,attr))
B = np.zeros((k,attr))
for i in range(k):
    B[i] = choice([0,1],size=attr)
print(B)
print(B.shape)
l = []
for k,v in enumerate(label):
    ll = []
    for i,j in enumerate(v):
        ll.append(j)
    l.append(ll)
# print(l)
for i in l:
    A[i[0] - 1] = B[i[1] - 1]
print(A.shape)
print(A[:10,:10])

np.savetxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\\feature.txt',A,fmt='%d')'''
'''for node in G.nodes():
  attrs = choice([0,1],size=n_attr)
  G.node[node]['attrs'] = attrs
  l.append(list(G.node[node]['attrs']))
  # print(G.node[node]['attrs'])
  # print(type(G.node[node]['attrs']))
print(l)
print(np.array(l))
k = np.array(l)
re = KMeans(n_clusters=2).fit_predict(k)
print(re)
print(G.node)'''
'''n = np.loadtxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\\network.dat',dtype=int)
n = n-1
np.savetxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\\network.txt',n,fmt='%d')
l = np.loadtxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\community.dat',dtype=int)
l = l-1
np.savetxt('D:\CodeData\PaperCode\DataSet\LFR5000\LFR0.7\label.txt',l,fmt='%d')'''
attr=4
B=np.zeros((10,4))
for i in range(10):
    B[i] = choice([0,1],size=attr)
print(B)




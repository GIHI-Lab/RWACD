import community as community_louvain
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from evaluate import Metrics

# 创建一个无向图
G = nx.read_edgelist("D:\CodeData\PaperCode\DataSet\citeseer\\network.txt",create_using=nx.DiGraph())
G = G.to_undirected()

# 计算最佳社区划分并可视化结果
partition = community_louvain.best_partition(G)
print(partition)
l = []
for k,v in partition.items():
    l.append(v)
print(l)
label = np.loadtxt("D:\CodeData\PaperCode\DataSet\citeseer\label.txt", dtype=int)
real_com = label[:, -1]
print(real_com)
FscoreList = []
AccList = []
NMIList = []
ARIList = []
pred_com = np.array(l)
print(pred_com)
'''metrics = Metrics(real_com, pred_com)
Fscore, Accuracy, NMI, ARI = metrics.getFscAccNmiAri()
FscoreList.append(Fscore)
AccList.append(Accuracy)
NMIList.append(NMI)
ARIList.append(ARI)
print(max(FscoreList))
print(max(AccList))
print(max(NMIList))
print(max(ARIList))'''
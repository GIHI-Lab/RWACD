import networkx as nx
import matplotlib.pyplot as plt

plt.rc('font', family='Times New Roman')

G = nx.karate_club_graph()
C = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':1,'10':1,'11':0,'12':0,'13':0,'14':0,'15':1,'16':1,'17':0,'18':0,'19':1,'20':0,'21':1,'22':0,'23':1,'24':1,'25':1,'26':1,'27':1,'28':1,'29':1,'30':1,'31':1,'32':1,'33':1,'34':1}

# 使用标签传播社区检测算法将节点分配到不同的社区
communities = nx.algorithms.community.label_propagation_communities(G)
community_mapping = {node: i for i, community in enumerate(communities) for node in community}
print(community_mapping)

# 创建节点颜色列表，使属于同一社区的节点颜色相同
node_colors = [community_mapping.get(node, -1) for node in G.nodes]

# 绘制可视化图形
nx.draw(G, with_labels=False, node_color=node_colors, cmap=plt.cm.Set1)
plt.savefig("D:\Research Direction\Paper\SVG\\karate_F.svg", dpi=300,format="svg")
plt.show()
import networkx as nx
import matplotlib.pyplot as plt

import csv

with open('D:\CodeData\PaperCode\DataSet\BolgCatalog\\network.txt', 'r') as txt_file:
    lines = txt_file.readlines()
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for line in lines:
        # 假设文本文件中的每一行都是以空格分隔的字段
        fields = line.strip().split('\t')
        writer.writerow(fields)
'''import csv
import pandas as pd

# 读取CSV文件数据
df = pd.read_csv('output.csv')

# 新增一行
new_row = {'Column1': 'id', 'Column2': 'source', 'Column3': 'target'}
df = df.append(new_row, ignore_index=True)

# 新增一列
# new_column = ['Value1', 'Value2', 'Value3', 'Value4']
# df['NewColumn'] = new_column

# 将修改后的数据保存为新的CSV文件
df.to_csv('output1.csv', index=False)'''
'''G = nx.read_edgelist("D:\CodeData\PaperCode\DataSet\citeseer\\network.txt", create_using=nx.DiGraph())
G = G.to_undirected()
node = G.nodes
def get_everynodedegree(G):
    node_degree = []
    for node in sorted([int(node) for node in G.nodes()]):
        node_degree.append(nx.degree(G,str(node)))
    return node_degree
D = get_everynodedegree(G)
count = 0
for i in D:
    if i == 1:
        count += 1
print(count)
'''


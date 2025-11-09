import numpy as np
import matplotlib.pyplot as plt  # 导入所需库
'''# 导入数据
x = np.arange(2)
Louvain = [0.124, 0.160]
DeepWalk = [0.235, 0.228]
LINE = [0.136, 0.212]
Node2Vec = [0.245, 0.189]
AANE = [0.209,0.320]
AWBA = [0.338, 0.277]
Ours = [0.327, 0.523]
# 设置所需参数
total_width, n = 0.8, 7  # （柱状图的默认宽度值为 0.8）
width = total_width / n
x = x - (total_width - width) / 2  # 现在的x是每个并列柱的第一柱的中心横坐标
# 绘制图
plt.bar(x, Louvain,  width=width, label='Louvain', hatch='***', edgecolor = 'k',color='white')
plt.bar(x + width, DeepWalk, width=width, label='DeepWalk', hatch='///',edgecolor = 'k',color='white')
plt.bar(x + 2 * width, LINE, width=width, label='LINE', hatch='|||',edgecolor = 'k',color='white')
plt.bar(x + 3 * width, Node2Vec, width=width, label='Node2Vec', hatch='+++',edgecolor = 'k',color='white')
plt.bar(x + 4 * width, AANE, width=width, label='AANE', hatch='\\\\\\',edgecolor = 'k',color='white')
plt.bar(x + 5 * width, AWBA, width=width, label='AWBA', hatch='ooo',edgecolor = 'k',color='white')
plt.bar(x + 6 * width, Ours, width=width, label='Ours', hatch='xxx',edgecolor = 'k',color='white')
plt.xticks(np.arange(2), ['Citeseer', 'BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=7, handletextpad=0.1, frameon=False)  # 添加图例
# plt.legend(loc='upper left',frameon=False)
plt.ylabel('NMI')
plt.savefig('D:\CodeData\PaperCode\image\Algorithm-NMI',dpi=300)
plt.show()'''
'''# 导入数据
x = np.arange(2)
Louvain = [0.112, 0.101]
DeepWalk = [0.124, 0.142]
LINE = [0.112, 0.144]
Node2Vec = [0.129, 0.095]
AANE = [0.158,0.225]
AWBA = [0.276, 0.176]
Ours = [0.296, 0.413]
# 设置所需参数
total_width, n = 0.8, 7  # （柱状图的默认宽度值为 0.8）
width = total_width / n
x = x - (total_width - width) / 2  # 现在的x是每个并列柱的第一柱的中心横坐标
# 绘制图
plt.bar(x, Louvain,  width=width, label='Louvain', hatch='***', edgecolor = 'k',color='white')
plt.bar(x + width, DeepWalk, width=width, label='DeepWalk', hatch='///',edgecolor = 'k',color='white')
plt.bar(x + 2 * width, LINE, width=width, label='LINE', hatch='|||',edgecolor = 'k',color='white')
plt.bar(x + 3 * width, Node2Vec, width=width, label='Node2Vec', hatch='+++',edgecolor = 'k',color='white')
plt.bar(x + 4 * width, AANE, width=width, label='AANE', hatch='\\\\\\',edgecolor = 'k',color='white')
plt.bar(x + 5 * width, AWBA, width=width, label='AWBA', hatch='ooo',edgecolor = 'k',color='white')
plt.bar(x + 6 * width, Ours, width=width, label='Ours', hatch='xxx',edgecolor = 'k',color='white')
plt.xticks(np.arange(2), ['Citeseer', 'BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=7, labelspacing=0.5, frameon=False)  # 添加图例
# plt.legend(loc='upper left',frameon=False)
plt.ylabel('ARI')
plt.savefig('D:\CodeData\PaperCode\image\Algorithm-ARI',dpi=300)
plt.show()'''
'''# 导入数据
x = np.arange(2)
Louvain = [0.353, 0.330]
DeepWalk = [0.453, 0.417]
LINE = [0.314, 0.393]
Node2Vec = [0.473, 0.350]
AANE = [0.433,0.481]
AWBA = [0.535, 0.436]
Ours = [0.599, 0.675]
# 设置所需参数
total_width, n = 0.8, 7  # （柱状图的默认宽度值为 0.8）
width = total_width / n
x = x - (total_width - width) / 2  # 现在的x是每个并列柱的第一柱的中心横坐标
# 绘制图
plt.bar(x, Louvain,  width=width, label='Louvain', hatch='***', edgecolor = 'k',color='white')
plt.bar(x + width, DeepWalk, width=width, label='DeepWalk', hatch='///',edgecolor = 'k',color='white')
plt.bar(x + 2 * width, LINE, width=width, label='LINE', hatch='|||',edgecolor = 'k',color='white')
plt.bar(x + 3 * width, Node2Vec, width=width, label='Node2Vec', hatch='+++',edgecolor = 'k',color='white')
plt.bar(x + 4 * width, AANE, width=width, label='AANE', hatch='\\\\\\',edgecolor = 'k',color='white')
plt.bar(x + 5 * width, AWBA, width=width, label='AWBA', hatch='ooo',edgecolor = 'k',color='white')
plt.bar(x + 6 * width, Ours, width=width, label='Ours', hatch='xxx',edgecolor = 'k',color='white')
plt.xticks(np.arange(2), ['Citeseer', 'BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=7, labelspacing=0.5,frameon=False)  # 添加图例
# plt.legend(loc='upper left',frameon=False)
plt.ylabel('ACC')
plt.savefig('D:\CodeData\PaperCode\image\Algorithm-ACC',dpi=300)
plt.show()'''

# X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\Blog_emb')
# plt.scatter(X4[:,0],X4[:,1],marker='.',cmap='Paired',label='Ours')
# # X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\DW_Blog')
# # plt.scatter(X3[:,0],X3[:,1],marker='.',cmap='Paired',label='Ours')
# plt.show()
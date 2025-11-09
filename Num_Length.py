import numpy as np
import matplotlib.pyplot as plt  # 导入所需库
plt.rc('font', family='Times New Roman')



'''x = np.arange(2)
NMI=[0.327,0.291]
ARI=[0.296,0.267]
ACC=[0.599,0.561]
# 设置所需参数
total_width, n = 0.8, 6  # （柱状图的默认宽度值为 0.8）
width = total_width / n
x = x - (total_width - width) / 6  # 现在的x是每个并列柱的第一柱的中心横坐标
# 绘制图
plt.bar(x, NMI,  width=width, label='RWACD', edgecolor = 'k',color='red')
plt.bar(x + width, ARI, width=width, label='Fixed',edgecolor = 'k',color='green')

plt.xticks(np.arange(2), ['NMI', 'ARI','ACC'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=3, handletextpad=0.1, frameon=False)  # 添加图例
# plt.legend(loc='upper left',frameon=False)
# plt.ylabel('Citeseer')
# plt.savefig('D:\CodeData\PaperCode\image\Algorithm-NMI',dpi=300)
plt.show()'''


'''x = ['NMI', 'ARI', 'ACC']
y1 = [0.327, 0.296, 0.599]
y2 = [0.291, 0.267, 0.561]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='Fixed')

plt.xlabel('Citeseer')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length_Citeseer',dpi=300)
plt.savefig("D:\Thesis\\result\\Num_Length_Cite.svg", dpi=300,format="svg")
plt.show()'''
x = ['NMI', 'ARI', 'ACC']
y1 = [0.523, 0.413, 0.675]
y2 = [0.493, 0.361, 0.644]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='Fixed')

plt.xlabel('BlogCatalog')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length_BlogCatalog',dpi=300)
plt.savefig("D:\Thesis\\result\\Num_Length_Blog.svg", dpi=300,format="svg")
plt.show()

'''fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,2,1)
x = ['NMI', 'ARI', 'ACC']
y1 = [0.327, 0.296, 0.599]
y2 = [0.291, 0.267, 0.561]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='RWACD-Fixed')

plt.xlabel('Citeseer')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)

plt.subplot(1,2,2)
x = ['NMI', 'ARI', 'ACC']
y1 = [0.523, 0.413, 0.675]
y2 = [0.493, 0.361, 0.644]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='RWACD-Fixed')

plt.xlabel('BlogCatalog')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length',dpi=300)
# plt.savefig("D:\Research Direction\Paper\SVG\\Num_Length_Blog.svg", dpi=300,format="svg")
# plt.show()'''

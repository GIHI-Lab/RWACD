import numpy as np
import matplotlib.pyplot as plt  # 导入所需库
#消融实验
plt.rc('font', family='Times New Roman')

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,2,1)
x = ['NMI', 'ARI', 'ACC']
y1=[0.290,0.271,0.557]
y2 = [0.291, 0.267, 0.561]
y3=[0.312,0.283,0.575]
y4 = [0.327, 0.296, 0.599]

bar_width = 0.2
opacity = 0.8

plt.bar(x, y1, bar_width, alpha=opacity, color='lightblue', label='RWACD-Non')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, alpha=opacity, color='pink', label='RWACD-Fixed')
plt.bar([i + 2 * bar_width for i in range(len(x))], y3, bar_width, alpha=opacity, color='blue', label='RWACD-W')
plt.bar([i + 3 * bar_width for i in range(len(x))], y4, bar_width, alpha=opacity, color='red', label='RWACD')

plt.xlabel('Citeseer')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
# plt.xticks([i + bar_width/4 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)

plt.subplot(1,2,2)
x = ['NMI', 'ARI', 'ACC']
y1 = [0.490, 0.397, 0.635]
y2 = [0.493, 0.361, 0.644]
y3=[0.500,0.405,0.667]
y4 = [0.523, 0.413, 0.675]

bar_width = 0.2
opacity = 0.8

plt.bar(x, y1, bar_width, alpha=opacity, color='lightblue', label='RWACD-Non')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, alpha=opacity, color='pink', label='RWACD-Fixed')
plt.bar([i + 2 * bar_width for i in range(len(x))], y3, bar_width, alpha=opacity, color='blue', label='RWACD-W')
plt.bar([i + 3 * bar_width for i in range(len(x))], y4, bar_width, alpha=opacity, color='red', label='RWACD')

plt.xlabel('BlogCatalog')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
# plt.xticks([i + bar_width/4 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length',dpi=300)
# plt.savefig('D:\Research Direction\Paper\SVG\study.svg',dpi=300,format="svg")
plt.show()

'''import numpy as np
import matplotlib.pyplot as plt  # 导入所需库


fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,2,1)
x = ['NMI', 'ARI', 'ACC']

y2 = [0.291, 0.267, 0.561]
y3=[0.312,0.283,0.575]
y4 = [0.327, 0.296, 0.599]

bar_width = 0.2
opacity = 0.8

plt.bar(x, y2, bar_width, alpha=opacity, color='lightblue', label='RWACD-Fixed')
plt.bar([i + bar_width for i in range(len(x))], y3, bar_width, alpha=opacity, color='pink', label='RWACD-W')
plt.bar([i + 2 * bar_width for i in range(len(x))], y4, bar_width, alpha=opacity, color='blue', label='RWACD')


plt.xlabel('Citeseer')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
# plt.xticks([i + bar_width/4 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)

plt.subplot(1,2,2)
x = ['NMI', 'ARI', 'ACC']

y2 = [0.493, 0.361, 0.644]
y3=[0.500,0.405,0.667]
y4 = [0.523, 0.413, 0.675]

bar_width = 0.2
opacity = 0.8

plt.bar(x, y2, bar_width, alpha=opacity, color='lightblue', label='RWACD-Fixed')
plt.bar([i + bar_width for i in range(len(x))], y3, bar_width, alpha=opacity, color='pink', label='RWACD-W')
plt.bar([i + 2 * bar_width for i in range(len(x))], y4, bar_width, alpha=opacity, color='blue', label='RWACD')


plt.xlabel('BlogCatalog')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
# plt.xticks([i + bar_width/3 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length',dpi=300)
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,2,1)
x = ['NMI', 'ARI', 'ACC']
y1 = [0.327, 0.296, 0.599]
y2 = [0.312,0.283,0.575]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='RWACD-W')

plt.xlabel('Citeseer')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)

plt.subplot(1,2,2)
x = ['NMI', 'ARI', 'ACC']
y1 = [0.523, 0.413, 0.675]
y2 = [0.500,0.405,0.667]

bar_width = 0.35
plt.bar(x, y1, bar_width, color='lightblue', label='RWACD')
plt.bar([i + bar_width for i in range(len(x))], y2, bar_width, color='pink', label='RWACD-W')

plt.xlabel('BlogCatalog')
# plt.ylabel('Value')
# plt.title('Comparison of Companies')
plt.xticks([i + bar_width/2 for i in range(len(x))], x)
plt.legend(loc='upper left',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\\Num_Length',dpi=300)
plt.show()'''
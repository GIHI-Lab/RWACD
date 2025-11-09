import numpy as np
import matplotlib.pyplot as plt

'''#α-NMI
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('NMI')
plt.savefig('D:\CodeData\PaperCode\image\α-NMI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)
plt.show()'''

'''#α-ARI
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('ARI')
plt.savefig('D:\CodeData\PaperCode\image\α-ARI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)
plt.show()'''


'''#α-ACC
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('ACC')
plt.savefig('D:\CodeData\PaperCode\image\α-ACC',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)
plt.show()'''

'''#β-NMI
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.315, 0.320, 0.321, 0.326, 0.325, 0.308, 0.327, 0.313, 0.322, 0.314, 0.320]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.506, 0.514, 0.505, 0.503, 0.508, 0.501, 0.505, 0.523, 0.494, 0.496, 0.502]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('NMI')
plt.savefig('D:\CodeData\PaperCode\image\β-NMI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])

# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)

plt.show()'''

'''#β-ARI
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.277, 0.286, 0.290, 0.294, 0.291, 0.269, 0.296, 0.280, 0.287, 0.286, 0.294]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.375, 0.371, 0.376, 0.372, 0.380, 0.367, 0.372, 0.413, 0.360, 0.370, 0.375]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('ARI')
plt.savefig('D:\CodeData\PaperCode\image\β-ARI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)

plt.show()'''

'''#β-ACC
# plt.figure(dpi=200)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.579, 0.578, 0.593, 0.586, 0.585, 0.572, 0.599, 0.576, 0.582, 0.582, 0.590]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.653, 0.652, 0.653, 0.651, 0.654, 0.650, 0.651, 0.675, 0.641, 0.648, 0.654]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('ACC')
plt.savefig('D:\CodeData\PaperCode\image\β-ACC',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)

plt.show()'''


'''#d-NMI
x = [16,32, 64, 128, 256, 512]
cite_y = [0.275, 0.293, 0.294, 0.327, 0.308, 0.327]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.495, 0.498, 0.506, 0.513, 0.492, 0.523]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('d')
plt.ylabel('NMI')
plt.savefig('D:\CodeData\PaperCode\image\d-NMI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)

plt.show()'''

'''#d-ARI
x = [16,32, 64, 128, 256, 512]
cite_y = [0.254, 0.293, 0.294, 0.296, 0.273, 0.293]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.400, 0.387, 0.385, 0.381, 0.363, 0.413]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('d')
plt.ylabel('ARI')
plt.savefig('D:\CodeData\PaperCode\image\d-ARI',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)

plt.show()'''

'''#d-ACC
x = [16,32, 64, 128, 256, 512]
# plt.xticks(np.arange(6),[16,32, 64, 128, 256, 512])
cite_y = [0.555, 0.566, 0.563, 0.599, 0.575, 0.586]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='*', color = 'blue' )
blog_y = [0.665, 0.658, 0.658, 0.655, 0.642, 0.675]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('d')
plt.ylabel('ACC')
plt.savefig('D:\CodeData\PaperCode\image\d-ACC',dpi=300)
# plt.legend(['citeseer','BlogCatalog'])
# 将图例置于当前坐标轴下
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=2, frameon=False)

plt.show()'''


'''x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058]
ax1.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202]
ax1.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax1.set_xlabel('α')
ax1.set_ylabel('NMI')

cite_y = [0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021]
ax2.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136]
ax2.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax2.set_xlabel('α')
ax2.set_ylabel('ARI')

cite_y = [0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290]
ax3.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389]
ax3.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax3.set_xlabel('α')
ax3.set_ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)
plt.show()'''

'''x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.315, 0.320, 0.321, 0.326, 0.325, 0.308, 0.327, 0.313, 0.322, 0.314, 0.320]
ax1.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.506, 0.514, 0.505, 0.503, 0.508, 0.501, 0.505, 0.523, 0.494, 0.496, 0.502]
ax1.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax1.set_xlabel('β')
ax1.set_ylabel('NMI')

cite_y = [0.277, 0.286, 0.290, 0.294, 0.291, 0.269, 0.296, 0.280, 0.287, 0.286, 0.294]
ax2.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.375, 0.371, 0.376, 0.372, 0.380, 0.367, 0.372, 0.413, 0.360, 0.370, 0.375]
ax2.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax2.set_xlabel('β')
ax2.set_ylabel('ARI')

cite_y = [0.579, 0.578, 0.593, 0.586, 0.585, 0.572, 0.599, 0.576, 0.582, 0.582, 0.590]
ax3.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.653, 0.652, 0.653, 0.651, 0.654, 0.650, 0.651, 0.675, 0.641, 0.648, 0.654]
ax3.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
ax3.set_xlabel('β')
ax3.set_ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          fancybox=True, shadow=True, ncol=5, frameon=False)
plt.show()'''

x = [16,32, 64, 128, 256, 512]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
plt.ylim(0,1)
x = [16,32, 64, 128, 256, 512]
cite_y = [0.275, 0.293, 0.294, 0.327, 0.308, 0.327]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.495, 0.498, 0.506, 0.513, 0.492, 0.523]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
# plt.plot(x, cite_y, label='Citeseer', linestyle='-',  color = 'blue' )
# blog_y = [0.495, 0.498, 0.506, 0.513, 0.492, 0.523]
# plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', color = 'green' )
plt.xlabel('d')
plt.ylabel('NMI')

plt.subplot(1,3,2)
plt.ylim(0,1)
cite_y = [0.254, 0.293, 0.294, 0.296, 0.273, 0.293]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.400, 0.387, 0.385, 0.381, 0.363, 0.413]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('d')
plt.ylabel('ARI')


plt.subplot(1,3,3)
plt.ylim(0,1)
cite_y = [0.555, 0.566, 0.563, 0.599, 0.575, 0.586]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.665, 0.658, 0.658, 0.655, 0.642, 0.675]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('d')
plt.ylabel('ACC')


# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
#           fancybox=True, shadow=True, ncol=2, frameon=False)
plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=2, frameon=False)
plt.savefig("D:\Research Direction\Paper\SVG\d-BC1.svg", dpi=300,format="svg")
# plt.show()

'''x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0,1)
cite_y = [0.315, 0.320, 0.321, 0.326, 0.325, 0.308, 0.327, 0.313, 0.322, 0.314, 0.320]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.506, 0.514, 0.505, 0.503, 0.508, 0.501, 0.505, 0.523, 0.494, 0.496, 0.502]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('NMI')

plt.subplot(1,3,2)
plt.ylim(0,1)
cite_y = [0.277, 0.286, 0.290, 0.294, 0.291, 0.269, 0.296, 0.280, 0.287, 0.286, 0.294]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.375, 0.371, 0.376, 0.372, 0.380, 0.367, 0.372, 0.413, 0.360, 0.370, 0.375]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('ARI')


plt.subplot(1,3,3)
plt.ylim(0,1)
cite_y = [0.579, 0.578, 0.593, 0.586, 0.585, 0.572, 0.599, 0.576, 0.582, 0.582, 0.590]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
blog_y = [0.653, 0.652, 0.653, 0.651, 0.654, 0.650, 0.651, 0.675, 0.641, 0.648, 0.654]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('β')
plt.ylabel('ACC')


# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
#           fancybox=True, shadow=True, ncol=2, frameon=False)
plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=2, frameon=False)
plt.savefig("D:\Research Direction\Paper\SVG\β-BC1.svg", dpi=300,format="svg")'''
# plt.show()
'''x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cite_y = [0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
plt.ylim(0,1)
blog_y = [0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('NMI')

plt.subplot(1,3,2)
cite_y = [0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
plt.ylim(0,1)
blog_y = [0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('ARI')


plt.subplot(1,3,3)
cite_y = [0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290]
plt.plot(x, cite_y, label='Citeseer', linestyle='-', marker='o', color = 'blue' )
plt.ylim(0,1)
blog_y = [0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389]
plt.plot(x, blog_y, label='BlogCatalog', linestyle='-', marker='v', color = 'green' )
plt.xlabel('α')
plt.ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=2, frameon=False)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
#           fancybox=True, shadow=True, ncol=2, frameon=False)
plt.savefig("D:\Research Direction\Paper\SVG\α-BC1.svg", dpi=300,format="svg")'''

# plt.show()



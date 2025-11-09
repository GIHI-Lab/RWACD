'''from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(50,2)
kmeans = KMeans(n_clusters=3,random_state=0).fit(X)
print(type(kmeans))
labels = kmeans.labels_
print(labels)

fig,ax = plt.subplots(figsize=(8,6))
scatter = ax.scatter(X[:,0],X[:,1],s=10,marker='.',c = labels,cmap='Paired')


plt.show()
'''
import random

import networkx as nx
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

plt.rc('font', family='Times New Roman')

'''X1 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\AWBA_citeseer')
X1 = X1[:,1:]
X2 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\\N2V_citeseer')
X2 = X2[:,1:]
X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\DW_citeseer')

X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\citeseer_emb')

#可视化
kmeans1 = KMeans(n_clusters=6,random_state=0).fit(X1)
labels1 = kmeans1.labels_
emb1 = TSNE(n_components=2,n_iter=1000).fit_transform(X1)

kmeans2 = KMeans(n_clusters=6,random_state=0).fit(X2)
labels2 = kmeans2.labels_
emb2 = TSNE(n_components=2,n_iter=1000).fit_transform(X2)

kmeans3 = KMeans(n_clusters=6,random_state=0).fit(X3)
labels3 = kmeans3.labels_
emb3 = TSNE(n_components=2,n_iter=1000).fit_transform(X3)

kmeans4 = KMeans(n_clusters=6,random_state=0).fit(X4)
labels4 = kmeans4.labels_
emb4 = TSNE(n_components=2,n_iter=1000).fit_transform(X4)


fig = plt.figure(figsize=(22, 22), dpi=100)

# ax1, ax2, ax3, ax4 = fig.subplots(2,2,sharey=True)
plt.subplot(2,2,1)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels1]
plt.scatter(emb1[:,0],emb1[:,1],marker='.',s=5,c=labels1,cmap='Paired',label='AWBA')
plt.legend(loc='upper left',frameon=False)
plt.subplot(2,2,2)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels2]
plt.scatter(emb2[:,0],emb2[:,1],marker='.',s=5,c=labels2,cmap='Paired',label='Node2Vec')
plt.legend(loc='upper left',frameon=False)
plt.subplot(2,2,3)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels3]
plt.scatter(emb3[:,0],emb3[:,1],marker='.',s=5,c=labels3,cmap='Paired',label='DeepWalk')
plt.legend(loc='upper left',frameon=False)
plt.subplot(2,2,4)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels4]
plt.scatter(emb4[:,0],emb4[:,1],marker='.',s=5,c=labels4,cmap='Paired',label='Ours')
plt.legend(loc='upper left',frameon=False)
plt.savefig('D:\CodeData\PaperCode\image\citeseer_visual_new',dpi=300)



plt.show()'''

'''X1 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\AWBA_Blog')
X1 = X1[:,1:]
X2 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\\N2V_Blog')
X2 = X2[:,1:]
X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\DW_Blog')

X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\Blog_emb')

#可视化
kmeans1 = KMeans(n_clusters=6,random_state=0).fit(X1)
labels1 = kmeans1.labels_
emb1 = TSNE(n_components=2,n_iter=1000).fit_transform(X1)

kmeans2 = KMeans(n_clusters=6,random_state=0).fit(X2)
labels2 = kmeans2.labels_
emb2 = TSNE(n_components=2,n_iter=1000).fit_transform(X2)

kmeans3 = KMeans(n_clusters=6,random_state=0).fit(X3)
labels3 = kmeans3.labels_
emb3 = TSNE(n_components=2,n_iter=1000).fit_transform(X3)

kmeans4 = KMeans(n_clusters=6,random_state=0).fit(X4)
labels4 = kmeans4.labels_
emb4 = TSNE(n_components=2,n_iter=1000).fit_transform(X4)


fig = plt.figure(figsize=(22, 22), dpi=100)

# ax1, ax2, ax3, ax4 = fig.subplots(2,2,sharey=True)
plt.subplot(2,2,1)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels1]
plt.scatter(emb1[:,0],emb1[:,1],marker='.',s=5,c=labels1,cmap='Paired',label='AWBA')
plt.legend(loc='upper right',frameon=False)
plt.subplot(2,2,2)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels2]
plt.scatter(emb2[:,0],emb2[:,1],marker='.',s=5,c=labels2,cmap='Paired',label='Node2Vec')
plt.legend(loc='upper right',frameon=False)
plt.subplot(2,2,3)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels3]
plt.scatter(emb3[:,0],emb3[:,1],marker='.',s=5,c=labels3,cmap='Paired',label='DeepWalk')
plt.legend(loc='upper right',frameon=False)
plt.subplot(2,2,4)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels4]
plt.scatter(emb4[:,0],emb4[:,1],marker='.',s=5,c=labels4,cmap='Paired',label='Ours')
plt.legend(loc='upper right',frameon=False)
plt.savefig('D:\CodeData\PaperCode\image\Blog_visual_new_r',dpi=300)
plt.show()'''

# X1 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\AWBA_Blog')
# X1 = X1[:,1:]
X2 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\\N2V_Blog')
X2 = X2[:,1:]
X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\DW_Blog')

X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\Blog_emb')

#可视化
# kmeans1 = KMeans(n_clusters=6,random_state=0).fit(X1)
# labels1 = kmeans1.labels_
# emb1 = TSNE(n_components=2,n_iter=1000).fit_transform(X1)

kmeans2 = KMeans(n_clusters=6,random_state=0).fit(X2)
labels2 = kmeans2.labels_
emb2 = TSNE(n_components=2,n_iter=1000).fit_transform(X2)

kmeans3 = KMeans(n_clusters=6,random_state=0).fit(X3)
labels3 = kmeans3.labels_
emb3 = TSNE(n_components=2,n_iter=1000).fit_transform(X3)

kmeans4 = KMeans(n_clusters=6,random_state=0).fit(X4)
labels4 = kmeans4.labels_
emb4 = TSNE(n_components=2,n_iter=1000).fit_transform(X4)


fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3, ax4 = fig.subplots(2,2,sharey=True)
# plt.subplot(2,2,1)
# # shapes = ['.','o','*','d','s','h']
# # marker = [shapes[i] for i in labels1]
# plt.scatter(emb1[:,0],emb1[:,1],marker='.',s=5,c=labels1,cmap='Paired',label='AWBA')
# plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,1)
plt.xlim(-70,70)
plt.ylim(-70,70)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels2]
plt.scatter(emb2[:,0],emb2[:,1],marker='.',s=5,c=labels2,cmap='Paired',label='Node2Vec')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,2)
plt.xlim(-70,70)
plt.ylim(-70,70)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels3]
plt.scatter(emb3[:,0],emb3[:,1],marker='.',s=5,c=labels3,cmap='Paired',label='DeepWalk')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,3)
plt.xlim(-70,70)
plt.ylim(-70,70)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels4]
plt.scatter(emb4[:,0],emb4[:,1],marker='.',s=5,c=labels4,cmap='Paired',label='RWACD')
plt.legend(loc='upper right',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\Blog_visual_new_r3',dpi=300)
plt.savefig("D:\Thesis\\result\\Visualization_Blog_11.svg", dpi=300,format="svg")

plt.show()

'''# X1 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\AWBA_Blog')
# X1 = X1[:,1:]
X2 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\\N2V_citeseer')
X2 = X2[:,1:]
X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\DW_citeseer')

X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\citeseer_emb')

#可视化
# kmeans1 = KMeans(n_clusters=6,random_state=0).fit(X1)
# labels1 = kmeans1.labels_
# emb1 = TSNE(n_components=2,n_iter=1000).fit_transform(X1)

kmeans2 = KMeans(n_clusters=6,random_state=0).fit(X2)
labels2 = kmeans2.labels_
emb2 = TSNE(n_components=2,n_iter=1000).fit_transform(X2)

kmeans3 = KMeans(n_clusters=6,random_state=0).fit(X3)
labels3 = kmeans3.labels_
emb3 = TSNE(n_components=2,n_iter=1000).fit_transform(X3)

kmeans4 = KMeans(n_clusters=6,random_state=0).fit(X4)
labels4 = kmeans4.labels_
emb4 = TSNE(n_components=2,n_iter=1000).fit_transform(X4)


fig = plt.figure(figsize=(22, 5), dpi=100)


# ax1, ax2, ax3, ax4 = fig.subplots(2,2,sharey=True)
# plt.subplot(2,2,1)
# # shapes = ['.','o','*','d','s','h']
# # marker = [shapes[i] for i in labels1]
# plt.scatter(emb1[:,0],emb1[:,1],marker='.',s=5,c=labels1,cmap='Paired',label='AWBA')
# plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,1)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels2]
plt.scatter(emb2[:,0],emb2[:,1],marker='.',s=5,c=labels2,cmap='Paired',label='Node2Vec')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,2)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels3]
plt.scatter(emb3[:,0],emb3[:,1],marker='.',s=5,c=labels3,cmap='Paired',label='DeepWalk')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,3)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels4]
plt.scatter(emb4[:,0],emb4[:,1],marker='.',s=5,c=labels4,cmap='Paired',label='RWACD')
plt.legend(loc='upper right',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\citeseer_visual_new_r3',dpi=300)
plt.savefig("D:\Thesis\\result\\Visualization_Cite_4.svg", dpi=300,format="svg")

plt.show()'''

'''#LFR

X2 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\\LFR_NV_2000_0.7')
X2 = X2[:,1:]
X3 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\LFR_DW_2000_0.7')

X4 = np.loadtxt('D:\CodeData\PaperCode\\visual_emb\LFR_2000_0.7')

"""
1000 19
2000 50
"""

kmeans2 = KMeans(n_clusters=19,random_state=0).fit(X2)
labels2 = kmeans2.labels_
emb2 = TSNE(n_components=2,n_iter=1000).fit_transform(X2)

kmeans3 = KMeans(n_clusters=19,random_state=0).fit(X3)
labels3 = kmeans3.labels_
emb3 = TSNE(n_components=2,n_iter=1000).fit_transform(X3)

kmeans4 = KMeans(n_clusters=19,random_state=0).fit(X4)
labels4 = kmeans4.labels_
emb4 = TSNE(n_components=2,n_iter=1000).fit_transform(X4)


fig = plt.figure(figsize=(22, 5), dpi=100)


# ax1, ax2, ax3, ax4 = fig.subplots(2,2,sharey=True)
# plt.subplot(2,2,1)
# # shapes = ['.','o','*','d','s','h']
# # marker = [shapes[i] for i in labels1]
# plt.scatter(emb1[:,0],emb1[:,1],marker='.',s=5,c=labels1,cmap='Paired',label='AWBA')
# plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,1)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels2]
plt.scatter(emb2[:,0],emb2[:,1],marker='.',s=5,c=labels2,cmap='Paired',label='Node2Vec')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,2)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels3]
plt.scatter(emb3[:,0],emb3[:,1],marker='.',s=5,c=labels3,cmap='Paired',label='DeepWalk')
plt.legend(loc='upper right',frameon=False)
plt.subplot(1,3,3)
plt.xlim(-80,80)
plt.ylim(-80,80)
# shapes = ['.','o','*','d','s','h']
# marker = [shapes[i] for i in labels4]
plt.scatter(emb4[:,0],emb4[:,1],marker='.',s=5,c=labels4,cmap='Paired',label='RWACD')
plt.legend(loc='upper right',frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\citeseer_visual_new_r3',dpi=300)
plt.savefig("D:\Thesis\\result\\Visualization_LFR2000_0.7_4.svg", dpi=300,format="svg")

plt.show()'''
def get_everynodedegree(G):
    node_degree = []
    for node in sorted([int(node) for node in G.nodes()]):
        node_degree.append(nx.degree(G,str(node)))
    return node_degree

def get_attrdegree(atrr):
    attr_degree = np.sum(atrr,axis=1)
    return list(attr_degree)

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
    for node in nodes:
        num_walks = num_walks_list[int(node)]
        if node in in_nodes:
            for i in range(num_walks):
                walks.append(get_randomwalk(G=G,start_node=node,walk_length_list=walk_length_list,Lmax=Lmax,transition_matrix=nodes_transition_inside))
        else:
            for i in range(num_walks):
                walks.append(get_randomwalk(G=G,start_node=node,walk_length_list=walk_length_list,Lmax=Lmax,transition_matrix=nodes_transition_boundary))
    return walks

walks = get_totalwalks(walk_length_list=walk_length_list, num_walks_list=num_walks_list, Lmax=Lmax, G=G, nodes=nodes, nodes_transition_inside=nodes_transition_inside, nodes_transition_boundary=nodes_transition_boundary)
# print(walks)
print(len(walks))
model = Word2Vec(walks, vector_size=128, window=5, min_count=0, sg=1, workers=8, epochs=4)
X = model.wv.vectors
res = KMeans(n_clusters=6).fit_predict(X)

for i in range(n):
    for i in range(num):
        for i in range(length):
            walk.append
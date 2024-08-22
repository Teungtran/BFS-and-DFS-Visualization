import matplotlib.pyplot as plt
import networkx as nx
import queue
import time

def bfs(graph, start_node):
    # đã được duyệt
    closed = set()
    
    # sẽ được duyệt
    fringe = queue.Queue()
    fringe.put(start_node)
    
    # list
    order = []
    
    # xây mô hình
    while not fringe.empty():
        # đỉnh(vertex)
        vertex = fringe.get()
        if vertex  not in closed:
            order.append(vertex)
            closed.add(vertex)
            for node in graph[vertex]:
                if node not in closed:
                    fringe.put(node)
    return order
                    
                    
def dfs(graph, start_node, closed = None):
    if closed is None:
        closed = set()
        
    order =[]
    
    if start_node not in closed:
        order.append(start_node)
        closed.add(start_node)
        for node in graph[start_node]:
            if node not in closed:
                # mô hình thác nước ( dfs after dfs after dfs and so on)
                order.extend(dfs(graph, node, closed))
    return order
# tham khảo
# visualization
def visual_search(order, title, G, pos):
    plt.figure(figsize = (13,8), dpi =100)
    plt.title(title)
    for i, node in enumerate(order, start = 1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels = True, 
                node_color = ['r' if n == node else 'blue' for n in G.nodes])
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(1)
    
# biểu đồ (graph)
G = nx.Graph()
# tuples (nối các nodes với nhau)
G.add_edges_from([('A', 'B'),('A', 'C'),('B', 'D'),('B', 'E'), ('C', 'F'), ('C', 'G')])
pos = nx.spring_layout(G)

visual_search(bfs(G, 'A'), 'BFS visual', G, pos) # biểu đồ cho BFS
visual_search(dfs(G, 'A'), 'DFS visual', G, pos) # biểu đồ cho DFS

        
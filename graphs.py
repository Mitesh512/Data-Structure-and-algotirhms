import queue


# Creating Graphs from the input links
def generate_default_dict_graph(adj_list):
    from collections import defaultdict
    graph = defaultdict(list)
    for ls in adj_list:
        u,v = ls
        graph[u].append(v)
        graph[v].append(u)
    return graph

def generate_graph(adj_list):
    graph = {}
    for ls in adj_list:
        u,v = ls
        if graph.get(u):
            graph[u].append(v)
        else:
            graph[u] = [v]

        if graph.get(v):
            graph[v].append(u)
        else:
            graph[v] = [u]
    return graph 
    
def BFS(graph,starting_node):
    """ 
    Steps in graph:
    what you need:
    Traversal Array,
    Queue
    has_visited_arr
    In BFS, we start with a “starting” node, mark it as visited, and push it into the queue data structure.
    In every iteration, we pop out the node ‘v’ and put it in the solution vector, as we are traversing this node.
    All the unvisited adjacent nodes from ‘v’ are visited next and are pushed into the queue. The list of adjacent neighbors of the node can be accessed from the adjacency list.
    Repeat steps 2 and 3 until the queue becomes empty, and this way you can easily traverse all the nodes in the graph.
    """

    # initialize the params for the BFS
    q = queue.Queue() # put and get operation
    vis_arr = set()
    traversal_arr = []
    vis_arr.add(starting_node)
    q.put(starting_node)

    while q.qsize() > 0:        
        nd = q.get()
        traversal_arr.append(nd)
        for nbr in graph[nd]:
            if nbr not in vis_arr:
                q.put(nbr)
                vis_arr.add(nbr)

    return traversal_arr

def BFS_all_without_starting_node(graph):
    visited = set()
    traversal_arr = []
    for nd in graph.keys():
        if nd not in visited:
            comp_arr = []
            q = queue.Queue()
            if len(graph[nd])>0:
                q.put(nd)

            while q.qsize() > 0:
                curr_nd = q.get()
                if curr_nd not in visited:
                    comp_arr.append(curr_nd)
                    visited.add(curr_nd)
                    for v in graph[curr_nd]:
                        if v not in visited:
                            q.put(v)
            if len(comp_arr) > 0:
                traversal_arr.extend(comp_arr)
    return traversal_arr

def BFS_all(graph, starting_node):
    visited = set()
    traversal_arr = []
    q = queue.Queue()
    q.put(starting_node)
    visited.add(starting_node)
    
    while q.qsize() >0:
        curr_nd = q.get()
        traversal_arr.append(curr_nd)
        for v in graph[curr_nd]:
            if v not in visited:
                q.put(v)
                visited.add(v)
    
    for nd in graph.keys():
        if nd not in visited:
            if len(graph[nd])>0:
                q.put(nd)
                visited.add(nd)
                while q.qsize()>0:
                    curr_v = q.get()
                    traversal_arr.append(curr_v)

                    for nbr in graph[curr_v]:
                        if nbr not in visited:
                            q.put(nbr)
                            visited.add(nbr)

    return traversal_arr

# DFS Depth First Search
def DFS(graph, start_node,visited,traversal_arr):
    """ 
    create  
    visited_arr = []
    traversal_arr = []
    
    In DFS, we start with a node ‘v’, mark it as visited and store it in the solution vector. 
    It is unexplored as its adjacent nodes are not visited.
    
    We run through all the adjacent nodes, and call the recursive dfs function to explore the node ‘v’ which has not been visited previously. 
    This leads to the exploration of another node ‘u’ which is its adjacent node and is not visited. 
    
    The adjacency list stores the list of neighbours for any node. Pick the neighbour list of node ‘v’ and run a for loop on the 
    list of neighbours (say nodes ‘u’ and ‘w’ are in the list). We go in-depth with each node. When node ‘u’ is explored completely 
    then it backtracks and explores node ‘w’.
    
    This traversal terminates when all the nodes are completely explored. 
    """
    visited.add(start_node)
    traversal_arr.append(start_node)

    for nbr in graph[start_node]:
        if nbr not in visited:
            DFS(graph,nbr,visited,traversal_arr)

    return visited,traversal_arr


def DFS_all(graph,startig_node):

    visited, traversal_arr = DFS(graph, startig_node,set(),[])

    for nd in graph.keys():
        if nd not in visited:
            visited,traversal_arr = DFS(graph, nd,visited,traversal_arr)
    
    return traversal_arr


def dfs(graph,nd,visited,comp):
	visited.add(nd)
	comp.append(nd)
	for nbr in graph[nd]:

		if nbr not in visited:
			dfs(graph,nbr,visited,comp)

	return	comp,visited

def get_dfs_traversal(graph):
	components = []
	visited = set()
	for nd in graph.keys():
		if nd not in visited:
			comp = []
			comp, visited = dfs(graph,nd,visited,comp)
			components.append(comp)
	return components



if __name__ == '__main__':
    graph_list = [(1, 7), (1, 3), (1, 2), (2, 3), (5, 6), (6, 8) ]
    # graph_list = [(1,2),(1,3),(2,4),(3,4),(3,5),(4,5)] 
    graph = generate_graph(graph_list)
    traversal_arr = BFS(graph, starting_node=1)
    traversal_arr

    test = get_dfs_traversal(graph)


    traversal_arr = DFS_all(graph,1)
    traversal_arr


    pass
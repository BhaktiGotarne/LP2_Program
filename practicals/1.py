# Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]                

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
# The code you provided implements Prim's algorithm in Python for finding the minimum spanning tree of a graph. Prim's algorithm starts with an initial node and repeatedly adds the edge with the smallest weight that connects a selected node to an unselected node until all nodes are selected or connected.

# Here's a breakdown of the code:

# - `INF` is set to a large value to represent infinity. It is used to initialize the minimum weight variable.
# - `N` represents the number of vertices in the graph. In this case, it is set to 5.
# - `G` is the adjacency matrix representation of the graph. It represents the weights of the edges between the vertices.
# - `selected_node` is a list that keeps track of whether a node is selected or not. Initially, all nodes are marked as unselected (False).
# - `no_edge` keeps track of the number of edges in the minimum spanning tree. It is initialized to 0.
# - The first node (0) is marked as selected by setting `selected_node[0] = True`.
# - The code then enters a loop until `no_edge` reaches `N - 1` (the number of edges in a minimum spanning tree with `N` vertices).
# - Inside the loop, the minimum weight is initialized to infinity, and variables `a` and `b` are set to 0.
# - Two nested loops iterate over the selected and unselected nodes to find the edge with the smallest weight. If an unselected node is connected to a selected node and the weight is smaller than the current minimum, it updates the minimum weight and stores the indices of the nodes.
# - After finding the minimum weight edge, it prints the edge and its weight.
# - The selected node `b` is marked as selected (`selected_node[b] = True`).
# - The `no_edge` counter is incremented.
# - The loop continues until `no_edge` reaches `N - 1`, finding the remaining edges of the minimum spanning tree.

# Note: The code assumes that the graph is connected, meaning there is a path between every pair of vertices. If the graph is not connected, this code may not find a minimum spanning tree.

# If you have any specific questions or need further clarification, feel free to ask!
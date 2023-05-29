# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node,end = " ")
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# def bfs(visited,graph,node,queue):
#     visited.add(node)
#     queue.append(node)

#     while queue:
#         s = queue.pop(0)
#         print(s,end = " ")
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def main():
#     visited1 = set() # TO keep track of DFS visited nodes
#     visited2 = set() # TO keep track of BFS visited nodes
#     queue = []       # For BFS
#     n = int(input("Enter number of nodes : "))
#     graph = dict()

#     for i in range(1,n+1):
#         edges = int(input("Enter number of edges for node {} : ".format(i)))    
#         graph[i] = list()
#         for j in range(1,edges+1):
#             node = int(input("Enter edge {}  for node {} : ".format(j,i)))
#             graph[i].append(node)

#     print("The following is DFS")
#     dfs(visited1, graph, 1)
#     print()
#     print("The following is BFS")
#     bfs(visited2, graph, 1, queue)

# if __name__=="__main__":
#     main()


    # graph = {
    #     '1' : ['2','3'],
    #     '2' : ['4', '5'],
    #     '3' : ['6','7'],
    #     '4' : [],
    #     '5' : [],
    #     '6' : [],
    #     '7' : []
    #     DFS : 1 2 4 5 3 6 7 
    #     BFS : 1 2 3 4 5 6 7 
    # }


# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node,end=" ")
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited,graph,neighbour)
# def bfs(visited,graph,node,queue):
#     visited.add(node)
#     queue.append(node)
#     while queue:
#         s=queue.pop(0)
#         print(s,end=" ")
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
# def main():
#     visited1 = set()
#     visited2 = set()
#     queue = []
#     n= int(input("Enter number of nodes:"))
#     graph = dict()

#     for i in range(1,n+1):
#         edges = int(input("Enter number of edges for node {}:".format(i)))
#         graph[i]=list()
#         for j in range(1,edges+1):
#             node = int(input("Enter edge {} for node {}:".format(j,i)))
#             graph[i].append(node)




# def main():
#     visited1 = set() # TO keep track of DFS visited nodes
#     visited2 = set() # TO keep track of BFS visited nodes
#     queue = []       # For BFS
#     n = int(input("Enter number of nodes : "))
#     graph = dict()

#     for i in range(1,n+1):
#         edges = int(input("Enter number of edges for node {} : ".format(i)))    
#         graph[i] = list()
#         for j in range(1,edges+1):
#             node = int(input("Enter edge {}  for node {} : ".format(j,i)))
#             graph[i].append(node)

#     print("The following is DFS")
#     dfs(visited1, graph, 1)
#     print()
#     print("The following is BFS")
#     bfs(visited2, graph, 1, queue)

# if __name__=="__main__":
#     main()
 
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
def main():
    visited1=set()
    visited2=set()
    queue=[]
    n=int(input("Enter number of nodes:"))
    graph=dict()
    for i in range(1,n+1):
        edges=int(input("the number of egdes for node {}:".format(i)))
        graph[i]=list()
        for j in range(1,edges+1):
           node=int(input("Enter number of edge {} for node {} :".format(j,i)))
           graph[i].append(node)
    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)

if __name__=="__main__":
    main()




# The code you provided is an implementation of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms on a graph. Here's how it works:

# 1. The `dfs` function implements the DFS algorithm. It takes the `visited` set, `graph`, and `node` as parameters.
# 2. If the `node` is not in the `visited` set, it prints the `node`, adds it to the `visited` set, and recursively calls the `dfs` function for each neighbor of the `node`.
# 3. The `bfs` function implements the BFS algorithm. It takes the `visited` set, `graph`, `node`, and `queue` as parameters.
# 4. It adds the `node` to the `visited` set and appends it to the `queue`.
# 5. While the `queue` is not empty, it dequeues the first element `s` from the `queue`, prints it, and iterates over its neighbors.
# 6. If a neighbor is not in the `visited` set, it adds it to the `visited` set and enqueues it in the `queue`.
# 7. The `main` function is the entry point of the program.
# 8. It prompts the user to enter the number of nodes in the graph (`n`).
# 9. It creates an empty `graph` dictionary to store the edges.
# 10. It iterates over the nodes from 1 to `n` and prompts the user to enter the number of edges for each node.
# 11. For each edge, it prompts the user to enter the connected node and appends it to the corresponding node's list in the `graph` dictionary.
# 12. After creating the graph, it initializes empty sets for `visited1` and `visited2`, and an empty `queue`.
# 13. It calls the `dfs` function with the starting node `1` and prints the result.
# 14. It calls the `bfs` function with the starting node `1` and prints the result.

# To use this code, you need to run it and follow the prompts to input the number of nodes and edges for each node. Then, it will display the result of DFS and BFS traversals on the graph.

# Let me know if you have any further questions!
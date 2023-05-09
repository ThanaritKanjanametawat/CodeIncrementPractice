#Time used: 3 Hours 2 Minutes
import time
n, k = list(map(int,input().split()))
S = list(map(int,input().split()))
S = list(enumerate(S,start=1))
T = input()

def DFS(adj_list, node, visited, depth):
    visited[node] = True
    max_depth = depth

    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            max_depth = max(max_depth, DFS(adj_list, adj_node, visited, depth + 1))

    visited[node] = False
    return max_depth

def find_max_depth(adj_list, root):
    visited = {node: False for node in adj_list}

    return DFS(adj_list, root, visited, 1)

def Spiderman(n, k, S, T):
    # Transform Input into a graph
    adj_list = {}
    for i in range(n):
        adj_nodes = []
        # Check for Tramboline
        if T[i] == "T":
            adj_nodes = S.copy()
            del adj_nodes[i]
        else:
            # Check if left is travesable
            if i-1 in range(n) and S[i-1][1] <= S[i][1]:
                adj_nodes.append(S[i-1])

            # Check if right is travesable
            if i+1 in range(n) and S[i+1][1] <= S[i][1]:
                adj_nodes.append(S[i+1])

        adj_list[S[i]] = adj_nodes


    root = None
    for node in adj_list:
        if node[0] == k:
            root = node

    print(find_max_depth(adj_list, root))


st = time.process_time()
Spiderman(n, k, S, T)
et = time.process_time()
print(f"Running Time: {et-st}")
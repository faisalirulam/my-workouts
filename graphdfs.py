graph={"A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":[],
        "F":[]
        }
visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
    
        for i in graph[node]:
            dfs(visited,graph,i)

dfs(visited,graph,"A")



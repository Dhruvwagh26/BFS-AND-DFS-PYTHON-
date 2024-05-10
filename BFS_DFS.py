**************Depth First Search*******************************************

def recursive_dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            recursive_dfs(visited, graph, neighbour)
            

if (__name__ == "__main__"):
    visited = set()
    graph = {
        'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]
    }
    recursive_dfs(visited, graph, 'A')


*****************************************************************************

**********************Breadth First Search***********************************
import collections
def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    
    while(queue):
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)
    
if (__name__ == "__main__"):
    #Dictionary
    graph  = {0:[1,2,3],1:[0,2],2:[3,4],3:[0,2],4:[2]}
    bfs(graph, 0)  #root = 0


***********OR *****************
# Define the graph as a dictionary where the keys are nodes and the values are lists of connected nodes.
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Create an empty list to keep track of visited nodes during BFS.
visited = []

# Create an empty queue to keep track of nodes to visit during BFS.
queue = []

# Define the BFS function that takes a starting node as an argument.
def bfs(visited, graph, node):
    # Add the starting node to visited and queue.
    visited.append(node)
    queue.append(node)
    
    # While there are still nodes in the queue, process the first node in the queue.
    while queue:
        # Remove the first node from the queue and process it.
        m = queue.pop(0)
        print(m, end=' ')
        
        # For each neighbor of the current node, if it has not been visited, add it to visited and queue.
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Print a message to the console and call the BFS function with the starting node.
print('Following is the Breadth-First Search')
bfs(visited, graph, '3')

import heapq
from collections import deque

def dijkstra(graph, start_node):
    """
    Shortest-path distances from start_node on a weighted graph with non-negative weights.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    pq = [(0, start_node)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def bfs(graph, start_node):
    """
    Breadth-First Search (unweighted shortest levels).
    Returns (order, distances) where:
      - order: list of nodes in the order visited
      - distances: dict of hop-count distance from start_node
    """
    visited = set()
    order = []
    distances = {start_node: 0}
    q = deque([start_node])

    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node].keys():
            if neighbor not in visited and neighbor not in q:
                distances[neighbor] = distances[node] + 1
                q.append(neighbor)
    return order, distances

def dfs(graph, start_node):
    """
    Depth-First Search (iterative).
    Returns list of nodes in the order visited.
    """
    visited = set()
    order = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Push neighbors in reverse to get a stable left-to-right feel
        neighbors = list(graph[node].keys())
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                stack.append(neighbor)
    return order

# Example Usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

start_node = 'A'
print("Dijkstra from A:", dijkstra(graph, start_node))

bfs_order, bfs_dist = bfs(graph, start_node)
print("BFS order from A:", bfs_order)
print("BFS hop distances from A:", bfs_dist)

dfs_order = dfs(graph, start_node)
print("DFS order from A:", dfs_order)

start_node_2 = 'B'
print("Dijkstra from B:", dijkstra(graph, start_node_2))
bfs_order_2, bfs_dist_2 = bfs(graph, start_node_2)
print("BFS order from B:", bfs_order_2)
print("BFS hop distances from B:", bfs_dist_2)
dfs_order_2 = dfs(graph, start_node_2)
print("DFS order from B:", dfs_order_2)

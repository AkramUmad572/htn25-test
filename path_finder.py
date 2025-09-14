import heapq

def dummy_heuristic(n1, n2):
    return 0  # reduces A* to Dijkstra

def astar(graph, start_node, goal_node, heuristic):
    """
    A* Search Algorithm.
    
    Args:
        graph (dict): adjacency dict like {node: {neighbor: weight, ...}, ...}
        start_node: starting node
        goal_node: target node
        heuristic (func): h(n) -> estimated cost from n to goal

    Returns:
        (path, cost) where:
          - path: list of nodes from start to goal
          - cost: total path cost (g-score)
    """
    # g-scores (actual distance so far)
    g_score = {node: float('infinity') for node in graph}
    g_score[start_node] = 0

    # f-scores (g + heuristic)
    f_score = {node: float('infinity') for node in graph}
    f_score[start_node] = heuristic(start_node, goal_node)

    # priority queue (f-score, node)
    pq = [(f_score[start_node], start_node)]
    came_from = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal_node:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_node)
            return path[::-1], g_score[goal_node]

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal_node)
                heapq.heappush(pq, (f_score[neighbor], neighbor))

    return None, float('infinity')  # no path found

def dijkstra(graph, start_node):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start_node.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                      and values are dictionaries of neighbors with their weights.
                      Example: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2}}
        start_node: The starting node for finding shortest paths.

    Returns:
        dict: A dictionary containing the shortest distances from the start_node
              to all other reachable nodes.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we've already found a shorter path to this node, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update and add to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

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
shortest_distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {shortest_distances}")

path, cost = astar(graph, 'A', 'F', dummy_heuristic)
print("A* path from A to F:", path, "with cost:", cost)

start_node_2 = 'B'
print("Dijkstra from B:", dijkstra(graph, start_node_2))
bfs_order_2, bfs_dist_2 = bfs(graph, start_node_2)
print("BFS order from B:", bfs_order_2)
print("BFS hop distances from B:", bfs_dist_2)
dfs_order_2 = dfs(graph, start_node_2)
print("DFS order from B:", dfs_order_2)

print("usage: bfs dfs or dijstra")

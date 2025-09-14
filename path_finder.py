import heapq

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

start_node_2 = 'B'
print("Dijkstra from B:", dijkstra(graph, start_node_2))
bfs_order_2, bfs_dist_2 = bfs(graph, start_node_2)
print("BFS order from B:", bfs_order_2)
print("BFS hop distances from B:", bfs_dist_2)
dfs_order_2 = dfs(graph, start_node_2)
print("DFS order from B:", dfs_order_2)

print("usage: bfs dfs or dijstra")

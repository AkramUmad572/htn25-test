# Graph Traversal Algorithms: `path_finder` Module

This module provides functions for traversing graphs using different algorithms.

## Dijkstra's Algorithm

The `dijkstra(graph, start_node)` function implements Dijkstra's algorithm to find the shortest paths from a given `start_node` in a weighted graph with non-negative weights.

### Parameters

* `graph (dict)`: A dictionary representing the graph where keys are nodes and values are dictionaries of neighbors with their weights.  Example: `{'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2}}`
* `start_node`: The starting node.

### Returns

* `dict`: A dictionary containing the shortest distances from the `start_node` to all other reachable nodes.

## Breadth-First Search (BFS)

The `bfs(graph, start_node)` function performs a Breadth-First Search, finding the shortest paths in terms of number of hops (unweighted).

### Parameters

* `graph (dict)`: Same as Dijkstra's.
* `start_node`: The starting node.

### Returns

* `tuple`: A tuple containing:
    * `order (list)`: List of nodes visited in BFS order.
    * `distances (dict)`: Dictionary of hop-count distances from `start_node`.

## Depth-First Search (DFS)

The `dfs(graph, start_node)` function performs a Depth-First Search.

### Parameters

* `graph (dict)`: Same as Dijkstra's.
* `start_node`: The starting node.

### Returns

* `list`: List of nodes visited in DFS order.

## Examples

```python
import path_finder
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'E': 3},
    'D': {'B': 2, 'F': 5},
    'E': {'C': 3, 'F': 2},
    'F': {'D': 5, 'E': 2}
}

start_node = 'A'
print("Dijkstra from A:", path_finder.dijkstra(graph, start_node))
bfs_order, bfs_dist = path_finder.bfs(graph, start_node)
print("BFS order from A:", bfs_order)
print("BFS hop distances from A:", bfs_dist)
dfs_order = path_finder.dfs(graph, start_node)
print("DFS order from A:", dfs_order)
```
# Graph Traversal Algorithms

This module provides functions for traversing graphs using three common algorithms: Depth-First Search (DFS), Breadth-First Search (BFS), and Dijkstra's algorithm.

## Dijkstra's Algorithm

Finds the shortest paths from a single source node to all other reachable nodes in a weighted graph.

```python
def dijkstra(graph, start_node):
    # ... implementation details ...
    return shortest_distances
```

**Parameters:**

* `graph`: A dictionary representing the graph where keys are nodes and values are dictionaries of neighbors with associated edge weights.
* `start_node`: The starting node for the search.

**Returns:**

A dictionary of shortest distances from the `start_node` to all other reachable nodes.

## Breadth-First Search (BFS)

Explores a graph level by level, finding the shortest path in an unweighted graph.

```python
def bfs(graph, start_node):
    # ... implementation details ...
    return bfs_order, bfs_distances
```

**Parameters:**

* `graph`: A dictionary representing the graph.
* `start_node`: The starting node.

**Returns:**

* `bfs_order`: A list of nodes visited in BFS order.
* `bfs_distances`: A dictionary of hop distances from the `start_node` to each reachable node.

## Depth-First Search (DFS)

Explores a graph by going as deep as possible along each branch before backtracking.

```python
def dfs(graph, start_node):
    # ... implementation details ...
    return dfs_order
```

**Parameters:**

* `graph`: A dictionary representing the graph.
* `start_node`: The starting node.

**Returns:**

A list of nodes visited in DFS order.

## Usage Example

```python
from path_finder import dijkstra, bfs, dfs

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'E': 3},
    'D': {'B': 5, 'F': 2},
    'E': {'C': 3, 'F': 4},
    'F': {'D': 2, 'E': 4}
}

print("Dijkstra from A:", dijkstra(graph, 'A'))
bfs_order, bfs_dist = bfs(graph, 'A')
print("BFS order from A:", bfs_order)
print("BFS hop distances from A:", bfs_dist)
dfs_order = dfs(graph, 'A')
print("DFS order from A:", dfs_order)
```
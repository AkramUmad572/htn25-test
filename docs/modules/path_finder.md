# Path Finder Module

## Overview

This module provides functions for graph traversal and pathfinding.

The graph is expected to be an adjacency list represented as a dictionary. Example:

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4},
    'D': {'B': 2}
}
```

---

## Dijkstra's Algorithm

Finds the shortest path in a **weighted graph** with non-negative edge weights.

### Function
`dijkstra(graph, start_node)`

### Parameters
- `graph` (dict): An adjacency list where keys are nodes and values are dictionaries of neighbors with their weights.
- `start_node`: The node from which to calculate shortest paths.

### Returns
- (dict): A dictionary mapping each reachable node to its shortest distance from `start_node`.

### Example
```python
shortest_distances = dijkstra(graph, 'A')
# Returns: {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': infinity}
```

---

## Breadth-First Search (BFS)

Finds the shortest path in an **unweighted graph** by traversing level by level. It is useful for finding the minimum number of hops between nodes.

### Function
`bfs(graph, start_node)`

### Parameters
- `graph` (dict): An adjacency list. Edge weights are ignored.
- `start_node`: The node to start the search from.

### Returns
- A tuple `(order, distances)`:
  - `order` (list): A list of nodes in the order they were visited.
  - `distances` (dict): A dictionary mapping each reachable node to its hop count from `start_node`.

### Example
```python
order, distances = bfs(graph, 'A')
# order -> ['A', 'B', 'C', 'D']
# distances -> {'A': 0, 'B': 1, 'C': 1, 'D': 2}
```

---

## Depth-First Search (DFS)

Traverses a graph by exploring as far as possible along each branch before backtracking. Useful for topological sorting, cycle detection, or simply visiting all nodes.

### Function
`dfs(graph, start_node)`

### Parameters
- `graph` (dict): An adjacency list. Edge weights are ignored.
- `start_node`: The node to start the search from.

### Returns
- (list): A list of nodes in the order they were visited.

### Example
```python
order = dfs(graph, 'A')
# Returns: ['A', 'B', 'D', 'C']
```
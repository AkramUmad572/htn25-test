# Pathfinding Algorithms

## A* Search

The A* search algorithm is now available for finding optimal paths in a graph.

### `astar(graph, start_node, goal_node, heuristic)`

**Overview:** This function implements the A* search algorithm to find the shortest path between a start and goal node in a graph.

**When to use:** Use A* when you need to find the shortest path in a graph, and you have a heuristic function that estimates the distance from any node to the goal.

**Parameters:**

* `graph (dict)`: An adjacency dictionary representing the graph.  Keys are nodes, and values are dictionaries where keys are neighbors and values are edge weights.
* `start_node`: The starting node.
* `goal_node`: The target node.
* `heuristic (func)`: A function that estimates the cost from a node to the goal node.  The function should take two nodes as input and return a non-negative number.

**Returns:**

* `(path, cost)`: A tuple containing the shortest path (list of nodes) and its total cost. Returns `(None, float('infinity'))` if no path is found.

**Example:**

```python
import heapq

def dummy_heuristic(n1, n2):
    return 0  # reduces A* to Dijkstra

def astar(graph, start_node, goal_node, heuristic):
    # ... (A* implementation from PR) ...

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'E': 3},
    'D': {'B': 2, 'F': 5},
    'E': {'C': 3, 'F': 2},
    'F': {'D': 5, 'E': 2}
}

path, cost = astar(graph, 'A', 'F', dummy_heuristic)
print("A* path from A to F:", path, "with cost:", cost)
```

## Greedy Technique
- In a greedy solution, we go for the best possible choice at each step of the algorithm.
- Because we are not considering future scenarios (and are only concerned with the best choice at each step), a greedy solution might not be the most effective solution for the problem.
- To decide whether or not to use a greedy approach for a particular problem, try to think whether or not the greedy technique will work for all the future steps of the algorithm.

### Dijkstras Algorithm - O(n^2)
```
1. Create a result dictionary. At the end of the program, result will have the shortest distance (value) for all nodes (key) in the graph. For our example, it will become as {'A': 0, 'B': 5, 'C': 3, 'D': 2, 'F': 6, 'E': 4}

2. Start with the source node. Distance from source to source itself is 0.

3. The distance to all other nodes from the source is unknown initially, therefore set the initial distance to infinity.

4. Create a set unvisited containing nodes that have not been visited. Initially, it will have all nodes of the graph.

5. Create a path dictionary that keeps track of the previous node (value) that can lead to the current node (key). At the end of the program, for our example, it will become as {'B': 'A', 'C': 'D', 'D': 'A', 'F': 'C', 'E': 'C'}.

6. As long as unvisited is non-empty, repeat the following:

- Find the unvisited node having smallest known distance from the source node.

- For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.

- If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.

- If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.

- Remove the current node from the unvisited set.
```

#### Implementation
```python
import sys
def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = {}
    result[source] = 0                 
    
    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize
            
    unvisited = set(graph.nodes)  
    
    path = {}
   
    # As long as unvisited is non-empty
    while unvisited: 
        min_node = None
        
        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:
                
                if min_node is None:       
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break
            
        current_distance = result[min_node]
        
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]
        
                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance
                    
                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node
            
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result
```

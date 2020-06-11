from heapq import heappush, heappop

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)
    
    visited = [False for _ in range(len(graph) + 1)]
    
    min_heap = [(0, 1)]
    total_cost = 0
    
    while len(min_heap) > 0:
        
        cost, current_island = heappop(min_heap)
        
        if visited[current_island]:
            continue
        
        total_cost += cost
        
        for neighbour, edge_cost in graph[current_island]:
            heappush(min_heap, (edge_cost, neighbour))
            
        visited[current_island] = True
        
    return total_cost

def create_graph(num_islands, bridge_config):
    graph = [list() for _ in range(num_islands + 1)]
    
    for edge in bridge_config:
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))
    
    return graph

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
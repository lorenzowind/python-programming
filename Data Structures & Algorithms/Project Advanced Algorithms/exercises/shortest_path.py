from math import sqrt
from heapq import heappop, heappush

def shortest_path(M, start, goal):
    """ Calculate the heuristic distance from the goal to all vertex and search the optimal path using A* algorithm.
    
    INPUT:
    M: Object of Map Class. Contains the intersections and roads.
    start: Integer. The initial vertex of the path.
    goal: Integer. The final vertex of the path.
    
    OUTPUT:
    Integers List or String message. Represents the shortest path from start to goal, a message of invalid arguments or a message of non-existent path.
    """
    if not is_valid(M, start, goal):
        return "Invalid arguments."
    
    heuristic_distance = find_heuristic_distance(M.intersections, goal)
    
    return find_shortest_path(M, start, goal, heuristic_distance)

def is_valid(M, start, goal):
    """ Verify if the start and goal vertex exists on the Map.
    
    INPUT:
    M: Object of Map Class. Contains the intersections and roads.
    start: Integer. The initial vertex of the path.
    goal: Integer. The final vertex of the path.
   
    OUTPUT:
    Boolean. Is True if the start and goal vertex exists on the Map, and False if they don't exist.
    """
    length = len(M.intersections)
    
    if 0 <= start <= length and 0 <= goal <= length:
        return True
    
    return False
    
def find_heuristic_distance(intersections, goal):
    """ Calculate the heuristic distance from the goal to all vertex, following the Euclidian formula.
    
    INPUT:
    intersections: Dictionary. Contains the x and y position of all vertex.
    goal: Integer. The final vertex of the path.
    
    OUTPUT:
    Dictionary. Contains the heuristic distance from the goal to all vertex.
    """
    goal_intersection = intersections[goal]
    
    heuristic_distance = {}
    
    for index, intersection in intersections.items():
        heuristic_distance[index] = calculate_distance(goal_intersection, intersection)
        
    return heuristic_distance
        
def calculate_distance(initial_vertex, final_vertex):
    """ Calculate the distance from an initial to a final vertex following the Euclidian formula.
    
    INPUT:
    initial_vertex: Float Tuple. The initial vertex position (x and y axis).
    final_vertex: Float Tuple. The final vertex position (x and y axis).
    
    OUTPUT:
    Float. The distance from an initial to a final vertex.
        
    """
    x_axis = (initial_vertex[0] - final_vertex[0]) ** 2
    y_axis = (initial_vertex[1] - final_vertex[1]) ** 2
    
    return sqrt(x_axis + y_axis)

def find_shortest_path(M, start, goal, heuristic_distance):
    """ Search the optimal path using A* algorithm.
    
    INPUT:
    M: Object of Map Class. Contains the intersections and roads.
    start: Integer. The initial vertex of the path.
    goal: Integer. The final vertex of the path.
    heuristic_distance: Dictionary. Contains the heuristic distance from the goal to all vertex.
    
    OUTPUT:
    Integers list or String message. Represents the shortest path from start to goal or a message of non-existent path.
    """
    min_heap = [(0.0, start)]
    
    open_list = {}
    closed_list = {}
    
    open_list[start] = None
    closed_list[start] = 0.0
    
    while len(min_heap):
        current_vertex = heappop(min_heap)[1]
        
        if current_vertex == goal:
            break
            
        for neighbour in M.roads[current_vertex]:
            distance_to_neighbour = calculate_distance(M.intersections[current_vertex], M.intersections[neighbour])
            
            current_distance = closed_list[current_vertex] + distance_to_neighbour
            
            if neighbour not in closed_list or current_distance < closed_list[neighbour]:
                closed_list[neighbour] = current_distance
                accumulated_distance = current_distance + heuristic_distance[neighbour]
                
                heappush(min_heap, (accumulated_distance, neighbour))
                open_list[neighbour] = current_vertex
                
    return get_path(open_list, start, goal)
    
def get_path(path, start, goal):
    """ Make an Integers List from the values and keys of a path's Dictionary. 
    
    INPUT:
    path: Dictionary. Contains the parent vertex of each one, representing the path.
    start: Integer. The initial vertex of the path.
    goal: Integer. The final vertex of the path.
    
    OUTPUT:
    Integers list or String message. Represents the shortest path from start to goal or a message of non-existent path.
    """
    if goal not in path:
        return 'Path does not exist.'
    
    new_path = [goal]
    current_vertex = goal

    if start != goal:
        while path[current_vertex] != start:
            new_path.append(path[current_vertex])
            current_vertex = path[current_vertex]

        new_path.append(path[current_vertex])

    return new_path[::-1]
## Reasoning: To implement the HTTP Router, I used the following logic:
1. Using classes with a dictionary in the main node to store each route of any path;
2. The inserting and finding operation are accessed through the Router class, which split the path with a filter lambda function to break the slashes previously;
3. Adding each part of the route and the handler in the dictionary, being able to access it:
    - The adding process consists of recursively adding all routes with a `handler not found` reference, but the last route with the informed handler;
    - The searching process is to follow all the routes by going through the dictionary keys.  

### Method `insert` (RouteTrie class)

#### Time complexity: O(h)
#### Space complexity: O(1)

### Method `find` (RouteTrie class)

#### Time complexity: O(h)
#### Space complexity: O(1)

### Method `insert` (RouteTrieNode class)

#### Time complexity: O(1)
#### Space complexity: O(1)

### Method `add_handler` (Router class)

#### Time complexity: O(n)
#### Space complexity: O(n)

### Method `lookup` (Router class)

#### Time complexity: O(n)
#### Space complexity: O(n)

### Method `split_path` (Router class)

#### Time complexity: O(1)
#### Space complexity: O(1)

## Overrall

### Time complexity: O(n)
### Space complexity: O(n)
## Reasoning: To implement the HTTP Router, I used the classes with a dictionary to store each route of any path. The inserting and finding operation are accessed through the Router class, which split the path with a filter function previously, adding each part as key in the dictionary and then being able to access it.

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
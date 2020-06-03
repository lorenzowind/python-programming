## Reasoning: To find the position of the number in the array, I first searched for the exact position of the pattern break, with that, I used two arrays to store the highest and the lowest values. And then the binary search on the specific array in which the number is included.

### Method `rotated_array_search`

#### Time complexity: O(1)
#### Space complexity: O(n)

### Method `find_rotated_point`

#### Time complexity: O(range)
#### Space complexity: O(1)

### Method `binary_search`

#### Time complexity: O(log(n))
#### Space complexity: O(1)

## Overrall

### Time complexity: O(log(n))
### Space complexity: O(n)
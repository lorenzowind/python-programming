## Reasoning: To find the minimum and maximum values of an array sorting it, I used the following logic:
1. A simple approach to find these values, just going through the array and storing in two variables;
2. To sorting, I implemented the Pigeonhole sort, considering the number of elements and the length of the range:
    - Using an array to store the value as keys, incrementing the quantity;
    - Iterating the array containing the values in order.

### Method `get_min_max`

#### Time complexity: O(n)
#### Space complexity: O(1)

### Method `pigeonhole_sort`

#### Time complexity: O(n + range)
#### Space complexity: O(n)

## Overrall

### Time complexity: O(n)
### Space complexity: O(n)
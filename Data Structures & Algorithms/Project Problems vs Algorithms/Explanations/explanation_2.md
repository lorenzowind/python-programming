## Reasoning: To find the position of the number in the array I implemented the following logic:
1. Searching for the exact position of the pattern break, going through the array starting for the first and last position at the same time, comparing them until the highest compared position is equal or lower the lowest compared position, with that finding where is possible to break in two sorted arrays;
2. Using two arrays to store the highest and the lowest sorted values and comparing the number to search with the last position of the lowest value's array, being able to use a binary search in only one array;
3. The binary search on the array in which the number is included, finding the position in that array;
4. Calculating the position difference to consider the original array, but only if the number was included in the lowest value portion or was not found - Incrementing with the break pattern position plus 1 (because the array starts with 0): `position searched + break pattern position + 1`.

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
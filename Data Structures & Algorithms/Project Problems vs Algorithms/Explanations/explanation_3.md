## Reasoning: To find the highest sums, I implemented the following logic:
1. Counting the frequency of the elements using a set and returning it as a list: `return list (set of frequencies)`
- [THIS IS AN ALTERNATIVE] Using quicksort to make it easier to find the right digits, considering that there are repeated elements;
    - Finding the pivot and calling the quicksort function recursively.
2. With the array sorted, the sums represent a pattern:
    - The length of the digits is the same if the number is even; otherwise, one of them has one more position;
    - The highest sum is found taking the elements following: `last - 2n position`; 
    - The second highest sum is similar: `last - (1 + 2n) position`.

### Method `rearrange_digits`

#### Time complexity: O(1)
#### Space complexity: O(1)

### Method `get_highest_sum`

#### Time complexity: O(n)
#### Space complexity: O(n)

### Method `get_digits`

#### Time complexity: O(1)
#### Space complexity: O(1)

### Method `count_frequencies`

#### Time complexity: O(n)
#### Space complexity: O(n)

### Method `quicksort` & `quicksort_recursive_solution` & `sort_helper`
- [THIS METHOD CAN BE USED IF THE ARRAY HAS REPEATED ELEMENTS]

#### Time complexity: O(n*log(n))
#### Space complexity: O(n)

## Overrall

### Time complexity: O(n)
### Space complexity: O(n)
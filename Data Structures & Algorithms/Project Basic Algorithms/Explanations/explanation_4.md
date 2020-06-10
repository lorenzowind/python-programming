## Reasoning: To sort the array of 0, 1 and 2, I implemented the following logic:
1. A dictionary to store the values (0, 1 and 2) as keys; 
2. Going through the whole array incrementing the value (frequency), considering the 0, 1 or 2 as the key;
3. Returning the 0, 1 and 2 times the frequencies following the order of keys: `[0] * dictionary[0] + [1] * dictionary[1] + [2] * dictionary[2]`.

### Method `sort_012`

#### Time complexity: O(n) 
#### Space complexity: O(1)

## Overrall

### Time complexity: O(n)
### Space complexity: O(1)
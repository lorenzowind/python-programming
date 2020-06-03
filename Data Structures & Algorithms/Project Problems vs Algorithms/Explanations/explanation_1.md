## Reasoning: To implement this algorithm, I used the following logic:
1. A result variable and a temporary variable to store the divisions by 2 and the previous value, repectively;
2. Comparing them in a loop and calculating the new result following a logic equation: `(result // temporary + temporary) // 2`;
3. The temporary variable receives the result value for the next repetition, and then the result approaches the floored or the exact square root.

### Method `sqrt`

#### Time complexity: O(log(n))
#### Space complexity: O(1) 

## Overrall

### Time complexity: O(log(n))
### Space complexity: O(1)
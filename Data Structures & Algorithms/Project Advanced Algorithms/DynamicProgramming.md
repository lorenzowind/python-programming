## Knapsack problem
```
- Input:
1. The items, each having its associated weight (kg) and value ($).
2. A knapsack that can hold a maximum weight of knapsack_max_weight (kg).

- Output:
Return the maximum total value of items that can be accommodated into the given knapsack.
```
### Dynamic approach
```python
# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value(knapsack_max_weight, items):
    
    # Initialize a lookup table to store the maximum value ($) 
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:
        
        # The "capcacity" represents amount of remaining capacity (kg) of knapsack at a given moment. 
        for capacity in reversed(range(knapsack_max_weight + 1)):
            
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]
```

## Longest Common Subsequence
- The Longest Common Subsequence is the longest sequence of letters that are present in both the given two strings in the same relative order.
1. An LCS need not necessarily be a contiguous substring.
2. There can be more than one LCS present in the given two strings.
3. There can be many more common subsequences present here, with smaller length.

### Implementation
```python
def lcs(string_a, string_b):
    
    # initialize the matrix 
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]
    
    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):
        
        for char_b_i, char_b in enumerate(string_b):
            
            # If there is a match, 
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
                
            # If there is not a match, 
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]
```
## Longest Palindromic Subsequence
- The Longest Palindromic Subsequence (LPS) is the most lengthy sequence of characters that is a palindrome.
1. The LPS solution algorithm depends on how the characters of a given string are related to each other.
2. For a string of length n characters, you can build an n x n matrix. The 2-D matrix will have characters of the given string on the top as well as on the left side.
3. The matrix will store the solution to smaller subproblems first, and gradually adding up more characters to the problem. In this case, a subproblem is to find the length of the LPS, up to a certain point in the string.

### Implementation
```python
# complete LPS solution
def lps(input_string): 
    n = len(input_string) 
  
    # create a lookup table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # strings of length 1 have LPS length = 1
    for i in range(n): 
        L[i][i] = 1 
    
    # consider all substrings
    for s_size in range(2, n+1): 
        for start_idx in range(n-s_size+1): 
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]); 
    
    return L[0][n-1] # value in top right corner of matrix
```

## The Coin Change Problem
```
Input: 
coins = [1, 2, 3], amount = 6

Output: 
2

Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.
```
### Implementation
```python
# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')]*(amount + 1)
    
    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0
    
    i = 0
    while (i < amount):
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i+coin] = min(res[i] + 1, res[i+coin])
        i += 1

    if res[amount] == float('inf'):
        return -1
    return res[amount]
```

## Stock Prices
```python
def max_returns(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    
    if len(arr) < 2:
        return
    
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit
```
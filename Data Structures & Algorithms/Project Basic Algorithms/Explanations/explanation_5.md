## Reasoning: To create the Trie structure, I implemented the following logic:
1. A Trie node to store the children in a dictionary;
2. The operations of inserting and finding a trie node, are simply going through the keys to find the leaf, adding or returning that node;
3. And the operation of collecting the suffixes consists of using a list to append the values which have a final word reference:
    - Using recursion to go through all the nodes following the children's keys of the root while the user writes.

### Method `insert` (TrieNode)

#### Time complexity: O(1) 
#### Space complexity: O(1)

### Method `insert` (Trie class)

#### Time complexity: O(h)
#### Space complexity: O(1)

### Method `suffixes` (TrieNode)

#### Time complexity: O(m*n)
- `m` is the number of children per Trie node
- `n` is the depth of the Trie tree
#### Space complexity: O(m*n)
- `m` is the number of letters of the word
- `n` is the number of words 

### Method `find` (Trie)

#### Time complexity: O(h)
#### Space complexity: O(1)

## Overrall

### Time complexity: O(m*n)
### Space complexity: O(m*n)
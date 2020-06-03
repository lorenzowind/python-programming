## Reasoning: To create the Trie structure, I implemented a Trie node to store the children in a dictionary. The operations of inserting and finding a trie node, are simply going through the keys to find the leaf. And the operation of collecting the suffixes consists of using a list to append the values which have a final word reference.

### Method `insert` (TrieNode)

#### Time complexity: O(1) 
#### Space complexity: O(1)

### Method `insert` (Trie class)

#### Time complexity: O(h)
#### Space complexity: O(1)

### Method `suffixes` (TrieNode)

#### Time complexity: O(n)
#### Space complexity: O(n)

### Method `find` (Trie)

#### Time complexity: O(h)
#### Space complexity: O(1)

## Overrall

### Time complexity: O(n)
### Space complexity: O(n)
## Algorithm 
- Given an unsorted list A of n numbers -> find the median of A
- Given an unsorted list A and an integer k (1<=k<=n) -> find the k(th) smallest of A

### Quicksort(A)
```
1. choose a pivot p -> How? -> the good pivot is the median

2. partition A into A<p, A=p, A>p

3. recursively sort A<p and A>p
```

### Example
```
A = [5, 2, 20, 17, 11, 13, 8, 9, 11]
p = 11

A<p = [5, 2, 8, 9]
-> if k<=4 then k(th) smallest in A<p

A=p = [11, 11]
-> if 4<=k<=6 then k(th) output p

A>p = [20, 17, 13]
-> if k>6 then k-6(th) smallest in A>p
```

### O(n) running time 
- T(n) = T(n/2) + O(n) -> T(n) = O(n)
- p = median(A) or approximated value
- n/4 <= p <= 3n/4

### A good pivot
- T(n) = T(3n/4) + O(n) = O(n)
- With slack of T(.24n): T(3n/4) + [T(n/5) + O(n)]...good pivot
- A subset S of A where the size is n/5 -> p = median(S)

### Pseudocode
```
input: unsorted A, integer k where 1 <= k <= n
output: k(th) smallest of A

1. break A into n/5 groups -> G1, G2, ..., Gn/5 [O(n)]
2. for i=1 -> n/5: sort Gi, Ni = median(Gi) [O(5!) -> O(1)/g -> O(n)]

3. S = {N1, N2, ..., Nn/5}

4. recursively: (S, n/10) [T(n/5)]

5. partition A into A<p, A=p, A>p

6. (recurse on A<p or A>p or output p) [T(3n/4)]
    6.1. if k <= |A<p| then return recursively: (A<p, k)
    6.2. if k > |A<p| + |A>p| then return recursively: (A>p, k - |A<p| + |A=p|)
    6.3. else output p

-> T(3n/4) + T(n/5) + O(n)

```

### Implementation
```python
def fastSelect(Arr, k):                         # k is an index
    n = len(Arr)                                # length of the original array
    
    if(k>0 and k <= n):                         # k should be a valid index         
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0
        
        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):                     # n//5 gives the integer quotient of the division 
            median = findMedian(Arr, 5*i, 5)    # find median of each group of size 5
            setOfMedians.append(median)         
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5*i < n): 
            median = findMedian(Arr, 5*i, n % 5)
            setOfMedians.append(median)
        
        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):            # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians)>1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))
        
        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                Arr_Less_P.append(element)
            elif (element>pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)
        
        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)
        
        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))
            
        else:
            return pivot     

# Helper function
def findMedian(Arr, start, size): 
    myList = [] 
    for i in range(start, start + size): 
        myList.append(Arr[i]) 
          
    # Sort the array  
    myList.sort() 
  
    # Return the middle element 
    return myList[size // 2] 
```

## [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- Divide the given array into three subarray w.r.t. the middle, say Left, Right, and Cross subarrays. Recurse on the Left part, and Right part untill you reach the base condition, i.e. single element in a subarray.
- Calculate the maximum sum of the Left, Right, and Cross subarrays, say L, R, and C respectively. Return the maximum of L, R, and C

### Pseudocode
```
1. if start == stop then return arr[start] [T(n)]

2. Calculate mid index [constant]

3. L = recursively (arr, start, mid) [T(n/2)]

4. R = recursively (arr, mid+1, stop) [T(n/2)]

5. C = maxSum (arr, start, mid, stop) O(n)

6. return max(C, max(L, R)) [constant]

-> T(n) = 2 * T(n/2) + O(n) = O(n*log(n))
```

### Implementation
```python
'''Helper Function - Find the max crossing sum w.r.t. middle index'''
def maxCrossingSum(arr, start, mid,  stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]                                     # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]                                  # Keep track of maximum sum
    
    # Traverse in reverse direction from (mid-1) to start 
    for i in range(mid-1, start-1, -1):                    # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum):                         # Update leftMaxSum
            leftMaxSum = leftSum
    
    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid+1]                                  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid+1]                               # Keep track of maximum sum
    
    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid+2, stop+1):                         # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum):                       # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''
    return (rightMaxSum + leftMaxSum)

'''Recursive function'''
def maxSubArrayRecursive(arr, start, stop):                # start and stop are the indices
    # Base case
    if (start==stop):
        return arr[start]

    if(start < stop):
        mid = (start+stop)//2                              # Get the middle index
        L = maxSubArrayRecursive(arr, start, mid)          # Recurse on the Left part
        R = maxSubArrayRecursive(arr, mid+1, stop)         # Recurse on the Right part
        C = maxCrossingSum(arr, start, mid, stop)          # Find the max crossing sum w.r.t. middle index
        return max(C, max(L,R))                            # Return the maximum of (L,R,C)
    
    else:                                                  # If ever start > stop. Not feasible. 
        return nums[start]

def maxSubArray(arr):
    start = 0                      # staring index of original array
    stop = len(arr) -1             # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)
```

## Summary
- Divide and Conquer approach is suitable to solve a big (scale) problem by breaking it into smaller sub-problems, where each sub-problem looks exactly similar to the original problem. In general, there are three phases:

1. Divide - Break the given problem into smaller sub-problems
2. Conquer - Solve each sub-problem using recursion. The smallest sub-problem (base case) would have a simple straightforward solution.
3. Combine - This phase will automatically execute as a part of the recursion call stack, which combines the solution of smaller sub-problems to generate the final solution.

- Quicksort and Mergesort are a few examples that follow the Divide and Conquer approach. There are a few points to note while deciding if one should go for faster Divide and Conquer approach:

1. The problem should be on a bigger scale.
2. The sub-problem must look precisely similar to the original problem in hand.
3. Use recursion to solve the problem. It means that the solution will be built for the smallest sub-problem (base case) first.
4. There is a trade-off between memory usage and speed of execution. Recursion comes with a price of extra memory usage for executing the call stack. But, if you use multi-threading, you can compute the solution even much faster.
5. In case if many sub-problems look precisely the same, then we don't want to re-execute the same again and again. In such cases, you can consider storing the results of the execution, and thus reuse them whenever required. This strategy is called Memoization (in Dynamic Programming approach).
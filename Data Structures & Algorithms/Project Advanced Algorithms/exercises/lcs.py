def lcs(string_a, string_b):
    
    matrix = [[0 for _ in range(len(string_a) + 1)] for _ in range(len(string_b) + 1)]
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
        
            if string_a[j - 1] == string_b[i - 1]:
                matrix[i][j] += matrix[i-1][j-1] + 1
            
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
            
    return matrix[-1][-1]

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
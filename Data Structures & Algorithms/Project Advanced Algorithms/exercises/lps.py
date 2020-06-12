def lps(input_string): 
    matrix = []
    
    for i in range(len(input_string)):
        matrix.append([])
        for j in range(len(input_string)):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    
    for i in range(2, len(input_string) + 1):
        for j in range(len(input_string) - i + 1):
            last_index = j + i - 1
            
            if i == 2 and input_string[j] == input_string[last_index]:
                matrix[j][last_index] = 2
    
            elif input_string[j] == input_string[last_index]:
                matrix[j][last_index] = matrix[j+1][last_index-1] + 2
            
            else:
                matrix[j][last_index] = max(matrix[j][last_index - 1], matrix[j + 1][last_index])        
            
    return matrix[0][-1]

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)
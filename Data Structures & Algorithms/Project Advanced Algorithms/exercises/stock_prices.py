def max_returns(prices):
    """
    Calculate maxiumum possible return
    
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    min_price_index, max_price_index = 0, 1
    current_min_price_index = 0
    
    for index in range(1, len(prices)):
        if prices[index] < prices[current_min_price_index]:
            current_min_price_index = index
            
        if prices[max_price_index] - prices[min_price_index] < prices[index] - prices[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    
    max_profit = prices[max_price_index] - prices[min_price_index]
    
    return max_profit

# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
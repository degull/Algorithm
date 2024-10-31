def solution(n, k):
    price_meat = 12000
    price_drink = 2000
    
    free_drinks = n//10
    
    total_cost = (n*price_meat) + ((k - free_drinks) * price_drink)
    
    return total_cost
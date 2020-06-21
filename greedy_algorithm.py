# Problem statement: Vending maching change to return

# inputs = cost of item, amount paid, denominations available

# outputs = amount to be returned, denominations to be returned


denominations_available = {
    1:'one',
    2:'two',
    5:'five',
    10:'ten',
    20:'twenty',
    50:'fifty',
    100:'hundred'
    }
denominations_available_quantity = {
    1: 1,
    2: 2,
    5: 5,
    10: 10,
    20: 20,
    50: 50,
    100: 100
    }

cost_of_item = 1
amount_paid = 100

def change_function(cost_of_item, amount_paid):

    amount_to_return = amount_paid - cost_of_item
    denominations_to_return = {key:0 for (key, value) in denominations_available.items()}

    while amount_to_return > 0:
        for denomination in reversed(sorted(denominations_available.keys())):
            if denomination <= amount_to_return or denominations_available_quantity[denomination] != 0:
                amount_to_return = amount_to_return - denomination
                denominations_to_return[denomination] += 1
                denominations_available_quantity[denomination] -= 1

    print(denominations_available_quantity)

    return denominations_to_return

if __name__ == '__main__':
    cost_of_item = 1
    amount_paid = 100
    print(change_function(cost_of_item, amount_paid)) 

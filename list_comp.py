number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]

#[expr for  item1 in  seq1 if condition]

def all_odd(number_list):
    odds = []
    [odds.append(item) for item in number_list if item %2 != 0]

    return odds
print all_odd(number_list)

def insert_value(number_list, value, index):
    number_list[index:index] = [value]

    return number_list
print insert_value(number_list, 4, 5)

def all_evens(number_list):
    evens = []
    [evens.append(item) for item in number_list if item % 2 == 0]

    return evens

print all_evens(number_list)
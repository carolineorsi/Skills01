number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

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
    # evens = []
    # [evens.append(item) for item in number_list if item % 2 == 0]
    return [item for item in number_list if item % 2 == 0]
    # return evens

print all_evens(number_list)

def uppercase_words(words):
    # ["apple", "berry"] = ["APPLE"]    s.upper()

    return [s.upper() for s in words if s.startswith("a")]

def long_words(word_list):
    

    return [word for word in word_list if len(word) >= 4]

print long_words(word_list)

def smaller(a, b):
    if a < b:
        return a
    else:
        return b



def smallest(number_list):
    # smaller = number_list[0]
    # for item in number_list:
    #     if item < smaller:
    #         smaller = item
    
    print reduce(smaller, number_list)

    # return item 

smallest(number_list)

def larger(a, b):
    if a > b:
        return a
    else:
        return b

print reduce(larger, number_list)


def halvesies(number_list):
    return [float(item)/2 for item in number_list]


print halvesies(number_list)


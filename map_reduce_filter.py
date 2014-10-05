# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.

def all_odd(number_list):
    return filter(lambda x: x % 2 == 1, number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return filter(lambda x: x % 2 == 0, number_list)

# Write a function that takes a list of strings and return a new list with all strings of length 4 or greater.
def long_words(word_list):
    return filter(lambda item: len(item) >= 4, word_list) 

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smaller = lambda a, b: a if (a < b) else b
    return reduce(smaller, number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    i = number_list[0]
    for item in number_list:
        if item > i:
            i = item
    return i


print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = []
    for item in number_list:
        new_list = new_list + [float(item) / 2]
    return new_list

print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for word in word_list:
        lengths = lengths + [len(word)]

    return lengths

print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for value in number_list:
        total = total + value
    return total

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = 1
    for value in number_list:
        total = total * value
   
    return total

print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ""
    for word in word_list:
        new_string = new_string + " " + word
    return new_string

print join_strings(word_list)

def list_length(list):
    count = 0
    for item in list:
        count += 1
    return count 

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    ave = float(sum_numbers(number_list)) / list_length(number_list)
    
    return ave

print average(number_list)


def eat_function(food_function):
    return food_function(5)

def burger(num):
    return print(num+5)

def sandwich(mult):
    return print(mult*10)

eat_function(sandwich)
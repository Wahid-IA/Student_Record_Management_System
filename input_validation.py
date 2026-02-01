#Argument for input to not be empty
def input_not_empty(type):
    while True:
        value= input(type).strip()
        if value:
            return value
        print("Input cannot be empty")

#Argument for input to be only positive integer number
def input_int(type):
    while True:
        value=input(type)
        if value.isdigit():
            return int(value)
        print("Roll must be only positive numbers.")
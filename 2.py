# Function that takes a string as a parameter 
# and returns the count of numbers and letters in it
def string_counter(string):
    letters = 0
    digits = 0
    for char in string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    return {'letters': letters, 'digits': digits}

# Another variation of the same function
def string_counter2(string):
    return {'letters': len([x for x in string if x.isalpha()]),
            'digits': len([x for x in string if x.isdigit()])}


if __name__ == '__main__':
    string_counter("hello 123")                 # --> {'digits': 3, 'letters': 5}
    string_counter2("Hello world! 123!")        # --> {'digits': 3, 'letters': 10}
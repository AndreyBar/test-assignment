# Function that takes 3 numeric parameters and returns the count of integers
# that are divisible by the third parameter in the range between two first params
def handle_numbers(num1, num2, num3):
    return len([x for x in range(num1, num2 + 1) if not x % num3])


if __name__ == '__main__':
    handle_numbers(1, 10, 2)      # --> 5
    handle_numbers(10, 18, 3)     # --> 3
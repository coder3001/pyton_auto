# 1. if number can be divided by 3 -> return 'Buzz'
# 2. if number can be divided by 5 -> return 'Fizz'
# 3. if number can be divided by 3 and 5 -> return 'FizzBuzz'
# 4. if number can NOT be divided by 3 and 5 -> return number

def fizz_buzz(input):
    # division_result = input % 3
    # if_comparision = division_result == 0
    if (input % 3 == 0 and input % 5 == 0):
        return "BuzzFizz"
    if input % 3 == 0:
        return "Buzz"
    if input % 5 == 0:
        return "Fizz"

    return input


print(fizz_buzz(15))

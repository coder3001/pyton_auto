# "LISTS"

# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# print(zeros)
# combined = zeros + letters
# print(combined)

# numbers = list(range(20))
# print(numbers)

# numbers = list(range(20))
# chars = list("Hello World")
# print(chars)
# print(len(chars))


# "ACCESSING_ITEMS"

# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0])
# print(letters[-1])
# print(letters[0:3])
# print(letters[:3])
# print(letters[0:])
# print(letters[:])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])


# "LIST_UNPACKING"


# numbers = [1, 2, 3, 4, 5, 13, 18]
# first, *other, last = numbers

# # first = numbers[0]
# # second = numbers[1]
# # third = numbers[2]

# print(first, last)
# print(other)


"LOOPING OVER LISTS"

letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

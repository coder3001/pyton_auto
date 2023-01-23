"LISTS"

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)
combined = zeros + letters
print(combined)

numbers = list(range(20))
print(numbers)

numbers = list(range(20))
chars = list("Hello World")
print(chars)
print(len(chars))


"ACCESSING_ITEMS"

letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0])
print(letters[-1])
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

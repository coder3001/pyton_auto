counter = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(f"поточне число з нашого range(1, 10):{x}")
        counter = counter + 1
 print(f"кількість принту чисел без остатку {counter}")
print(counter)

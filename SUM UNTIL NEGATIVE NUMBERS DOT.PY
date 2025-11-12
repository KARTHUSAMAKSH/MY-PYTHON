# Sum Until Negative Number
total = 0

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total += num

print("Total sum:", total)

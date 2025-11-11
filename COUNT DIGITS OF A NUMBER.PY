# Count Digits of a Number
num = int(input("Enter a number: "))

count = 0
temp = abs(num)  # handle negative numbers

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits:", count)

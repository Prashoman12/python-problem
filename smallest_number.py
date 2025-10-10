# 1.write a python program to find the smallest number from a set of numbers.
numbers = [50, 21, 32, 12, 54, 65, 10, 76, 87, 98]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)

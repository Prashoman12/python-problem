# write a program to find the second highest number from a set of numbers.
numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 20]
highest= numbers[numbers.index(max(numbers))]
second_highest = numbers[0]

for num in numbers:
    if num > second_highest and num != highest:
        second_highest = num
    elif second_highest == highest:
        second_highest = num
        highest = second_highest
    

print("Second highest number:", second_highest)
print("Highest number:", highest)

# 1.write a python program to find the sum of odd and even numbers from a set of numbers.
numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98]
even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
        even_sum += num
    else:
        print(f"{num} is odd")
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
# write a program to find the sum of all numbers between 50 and 100 which are divisible by 3 and not  divisible by 5
total_sum = 0
for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        total_sum += num
print("Sum of numbers between 50 and 100 that are divisible by 3 and not by 5:", total_sum)

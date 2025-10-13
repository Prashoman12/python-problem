num = int(input("Enter a number: "))
temp = num
count = 0
digit_sum = 0
while temp > 0:
    digit = temp % 10
    count += 1
    digit_sum += digit
    temp //= 10
print("Number of digits in", num, "is:", count)
print("Sum of digits in", num, "is:", digit_sum)
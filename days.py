total_days = int(input("Enter number of days: "))
years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7
print(f"{total_days} days is approximately {years} years, {weeks} weeks, and {days} days.")
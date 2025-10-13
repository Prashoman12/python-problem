marks = int(input("Enter marks(1-100): "))

match marks:
    case m if 80 <= m <= 100:
        grade = 'A+'
    case m if 75 <= m < 80:
        grade = 'A'
    case m if 70 <= m < 75:
        grade = 'A-'
    case m if 65 <= m < 70:
        grade = 'B+'
    case m if 60 <= m < 65:
        grade = 'B'
    case m if 55 <= m < 60:
        grade = 'B-'
    case m if 50 <= m < 55:
        grade = 'C+'
    case m if 45 <= m < 50:
        grade = 'C'
    case m if 40 <= m < 45:
        grade = 'D'
    case m if 0 <= m < 40:
        grade = 'F'
    case _:
        grade = 'Invalid'
print("Grade:", grade)
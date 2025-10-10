
size = int(input("Enter the size of the list: "))
numbers = []

for i in range(size):
    num = int(input(str(i+1) + ". Enter number: "))
    numbers.append(num)


while True:
    print("\n --------Menu--------")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Display the list")
    print("4. Exit")

    match input("Enter your choice (1-4): "):
        case "1":
            new_num = int(input("Enter a number to add: "))
            numbers.append(new_num)
            print("Number added successfully!")
        case "2":
            del_num = int(input("Enter a number to remove: "))
            if del_num in numbers:
                numbers.remove(del_num)
                print("Number removed successfully!")
            else:
                print("Number not found in the list.")
        case "3":
            for num in numbers:
                print(num)
            
        case "4":
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice! Please enter 1-4.")
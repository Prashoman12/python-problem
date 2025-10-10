# Maximum of Three Numbers

a,b,c = map(int, input("").split())

def max_of_two(x, y):
    
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    
    return max_of_two(x, max_of_two(y, z))

print("Maximun value is :", max_of_three(a, b, c))

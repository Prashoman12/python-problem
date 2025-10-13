# list=[2,4,5,6,8,9,4,3,6,7]
# count=0

# for i in range(len(list)):
#     count += list[i]
#     print(list[i])
# print(count)

# from itertools import chain

# from itertools import chain


# a1 = range(10,0,-2)
# a2 = range(30,20,-2)
# a3 = range(50,40,-2)

# final = chain(a1,a2,a3)

# print(final) #generator object

# Expected output: <itertools.chain object at 0xae6330>

print("using for loop")

for i in range(1,101):
    print(i, end=" ")
print("\n")

print("using while loop")
i=1
while i<=100:
    print(i, end=" ")
    i+=1
print("\n")

print("using do while loop")
i=1
while True:
    print(i, end=" ")
    i+=1
    if i>=101:
        break
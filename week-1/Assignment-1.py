#Create lower triangular, upper triangular and pyramid containing the "*" character.
n=int(input("Enter number of rows: "))

print("Lower Triangular Pattern:\n")
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print("\n")


print("Upper Triangular Pattern:\n")
for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    print("\n")


print("Pyramid Pattern:\n")
for i in range(n):
    k=0
    for j in range(n-i):
        print(" ",end=" ")
    
    while(k!=2*i+1):
        print("* ",end="")
        k=k+1
    print("\n")
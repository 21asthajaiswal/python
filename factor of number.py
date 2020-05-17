# Python Program to find the factors of a number
def factor_of_number(x):
    for i in range(1,x+1):
        if (x % i == 0):
            print(i)
x = int(input("enter the number="))
factor_of_number(x)

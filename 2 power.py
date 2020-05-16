# Display the powers of 2 using anonymous function
term = int(input("enter the term="))
result = list(map(lambda x: x**2,range (term)))
for i in range(term):
    print("2 raised to power",i,"is",result[i])

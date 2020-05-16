#python Program to Find Numbers Divisible by Another Number
lst = [12, 65, 54, 39, 102, 339, 221]
num = int(input('enter the number'))

result = list(filter(lambda x: (x % num == 0), lst))
print("number is divisible",result)
          
    

# Python Program to find the L.C.M. of two input number
def lcm (x,y):
    if x > y :
        greater = x
    else :
        greater = y
    while (True):
        if (greater % x == 0) and (greater % y == 0):
            result = greater
            break
        greater += 1
    return result    
x = 54
y = 24
print("lcm of numbers is =",lcm(x,y))

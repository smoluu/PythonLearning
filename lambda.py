def myFunction(num):
    return lambda a: a*num

myMultiply = myFunction(10)

print(myMultiply(10))
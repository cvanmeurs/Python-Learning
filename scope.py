

a = 10
b = 20

print("OUTER SCOPE, a is ", a)
print("OUTER SCOPE, b is ", b)

def myFunction(a):
    print("INNER SCOPE, a is", a)
    print("INNER SCOPE, b is", b)

myFunction(a)
myFunction(b)

print("OUTER SCOPE, a is ", a)
print("OUTER SCOPE, b is ", b)

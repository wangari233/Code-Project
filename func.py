x = 10    #x is a global variable

def my_func():
    
    x = 20     # x is a local variable
    print(x, end=" ")

my_func()
print(x)

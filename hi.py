def outer_func():
    msg = "Hello"     #msg is an enclosing variable
    
    def inner_func():
        nonlocal msg
        msg = "Hi"
        
    inner_func()
    print(msg)

outer_func()

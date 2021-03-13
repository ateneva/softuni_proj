
### Fix the code below, so it returns the expected output.

    def outer():
        x = "local"
    
        def inner():
            x = "nonlocal"
            print("inner:", x)
    
        def change_global():
            x = "global: changed!"
    
        print("outer:", x)
        inner()
        print("outer:", x)
        change_global()
    
    print(x)
    outer()
    print(x)


### Good Practices to make the code more readable

    x = "global"
    
    def outer():
        def inner():
            new_x = f"nonlocal{x}"
            print("inner:", new_x)
            return new_x
    
        def change_global():
            return "global: changed!"
    
        x = "local"
        print("outer:", x)
        x = inner()
        print("outer:", x)
        return change_global()
    
    
    print(x)
    x = outer()
    print(x)
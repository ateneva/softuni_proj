
### Fix the exceptions in the code below:


    numbers_list = input().split(", ")
    result = 0
    
    for i in range(numbers_list):
        number = numbers_list[i + 1]
        if number < 5:
            result *= number
        elif number > 5 and number > 10:
            result /= number
    
    print(result)


 > *input*

    > 1, 4, 5
    > 4, 5, 6, 1, 3
    > 2, 5, 10


### Fixed: 

    numbers_list = [int(i) for i in input().split(", ")]
    result = 0
    
    for i in range(len(numbers_list)):
        number = numbers_list[i] + 1
        if number < 5:
            result *= number
        elif number > 5 and number > 10:
            result /= number
    
    print(result)
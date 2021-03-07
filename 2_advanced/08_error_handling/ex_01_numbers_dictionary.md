
### You are provided with the following code: 

    numbers_dictionary = {}
    
    line = input()
    
    while line != "Search":
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    
    line = input()
    
    while line != "Remove":
        searched = line
        print(numbers_dictionary[searched])
    
    line = input()
    
    while line != "End":
        searched = line
        del numbers_dictionary[searched]
    
    print(numbers_dictionary)


* On the first several lines, until you receive the command `"Search"`, 
  you will receive on separate lines the number as text and the number as integer
  

* When you receive `"Search"` on the next several lines until you receive the command `"Remove"`, 
  you will be given the searched number as text and you need to print it on the console


* When you receive `"Remove"` on the next several lines until you receive `"End"` 
  you will be given the searched number as text and you need to remove it from the dictionary


* At the end you need to print what is left from the dictionary

There is some missing code in the solution and there are some errors that may occur. 
Complete the code so the following errors are handled:
* Passing non-integer type to the variable number
* Searching for a non-existent number
* Removing a non-existent number


Print appropriate messages when an error has occurred. 
The messages should be:
* `"The variable number must be an integer"`
* `"Number does not exist in dictionary"` - for non-existing keys

![img_1.png](img_1.png)
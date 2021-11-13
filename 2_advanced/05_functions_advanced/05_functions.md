Function Fundamentals
---------------------

![](https://t4668229.p.clickup-attachments.com/t4668229/4b1c87e3-3246-4188-9c35-3e9e653fbd20/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/3c689f1d-f7b8-4350-a6d8-1af47678f786/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/435b82a5-e036-4dce-85de-550b957f46c5/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/37312641-38ac-4583-b4aa-08a0dcf0d8c1/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/a4eb7c32-7d5f-41db-82b1-a25cde9de73c/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/370ea663-afbc-4f0c-86d5-f8f0dd7edf20/image.png)



![](https://t4668229.p.clickup-attachments.com/t4668229/a363e6fe-857a-4138-b777-f7c8718d181e/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/fde541be-a94d-4118-b53e-753b1c0c7bb0/image.png)



![](https://t4668229.p.clickup-attachments.com/t4668229/53ae5484-beeb-49b0-936d-ba18d5c39786/image.png)



![](https://t4668229.p.clickup-attachments.com/t4668229/208d8179-e5c2-498e-b798-f914249d15d6/image.png)


## Basic function problems: 
  

* [01_grades.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_01_grades.py)
* [02_calculations.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_02_calculations.py)
* [03_repeat_string.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_03_repeat_string.py)
* [04_orders.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_04_orders.py)
* [05_calculate_rectangle_area.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_05_calculate_rectangle_area.py)


* [ex_01_smallest_of_three.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_01_smallest_of_three.py)
* [ex_02_add_and_subtract.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_02_add_and_subtract.py)
* [ex_03_characters_in_range.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_03_characters_in_range.py)
* [ex_04_odd_and_even_sum.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_04_odd_and_even_sum.py)
* [ex_05_palindrome_integers.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_05_palindrome_integers.py)
* [ex_06_password_validator.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_06_password_validator.py)
* [ex_07_perfect_number.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_07_perfect_number.py)
* [ex_08_loading_bar.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_08_loading_bar.py)
* [ex_09_factorial_division.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/03_functions/03_functions_ex_09_factorial_division.py)


Advanced Functions
==================


![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4d9.png?version=6.0.0) Functions Lectures:
-----------------------------------------------------------------------------------------------------

### **Doncho**

> [_https://softuni.bg/trainings/resources/video/50323/video-04-june-2020-doncho-minkov-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/50323/video-04-june-2020-doncho-minkov-python-advanced-may-2020/2839)

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f5a5.png?version=6.0.0) Functions Exercises:
------------------------------------------------------------------------------------------------------

### **Tanya**

> [_https://softuni.bg/trainings/resources/video/50331/video-05-june-2020-tanya-staneva-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/50331/video-05-june-2020-tanya-staneva-python-advanced-may-2020/2839)



![](https://t4668229.p.clickup-attachments.com/t4668229/dd509ad3-dd05-4de7-b953-0155365678f4/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/c9ae8a71-ffd8-452a-aa66-72aa10aa0972/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/d1f9968c-6e62-4d02-bae8-f6684ec9d6e7/image.png)


![](https://paper.dropboxstatic.com/static/img/ace/emoji/2757.png?version=6.0.0)**Avoid lambdas if possible because:**

1.  they are a slow operation
2.  they may easily **render intangible repetitive code**

  

![](https://t4668229.p.clickup-attachments.com/t4668229/af42ca05-2f8e-4847-8cd8-f59bac89f67a/image.png)

  

```python
'''
Write a program that receives a list of numbers and prints their absolute value.
'''

def absolute_numbers(num_sequence):
    abs_numbers = [abs(float(n)) for n in num_sequence.split(" ")]
    return abs_numbers

print(absolute_numbers(input()))
```

```python
'''
Write a program that rounds all the given numbers.
'''

def round_numbers(num_sequence):
    return [round(float(n)) for n in num_sequence.split(" ")]

print(round_numbers(input()))
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/e768b8e9-b2c1-4118-a6b6-7b92ad42e940/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/fe63171d-8d0c-425b-89cb-46e177eb01c0/image.png)

  

```python
def args_length(*args):
    return len(args)

print(args_length(1, 32, 5))
print(args_length("john", "peter"))
```


![](https://t4668229.p.clickup-attachments.com/t4668229/6f2265ac-e712-4989-964e-6030fdbb6334/image.png)


```python
'''
Write a function called multiply that can receive any amount of numbers
as different parameters and returns the result of the multiplication of all of them.
'''

def multiply(*args):
    result = 1
    for x in args:
        result *= x
    return result
```

  

```python
'''
Write a function called operate that receives an operator(+, -, * or /)
as first argument and multiple numbers as additional arguments (*args).

The function should return the result of the operator applied to all the numbers. 
'''

def operate(operator, *args):
    def get_starting_value(operator):
        if operator in ('+', '-'):
            return 0
        else:
            return 1

    result = get_starting_value(operator)

    for x in args:
        if operator == '+':
            result += x

        elif operator == '-':
            result -= x

        elif operator == '*':
            result *= x

        else:
            result /= x
    return result
```


![](https://t4668229.p.clickup-attachments.com/t4668229/67e1f4c8-eef1-4bca-af39-4a196d585b1f/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/a3431bbf-0936-45c4-b5be-dcb7c112f5ee/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/243efb4d-9b0d-4a6a-8ac1-d3eaa46e0f4e/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/c0b3e803-b307-42a5-b144-f2f5f5d3d0d4/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/73b93ded-5cc7-4c30-bfc3-7099b3d70cd4/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/1fabefc4-1e8f-4b86-bf23-4f5c148677ce/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/647ecdcc-5256-4dc7-ab00-35c9ae61bed4/image.png)

  

```python
def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
```


```python
def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he " 
           f"is {kwargs.get('age')} years old"
```


![](https://t4668229.p.clickup-attachments.com/t4668229/6ad7b500-1934-40ec-8e5e-66c707acea7f/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/88483f1a-ee7d-417c-a84b-83afb288f90b/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/8cb31f91-bbca-4516-8c1e-6357f26a6182/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/b40303eb-ebba-4968-9359-e18a484a8b38/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/4a250e48-8dd9-4e71-97db-90238b4407cc/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/d8f8af96-920a-47cd-8cd7-b7f727b7d724/image.png)

  

```python
# calculate factoriel

def fact(n):
    if n == 0:
        return 1    # base case

    return n * fact(n-1)    # recursive call

print(fact(4))
```

### Advanced functions problems: 

* [01_absolute_values.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_01_absolute_values.py)
* [02_rounded_numbers.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_02_rounded_numbers.py)
* [03_multiplication_function.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_03_multiplication_function.py)
* [04_operate.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_04_operate.py)
* [05_person_info.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_05_person_info.py)

* [01_even_numbers.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_01_even_numbers.py)
* [02_sort.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_02_sort.py)
* [03_min_max_and_sum.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_03_min_max_and_sum.py)
* [04_negative_vs_positive.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_04_negative_vs_positive.py)
* [05_odd_or_even.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_05_odd_or_even.py)
* [06_even_or_odd.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_06_even_or_odd.py)
* [07_concatenate.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_07_concatenate.py)
* [08_function_executor.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_08_function_executor.py)
* [09_keyword_arguments_length.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/05_functions_advanced/05_functions_adv_ex_09_keyword_arguments_length.py)


Best Practices for writing functions
====================================

*   How to document your code so that others can easily understand it.
*   How to create functions that are easier to test, debug, and change.
*   How to setup default arguments in functions so that your code doesn't behave unexpectedly.


### ✅ Document your code so that others can easily understand it

With a **docstring** though, it is much easier to tell what the expected inputs and outputs should be, as well as what the function does. A [**docstring**](https://en.wikipedia.org/wiki/Docstring) is a string written as the first line of a function. Because docstrings usually span multiple lines, they are enclosed in triple quotes, Python's way of writing multi-line strings:


Every docstring has some (although usually not all) of these five key pieces of information:

1.  Description of what the function does.
2.  Description of the arguments, if any.
3.  Description of the return value(s), if any.
4.  Description of errors raised, if any.
5.  Optional extra notes or examples of usage.

  

```python
def split_and_stack(df, new_names):
    """Splits a DataFrame's columns into two halves and then stack
    them vertically, returning a new DataFrame with `new_names` as the
    column names.

    Args:
      df (DataFrame): The DataFrame to split.
      new_names (iterable of str): The column names for the new DataFrame.

    Returns:
      DataFrame
    """
    half = int(len(df.columns) / 2)
    left = df.iloc[:, :half]
    right = df.iloc[:, half:]
    return pd.DataFrame(
      data=np.vstack([left.values, right.values]),
      columns=new_names
    )
```

Docstrings makes it easier for you and other **data scientists or engineers to use, read, and maintain your code in the future.**

  

🆑 **code convention** 👇

```python
def function(arg_1, arg_2=42):
    """Description of what the function does.

    Args:
      arg_1 (str): Description of arg_1 that can break onto the next line
        if needed.
      arg_2 (int, optional): Write optional when an argument has a default
        value.

    Returns:
      bool: Optional description of the return value
      Extra lines are not indented.

    Raises:
      ValueError: Include any error types that the function intentionally
        raises.

    Notes:
      See https://www.dataquest.io for more info.  
    """
```


[https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

⚠️ Remember that even though computers execute it, **code is actually written for humans to read** (otherwise you'd just be writing the 1s and 0s that the computer operates on).

  

```python
import inspect

def count_letter(content, letter):
    """Counts the number of times letter appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int
      
    Raises:
      ValueError: `letter` must be a single character string
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])

formatted_docstring = inspect.getdoc(count_letter)
print(formatted_docstring)
```


👉 using the built-in approach

```python
def the_answer():
    """Returns the answer to life, 
    the universe, and everything.

    Returns:
        int
    """
    return 42
print(the_answer.__doc__)
```


```python
Returns the answer to life, 
    the universe, and everything.

    Returns:
        int
```

  

⚠️ **Use inspect module to return the info without empty spaces and formatting**

```python
import inspect
print(inspect.getdoc(the_answer))
```

  

```python
Return the answer to life, 
the universe, and everything.

Returns:
    int
```

  

👇 🔻

```python
import inspect
raw_docstring = split_and_stack.__doc__
print(raw_docstring)

formatted_docstring = inspect.getdoc(split_and_stack)
print(formatted_docstring)
```

  

### ✅ Create functions that are easier to test, debug, and change

  

Now that we know how to make our functions easier to understand, let's look at how we can also make them easier to test, debug, and change. The [**Don't repeat yourself**](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle, also known as **DRY**, and the **Do One Thing** principle are good ways to ensure that our

functions are well designed and easy to test. Let's see how, starting with DRY.

  

When we write code to look for answers to a research question, it is totally normal to copy and paste a bit of code, tweak it slightly, and re-run it. However this, kind of repeated code can lead to real problems.

  

> **DRY = Do not repeat yourself**

```python
df['y1_z'] = (df['y1_gpa'] - df['y1_gpa'].mean()) / df['y1_gpa'].std()
df['y2_z'] = (df['y2_gpa'] - df['y2_gpa'].mean()) / df['y2_gpa'].std()
df['y3_z'] = (df['y3_gpa'] - df['y3_gpa'].mean()) / df['y3_gpa'].std()
df['y4_z'] = (df['y4_gpa'] - df['y4_gpa'].mean()) / df['y4_gpa'].std()
```

  

🆚

```python
def standardize(column):
    """Standardizes the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df['y1_gpa'])
df['y2_z'] = standardize(df['y2_gpa'])
df['y3_z'] = standardize(df['y3_gpa'])
df['y4_z'] = standardize(df['y4_gpa'])
```

  

> **DO One Thing**

```python
def load_and_plot(path):
    """Loads a data set and plot the first two principal components.

    Args:
      path (str): The location of a CSV file.

    Returns:
      tuple of ndarray: (features, labels)
    """
    # load the data
    data = pd.read_csv(path)
    y = data['label'].values
    X = data[col for col in train.columns if col != 'label'].values

    # plot the first two principal components
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])

    return X, y
```

  

🆚

```python
def load_data(path):
    """Loads a data set.

    Args:
      path (str): The location of a CSV file.

    Returns:
      tuple of ndarray: (features, labels)
    """
    data = pd.read_csv(path)
    y = data['labels'].values
    X = data[col for col in data.columns if col != 'labels'].values
    return X, y
```

  

```python
def plot_data(X):
    """Plots the first two principal components of a matrix.

    Args:
      X (numpy.ndarray): The data to plot.
    """
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])
```

  

First of all, our code has become more flexible. Imagine that later on in our script, we just want to load the data and not plot it. That's easy now with the `load_data()` function.

  

Likewise, if we wanted to do some transformation to the data before plotting, we can do the transformation and then call the `plot_data()` function. We have decoupled the loading functionality from the plotting functionality.

  

The code will also be easier for other developers to understand, and it will be more pleasant to test and debug.

  

Finally, if we ever need to update our code, functions that each have a single responsibility make it easier to predict how changes in one place will affect the rest of the code.

  

```python
#INITIAL CODE
def mean_and_median(values):
    """Gets the mean and median of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The mean and median
    """
    mean = sum(values) / len(values)
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return mean, median
```

  

### ✅ Setup default arguments in functions so that your code doesn't behave unexpectedly

```python
def add_column(values, df=pandas.DataFrame()):
    """Adds a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
          If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    df['col_{}'.format(len(df.columns))] = values
    return df
```

🆚

```python
def add_column(values, df=None):
    """Adds a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
          If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    if df is None:
        df = pandas.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df

df_1 = add_column(values=range(10))
print(df_1)

df_2 = add_column(values=range(10))
print(df_2)
```

  

Further Reading
===============
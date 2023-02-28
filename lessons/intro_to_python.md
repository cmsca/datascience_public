# Intro to Python

## Desired outcomes from this session:

The purpose of this session is to ensure each participant is comfortable enough with Python to enjoy and learn from the course.

- [ ] **Variables, expressions, statements**

    - Variables: a container that stores values
    ```Python
        x = 5 # A variable x is being created and assigned the value of 5.
    ```
    - Expressions: the use of operators to get some other value
    ```Python
        x = 10 + 5 # The arithmetic addition operator is used to add the two values
    ```
    - Statements: executes a command
    ```Python
        print(x) # Python executes the print statement to display x
    ```

- [ ] **Conditional execution**

    Boolean Expressions (True/False) can be checked by the conditional statement

    - If statements: if a condition is true, the code inside that `if` statement will run
    ```Python
        if(x > y):
            # The code in here will run if x is greater than y
    ```

    - If-else statements: if a condition is true, the code inside the `if` statement will run. Otherwise the code in the `else` statement will run
    ```Python
        if(y > x):
            # The code in here will run if y is greater than x
        else:
            # The code in here will run if the first condition was not true
    ```

    - Else-if statements: If a condition is true, the code inside the `if` statement will run. Otherwise, the `elif` conditon will be checked. If the `elif` condition is true, then the code inside the else-if will run
    ```Python
        if(x == y):
            # The code in here will run if x is equal to y
        elif(x > y)
            # The code in here will run if the previous condition was false and if x is greater than y
    ```

- [ ] **Functions**

    Functions are blocks of re-useable code that can run when called. Example:

    ```Python
    def my_function():
        x = 10
        print(x)
    
    # You can call the function by the following:
    my_function()
    ```
    Functions can also have parameters. For example:
    ```Python
    def print_value(value_to_print):
        print(value_to_print)
    
    # Call the function using:
    print_value("Hello World") # The argument "Hello World" is passed into the function
    
    ```
    This function displays:
    ```
    Hello World
    ```
    There can be as many parameters as you would like but each parameter must be separated by a comma and each argument must be in order of the parameters. For example:
    ```Python
    def print_hello_world(first, second):
        print(first)
        print(second)
    
    # Call the function using:
    print_hello_world("Hello", "World")
    ```
    This function displays:
    ```
    Hello
    World
    ```


- [ ] **Loops and iterations**

    For Loop: a loop that repeat a block of code a certain number of times
    ```Python
    for i in range(x):
        # The code in this block will run x times.
    ```

    Enhanced For Loop: A loop specifically made to iterate through elements in data structures.
    ```Python
    my_list = [1,2,3,4,5,6,7]
    for var in my_list:  # This loop will print every element of the list my_list 
        print(var)
    ```

    While Loop: a loop that repeats a block of code while a certain condition is true
    ```Python
    value = 0
    while (value < 10): # This loop will print values from 0-9 
        print(value)
        value = value + 1
    ```
    - When creating your own, beware of infinite loops!

- [ ] **Strings**

    Strings are data structures in Python that store a sequence of characters
    - Strings can be encased in single quotes `'Hello World'` or double quotes `"Hello World"`
    - Strings can be sliced, joined (concatenated), etc.
    Example of a String:
    ```Python
    my_string = "Hello World"
    print(my_string)
    ```
- [ ] **Lists**
    Lists are data structures that can store multiple values in one variable
    An example of a list would be:
    ```Python
    animal_list = ["cat", "dog", "snake", "hamster"]
    ```
    A list can have a combination of data types. For example:
    ```Python
    random_list = ["green", 1, True, "blue", 2, True, "red", 3, False]
    ```
    Since lists are objects, they have functions such as `type()` or `len()`
- [ ] **Dictionaries**

    Dictionaries are data structures that allow you to store values in what is called "key:value pairs"
    For each key, there will be a value to that key, but two keys cannot be the same.
    Just like lists they can have a combination of data types. 
    For example: 

    ```Python
    student_info = {

        "name": "Sam Smith",
        "honors_student": True,
        "grade": 11,
        "gpa": 4.0

    }

    print(student_info) # prints out the dictionary 
    ```
    We get the output: `{'name': 'Sam Smith', 'honors_student': True, 'grade': 11, 'gpa': 4.0}`

## Resources / Notes from the session:

- For any participant who has not been able to set up their laptop with Python, please create a [REPLIT](https://replit.com/) account for the session

- We will be using the lesson plans and material from the [Python for Everybody](https://www.py4e.com/) course


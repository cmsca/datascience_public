# Intro to Python

## Desired outcomes from this session:

The purpose of this session is to ensure each participant is comfortable enough with Python to enjoy and learn from the course.

- [ ] Variables, expressions, statements
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

- [ ] Conditional execution
    Boolean Expressions (True/False) can be checked by the conditional statement

    - If statements: if a condition is true, the code inside that `if` statement will run
    ```Python
        if(x > y):
            # The code in here will run if x is greater than y
    ```

    - If-else statements: if a condition is true, the code inside the `if` statement will run. Otherwise the code in the `else` statement will run
    ```Python
        if(y > x):
            # The code in here will run of y IS greater than x
        else:
            # The code in here will run if the first condition was not true
    ```

    - Else-if statements: If a condition is true, the code inside the `if` statement will run. Otherwise, the `elif` conditon will be checked. If the `elif` condition is true, then the code inside the else-if will run
    ```Python
        if(x == y):
            # The code in here will run if x is equal to y
        elif(x > y)
            # The code in here will run if the previous condition was false and x is greater than y
    ```

- [ ] Functions: blocks of re-useable code that can run when called. Example:

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
    print_value("Hello World")
    # The argument "Hello World" is passed into the function
    ```
    This function displays:
    ```
    Hello World
    ```
    There can be as many parameters as you would like but each parameter must be separated by a comma. Each argument must be in order of the parameters. For example:
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


- [ ] Loops and iterations
- [ ] Strings
- [ ] Lists
- [ ] Dictionaries

## Resources / Notes from the session:

- For any participant who has not been able to set up their laptop with Python, please create a [REPLIT](https://replit.com/) account for the session

- We will be using the lesson plans and material from the [Python for Everybody](https://www.py4e.com/) course


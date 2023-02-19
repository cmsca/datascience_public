# Intro to Web SQL

## Desired outcomes from this session:

The purpose of this session is to ensure each participant feels comfortable with the basics of SQL. We'll cover:

- [ ] Intro

    SQL uses relational databases 

    SQL provides instructions to search from a database
- [ ] Syntax

    Case Independent - SQL Reserved Keywords can be upper case or lowercase. Convention is to make them all uppercase to distinguish them between table or database names.

    `*` = Gets All Values

    `--` - Comment 

    `AS` - Give an alias to a name

    `JOIN` - Joins two tables together

    `SELECT` - Select data from a database

    `DISTINCT` = Gives rows that are unique (not repeated)

    `FROM` - Specifies table

    `LIMIT [x]` - Gets the first `x` values

- [ ] Clauses

    When writing clauses always have the where clause then the and clause then the or clause. 
    ```SQL
    LIKE '% %' 
    ``` - Finds similar keywords

    ```SQL 
    WHERE [] = '' 
    ``` - Create a condition 

     ```SQL 
    WHERE [] IS NOT NULL 
    ``` - Create a condition to not return `NULL` values
    
    ```SQL 
    AND [] = '' ``` - Add multiple conditions

     ```SQL 
    AND [] NOT LIKE '% %' ``` - Add condition to get a value that is not like some other value

    ```SQL
    OR [] = '' ``` - Add multiple conditions

    ```SQL
    ORDER BY [] ``` - Orders the column in alphabetical order

    ```SQL
    ORDER BY [] DESC``` Orders the column in descending alphabetical order

- [ ] Query

    Example Query: 
    ```SQL
    SELECT CustomerID FROM Customers WHERE Country = 'Germany' AND City = 'Berlin'
    ```

- [ ] Data Types

    `INTEGER` - Stores whole numbers

    `TEXT` - Stores long character strings

    `BLOB` - Memory address of an object(reference or pointer)

    `REAL`/`NUMERIC` - Stores numbers with decimals (Floating point numbers)

    `NULL` - Values that do not exist

- [ ] Security lesson: Phishing & 2-Factor Authentication

    - Prevents Phishing 

    - Sends a code to your phone to verify that the person logging in is you

    - Apps include [Twilio Authy](https://authy.com/) and [Duo Mobile](https://duo.com/)

- [ ] Using the [SQLite DB Browser](https://sqlitebrowser.org/)

Our timeline will be:

- 2pm - 2:50pm: Intro to SQL using the W3 [School SQL editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_asc)

- 2:50pm - 3pm: Break

- 3pm - 3:30pm: Practical exercise using the SQLite DB Browser

- 3:30pm - 4pm: Security lesson on Phishing and 2FA

## Resources / Notes from the session:

- W3 Schools SQL tutorial: https://www.w3schools.com/sql/

- W3 School SQL (in browser) editor: https://www.w3schools.com/sql/trysql.asp?filename=trysql_asc

- US Chess website: https://new.uschess.org/

- US Chess (old) website: https://www.uschess.org/index.php/Players-Ratings/

# README for CSD 310 - Movies Lab

## Assignment Overview 6.2 - Setup

This assignment is designed to enhance your skills in working with MySQL and Python. You will create database tables, run SQL scripts, and connect a Python program to MySQL. It's important to comprehend each step and its purpose.

### 1. Connecting PyCharm to MySQL
- Refer to the instructions provided in Module 4.
- Open the "PyCharm Install and Link to MySQL database" document for guidance.

### 2. MySQL Examples in the `db_init.sql` Script
- View `db_init_2022.sql` to understand the use of various SQL commands:
  - `DROP USER IF EXISTS`
  - `CREATE USER`
  - `GRANT ALL PRIVILEGES`
  - `DROP TABLE IF EXISTS`
  - `CREATE TABLE`
  - `FOREIGN KEY Constraints`
  - `INSERT INTO`

### 3. MySQL Command Line Interface (CLI) Scripts
- Instructions on starting MySQL CLI.
- Activation of the desired database using `use <database name>;`
- Running SQL scripts with `source <path_to_the_sql_script>.sql`
- Show database tables using `SHOW TABLES;`

### 4. MySQL and Python
- Install the MySQL Python driver: `pip install mysql-connector-python`
- Create a `mysql_test.py` script with the necessary imports and database connection test code.

### 5. Checklist
- Ensure all steps are completed:
  - Database activation guide review.
  - PyCharm connection to MySQL.
  - Installation of MySQL Python Driver.
  - Connection test for Python Connector.
  - Execution of CLI Scripts.

### 6. Instructions
- Complete the checklist.
- Activate the movies database in MySQL.
- Run `db_init_2022.sql` and take screenshots of the output and `SHOW TABLES` command.
- Create `mysql_test.py` under `module_6` directory.
- Write a Python program to connect to the movies database and run it. Capture a screenshot of the output.
- Compile all screenshots in a single Word document with your details.

### 7. GitHub
- Follow the GitHub tutorial on W3Schools.
- Stage, commit, and push your work to GitHub.

### 8. Deliverable
- Combine screenshots and GitHub repository link in a Word document.
- Save the document as `<your-last-name>-<assignment-name>.docx`.

## Assignment Overview 7.2 - Table Queries

In this assignment, you'll deepen your understanding of querying MySQL database tables using both the MySQL Command Line Interface (CLI) and a Python script.

### MySQL CLI: Select Query
- Learn to perform select queries through the MySQL CLI.
- Basic syntax: `SELECT <column_name>, <column_name> FROM <table_name>;`
- Example: `SELECT f_name, l_name, email FROM employee;`

### Python Script Cursor Example
- Use a cursor object to execute queries and fetch results in Python.
- Example code structure:
  ```python
  cursor = db.cursor()
  cursor.execute("SELECT f_name, l_name, email FROM employee") # Selecting fields
  employees = cursor.fetchall()
  for employee in employees:
      print("First Name: {}\nLast Name: {}\nEmail: {}\n".format(employee[0], employee[1], employee[2])) # Output format
  ```

### Instructions
1. **File Creation and Setup**:
   - Create a new file named `movies_queries.py` under the `module_7` directory.
   - Write code to connect to your MySQL movies database. Refer to the previous assignment for the structure.
   - You may reuse the connection code from the previous assignment.

2. **Writing Queries**:
   - Write four distinct queries within one Python file.
   - The queries should be:
     1. Select all fields from the `studio` table.
     2. Select all fields from the `genre` table.
     3. Select movie names with a run time of less than two hours.
     4. Get a list of film names and directors, ordered by director.

3. **Query Execution and Documentation**:
   - Run your script and capture the output of each query.
   - Ensure the output matches the format shown in the example.

4. **Documentation and Submission**:
   - Take screenshots of your script results.
   - Compile these screenshots into a Word document.

### Deliverable
- Your submission should include:
  - The `movies_queries.py` Python file.
  - A Word document containing screenshots of your script's output.
- Ensure to include descriptions and the correct output format in your screenshots.
- Remember to include your name, date, and assignment details in the Word document.

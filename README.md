# README for CSD 310 - Movies: 6.2 Lab

## Assignment Overview

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

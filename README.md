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

## Assignment Overview 8.2 - Update & Deletes

This lab focuses on updating and deleting records from a MySQL database, as well as enhancing your Python scripting skills to interact with the database.

### 1. MySQL Instructions

#### Update Records
- Syntax: `UPDATE <table> SET <columns> WHERE <column> = <value>;`
- Example: 
  ```sql
  UPDATE player
  SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';
  ```

#### Delete Records
- Syntax: `DELETE FROM <table> WHERE <column> = <value>;`
- Example: 
  ```sql
  DELETE FROM player WHERE first_name = 'Smeagol';
  ```

#### Insert Records
- Syntax: `INSERT INTO <table> (<columns>) VALUES (<values>);`
- Example: 
  ```sql
  INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1);
  ```

### 2. Python Instructions

#### Function Creation
- Develop a Python function `show_films(cursor, title)` to display contents of the film table.
- Utilize INNER JOINs in the SQL query for genre and studio names.
- Ensure proper formatting and iteration over the dataset to display the results.

#### Python Example
```python
def show_films(cursor, title):
    # SQL query with INNER JOIN
    cursor.execute("select film_name as Name, film director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
```

### 3. Assignment Instructions

1. **File Setup**:
   - Create a new file named `movies_update_and_delete.py` in the `module_8` directory.

2. **Database Operations**:
   - Connect to the movies database.
   - Insert a new record (avoid using 'Star Wars').
   - Update the film 'Alien' to the 'Horror' genre.
   - Delete the movie 'Gladiator'.

3. **Execution and Documentation**:
   - After each database operation, call `show_films(cursor, "DISPLAYING FILMS")` to display the current state of the film table.
   - Document the process and results. Take screenshots or copy the output to a Word document.
   - Ensure your output matches the expected output format.

### Deliverable

- Submit the `movies_update_and_delete.py` Python file.
- Include a Word document with screenshots or copied output showcasing your results.
- Ensure the document contains your name, date, and assignment details.


## Assignment Overview 10 - Milestone #2

Milestone #2 focuses on refining your Entity-Relationship Diagram (ERD) and creating a functional database with sample data in MySQL. You will also write a Python script to display the data from each table.

### 1. ERD and Business Rules Review

- **ERD Refinement**: Re-examine your initial ERD. Ensure that it includes attributes for each table and revise as necessary.
- **Normalization**: Confirm that all tables are in the Third Normal Form (3NF) to ensure database efficiency and reduce redundancy.

### 2. SQL Script Creation

- **Table Creation**: Write a `.sql` script to create the tables in MySQL as defined in your ERD.
- **Data Population**: Populate each table with at least 6 records (or fewer if specified in your case study).

### 3. Python Script for Data Display

- Write a Python script similar to the 'movies example' from a previous assignment. The script should display data from each table in your database.
- The script should connect to your MySQL database, query each table, and output the results.

### 4. Documentation and Deliverables

- **Python Scripts**: Include all Python scripts used for displaying table data.
- **Word Document**: Create a document containing:
  - Your group name and members.
  - The revised ERD.
  - Screenshots of the data displayed from each table, as output by your Python script.

### 5. Submission Guidelines

- **Packaging**: Zip up all Python scripts and the Word document.
- **Posting**: Have one group member post the zipped file to your group forum with the subject line "Milestone 2".
- **GitHub**: Each team member should push the deliverable to their respective GitHub accounts.
- **No Blackboard Upload**: File uploads to Blackboard are not necessary for this milestone.

## Assignment Overview 11 - Milestone #3

Milestone #3 is about deriving valuable business insights from your database. This involves creating reports based on the data, which will aid in making informed business decisions as outlined in your case study.

### 1. Understanding the Business Requirements

- **Case Study Review**: Revisit the case study to identify key business decisions.
- **Report Identification**: Determine what information from the tables will be useful for these decisions. Plan to create a minimum of three different reports.

### 2. Report Description and Script Writing

- **Report Descriptions**: For each report, provide a clear and detailed description, explaining its purpose and the insights it aims to deliver.
- **Python Script Development**: Write Python scripts to generate these reports. The scripts should:
  - Connect to your MySQL database.
  - Execute the necessary SQL queries to retrieve the data.
  - Format and display the results clearly.

### 3. Execution and Documentation

- **Running the Scripts**: Execute each Python script and capture the output.
- **Screenshots**: Take screenshots of each report as displayed by the Python script.

### 4. Documentation and Deliverables

- **Python Scripts**: Include all scripts used for generating the reports.
- **Word Document**: Create a document containing:
  - Your group name and members.
  - Detailed descriptions of each report.
  - Screenshots showing the results of the queries.

### 5. Submission Guidelines

- **Packaging**: Zip up all Python scripts and the Word document.
- **Posting**: Have one group member post the zipped file to your group forum in Blackboard with the subject line "Milestone 3".
- **GitHub**: Each team member should push the deliverable to their respective GitHub accounts.
- **No Blackboard Upload**: File uploads to Blackboard are not necessary for this milestone.

from datetime import datetime
current_month = datetime.today().strftime('%Y-%m')

import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import SQLMode

# Create Database
passString = input("Please enter your mySQL root password: ")
db = mysql.connector.connect( # Using movies_user from previous modules, because everyone should already have this user.
    host="localhost",
    username="root",
    password=passString
)
cursor = db.cursor()

# Create Database WillsonFinancial, Delete first if it exists
cursor.execute("DROP DATABASE IF EXISTS WillsonFinancial")
cursor.execute("CREATE DATABASE WillsonFinancial")
cursor.execute("GRANT ALL PRIVILEGES ON WillsonFinancial.* TO 'movies_user'@'localhost'")


cursor.close()
db.close() # Going to re-connect to the new database, because I can re-use the code below

config = { # Using the movies_user
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "WillsonFinancial",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    db.sql_mode = ''

    db.autocommit = True

    print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n Press 'Enter' to continue...\n")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

# Create Employees Table
sql = '''CREATE TABLE IF NOT EXISTS Employees(
    EmployeeID INT NOT NULL,
    FirstName CHAR(20) NOT NULL,
    LastName CHAR(20) NOT NULL,
    PRIMARY KEY (EmployeeID)
)'''
cursor.execute(sql)

# Populate Employees Table (Data provided in case study)
cursor.execute("INSERT INTO Employees VALUES (1, 'Jake', 'Willson')")
cursor.execute("INSERT INTO Employees VALUES (2, 'Ned', 'Willson')")
cursor.execute("INSERT INTO Employees VALUES (3, 'Phoenix', 'Two Star')")
cursor.execute("INSERT INTO Employees VALUES (4, 'June', 'Santos')")

# Create Client Table, Phone Number expects "11234567890" format, where first characters represent country code, For example US country code is 1
sql = '''CREATE TABLE IF NOT EXISTS Clients(
    ClientID INT NOT NULL,
    Business CHAR(200),
    FirstName CHAR(20),
    LastName CHAR(20),
    Address CHAR(200),
    PhoneNumber CHAR(12),
    DateAdded DATE,
    PRIMARY KEY (ClientID)
)'''
cursor.execute(sql)

# Populate Clients Table (Data NOT provided by case study)
cursor.execute("INSERT INTO Clients VALUES (1, 'Jersey Dairy Farm', 'Bill', 'Jersey', '123 Fake Street', '11234567890', '2023-01-01')")
cursor.execute("INSERT INTO Clients VALUES (2, 'Scott Auto Sales - Sales Department', 'Michael', 'Scott', '17 Playground Ave', '1596237891', '2023-02-01')")
cursor.execute("INSERT INTO Clients VALUES (3, 'Scott Auto Sales - Advertising Department', 'Jim', 'Scott', '17 Playground Ave', '03216549871', '2023-02-01')")
cursor.execute("INSERT INTO Clients VALUES (4, '', 'Mike', 'Dillber', '62 Parkway Drive', '01112223333', '2023-04-01')")
cursor.execute("INSERT INTO Clients VALUES (5, '', 'John', 'Bengal', '', '12223334444', '2023-06-01')")
cursor.execute("INSERT INTO Clients VALUES (6, 'Greene Pharmacy', 'Henry', 'Greene', '911 Medicine Drive', '65984231657', '2023-06-01')")

# Create Assets Table
sql = '''CREATE TABLE IF NOT EXISTS Assets(
    ClientID INT NOT NULL,
    AssetType CHAR(30),
    AssetID INT NOT NULL,
    Value DOUBLE,
    PRIMARY KEY (AssetID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
)'''
cursor.execute(sql)

# Populate Assets Table
cursor.execute("INSERT INTO Assets VALUES (1, 'Real Estate', 1, 3000000.00)")
cursor.execute("INSERT INTO Assets VALUES (1, 'Tractor', 2, 100000)")
cursor.execute("INSERT INTO Assets VALUES (2, 'Ford Mustang GT', 3, 65000)")
cursor.execute("INSERT INTO Assets VALUES (2, 'Dodge Ram 4x4', 4, 50000)")
cursor.execute("INSERT INTO Assets VALUES (3, 'Real Estate', 5, 165000)")
cursor.execute("INSERT INTO Assets VALUES (4, 'Real Estate', 6, 124000)")
cursor.execute("INSERT INTO Assets VALUES (5, 'Real Estate', 7, 187000)")

# Create Transactions Table, Date expects "xx/yy/zzzz" format
sql = '''CREATE TABLE IF NOT EXISTS Transactions(
    ClientID INT NOT NULL,
    Date DATE,
    TransNumber INT NOT NULL,
    Amount DOUBLE,
    PRIMARY KEY (TransNumber),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
)'''
cursor.execute(sql)

# Populate Transactions Table
cursor.execute("INSERT INTO Transactions VALUES (1, '2023-11-27', 1, 231.49)")
cursor.execute("INSERT INTO Transactions VALUES (1, '2023-10-14', 2, 349.67)")

# More than 10 for 2nd ID for testing
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-02', 3, 50000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-06', 4, 40000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-10', 5, 50000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-11', 6, 40000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-12', 7, 50000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-14', 8, 40000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-15', 9, 50000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-17', 10, 40000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-18', 11, 50000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-20', 12, 40000.00)")
cursor.execute(f"INSERT INTO Transactions VALUES (2, '{current_month}-22', 13, 40000.00)")

# More than 10 for 6th ID for testing
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-01', 14, -156.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-02', 15, -214.73)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-03', 16, 15.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-04', 17, 24.73)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-05', 18, 1568.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-06', 19, 2174.73)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-07', 20, 1566.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-08', 21, 2124.73)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-09', 22, 56.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-10', 23, 2314.73)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-11', 24, 15.34)")
cursor.execute(f"INSERT INTO Transactions VALUES (6, '{current_month}-12', 25, 2214.73)")


# Display Data
cursor.execute("SELECT * FROM EMPLOYEES")
data = cursor.fetchall()
print("\n-- DISPLAYING EMPLOYEES TABLE --\n")
for employee in data:
    print("Employee Name: {} {}\nEmployee ID: {}\n".format(employee[1], employee[2], employee[0]))
input("Press 'Enter' to Continue...")

cursor.execute("SELECT * FROM Clients")
data = cursor.fetchall()
print("\n-- DISPLAYING CLIENTS TABLE --\n")
for client in data:
    print("Client ID: {}\n\nBusiness: {}\nContact Name: {} {}\nAddress: {}\nPhone Number: {}\n".format(client[0], client[1], client[2], client[3], client[4], client[5]))
input("Press 'Enter' to Continue...")

cursor.execute("SELECT * FROM Assets")
data = cursor.fetchall()
print("\n-- DISPLAYING ASSETS TABLE --\n")
for asset in data:
    print("Client ID: {}\nAsset Type: {}\nAsset ID: {}\nValue: {}\n".format(asset[0], asset[1], asset[2], asset[3]))
input("Press 'Enter' to Continue...")

cursor.execute("SELECT * FROM Transactions")
data = cursor.fetchall()
print("\n-- DISPLAYING TRANSACTIONS TABLE --\n")
for trans in data:
    print("Client ID: {}\nDate: {}\nTransaction Number: {}\nTransaction Amount: {}\n".format(trans[0], trans[1], trans[2], trans[3]))
input("No Tables Remaining to Print. Press 'Enter' to Exit...")

cursor.close()
db.close()
import mysql.connector
from datetime import datetime, timedelta

# Database connection configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "WillsonFinancial",
    "raise_on_warnings": True
}

# Establishing connection to the database
try:
    db = mysql.connector.connect(**config)
    print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
except mysql.connector.Error as err:
    print("Error connecting to MySQL:", err)
    exit(1)

cursor = db.cursor()

# Client Growth Report Query
one_year_ago = (datetime.today() - timedelta(days=30*12)).strftime('%Y-%m-%d')
client_growth_query = """
SELECT YEAR(DateAdded) AS Year, MONTH(DateAdded) AS Month, COUNT(*) AS NewClients
FROM Clients
WHERE DateAdded >= %s
GROUP BY YEAR(DateAdded), MONTH(DateAdded)
ORDER BY Year, Month;
"""

# Asset Overview Report Query
asset_overview_query = """
SELECT AVG(Value) AS AverageAssetValue
FROM Assets;
"""

# Transaction Analysis Report Query
transaction_analysis_query = """
SELECT ClientID, COUNT(*) AS TransactionCount
FROM Transactions
WHERE DATE_FORMAT(Date, '%%Y-%%m') = DATE_FORMAT(CURDATE(), '%%Y-%%m')
GROUP BY ClientID
HAVING COUNT(*) > 10;
"""

# Execute Client Growth Report Query
cursor.execute(client_growth_query, (one_year_ago,))
print("\n-- CLIENT GROWTH REPORT --\n")
for year, month, new_clients in cursor:
    print("Year: {}, Month: {}, New Clients: {}".format(year, month, new_clients))

# Execute Asset Overview Report Query
cursor.execute(asset_overview_query)
print("\n-- ASSET OVERVIEW REPORT --\n")
for average_asset_value, in cursor:
    print("Average Asset Value: ${:.2f}".format(average_asset_value))

# Execute Transaction Analysis Report Query
cursor.execute(transaction_analysis_query)
print("\n-- TRANSACTION ANALYSIS REPORT --\n")
for client_id, transaction_count in cursor:
    print("Client ID: {}, Transaction Count: {}".format(client_id, transaction_count))


# Clean up
cursor.close()
db.close()

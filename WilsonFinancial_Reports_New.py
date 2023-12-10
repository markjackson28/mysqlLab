import mysql.connector
import datetime

def connect_to_database():
    config = {
        "user": "movies_user",
        "password": "popcorn",
        "host": "127.0.0.1",
        "database": "WillsonFinancial",
        "raise_on_warnings": True
    }
    return mysql.connector.connect(**config)

def generate_new_clients_report():
    db = connect_to_database()
    cursor = db.cursor()

    current_year = datetime.datetime.now().year
    query = """
    SELECT c.ClientID, c.FirstName, c.LastName, c.DateAdded, COUNT(a.AssetType) AS NumberOfAssets, SUM(a.Value) AS TotalAssetValue
    FROM Clients c
    LEFT JOIN Assets a ON c.ClientID = a.ClientID
    WHERE YEAR(c.DateAdded) = %s
    GROUP BY c.ClientID;
    """
    cursor.execute(query, (current_year,))

    print(f"\n-- New Clients Report for the Year {current_year} --\n")
    for row in cursor:
        print(
            f"Client ID: {row[0]}, Name: {row[1]} {row[2]}, Date Added: {row[3]}, Number of Assets: {row[4]}, Total Asset Value: {row[5]}")
    cursor.close()
    db.close()

def generate_asset_overview(client_id):
    db = connect_to_database()
    cursor = db.cursor()

    query = """
    SELECT AssetType, AssetID, Value
    FROM Assets
    WHERE ClientID = %s;
    """
    cursor.execute(query, (client_id,))

    total_value = 0
    assets_count = 0
    print(f"\n-- Asset Overview for Client ID {client_id} --\n")
    for asset in cursor:
        total_value += asset[2]
        assets_count += 1
        print(f"Asset Type: {asset[0]}, Asset ID: {asset[1]}, Value: {asset[2]}")

    if assets_count > 0:
        average_value = total_value / assets_count
        formatted_total_value = "{:.2f}".format(total_value)
        formatted_average_value = "{:.2f}".format(average_value)
        print(f"\nTotal Value of Assets: {formatted_total_value}, Average Value: {formatted_average_value}")
    else:
        print("\nNo assets found for this client.")

    cursor.close()
    db.close()

def generate_transaction_report(client_id):
    db = connect_to_database()
    cursor = db.cursor()

    query = """
    SELECT Date, TransNumber, Amount
    FROM Transactions
    WHERE ClientID = %s;
    """
    cursor.execute(query, (client_id,))

    total_amount = 0
    transactions_count = 0
    print(f"\n-- Transaction Report for Client ID {client_id} --\n")
    for trans in cursor:
        total_amount += trans[2]
        transactions_count += 1
        print(f"Date: {trans[0]}, Transaction Number: {trans[1]}, Amount: {trans[2]}")

    formatted_total_amount = "{:.2f}".format(total_amount)
    print(f"\nTotal Transactions Value: {formatted_total_amount}, Number of Transactions: {transactions_count}")
    cursor.close()
    db.close()

def main():
    while True:
        print("\nSelect a report to generate:")
        print("1. New Clients Report")
        print("2. Asset Overview for a Specific Client")
        print("3. Transaction Report for a Specific Client")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_new_clients_report()
        elif choice == '2':
            client_id = input("Enter the Client ID: ")
            generate_asset_overview(client_id)
        elif choice == '3':
            client_id = input("Enter the Client ID: ")
            generate_transaction_report(client_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

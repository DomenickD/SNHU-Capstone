"""Create a database in sqlite from the csv files taken from yfinance API"""

import sqlite3
import os
import pandas as pd

# Database file name
DATABASE_NAME = "stock_data.db"

# Directory containing CSV files
CSV_DIRECTORY = "stock_data_csv"

# Establish a connection to the database
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    pull_date TIMESTAMP
)
"""
)

# Iterate through CSV files in the directory
for filename in os.listdir(CSV_DIRECTORY):
    if filename.endswith(".csv"):
        # Construct the full file path
        filepath = os.path.join(CSV_DIRECTORY, filename)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(filepath)

        # Extract the table name from the filename (removing the '_max.csv' part)
        table_name = filename.replace("_max.csv", "")

        # Write the DataFrame to a new SQLite table
        df.to_sql(
            table_name, conn, if_exists="replace", index=False
        )  # Replace if table exists

        print(f"Created table '{table_name}' from '{filename}'")

# Close the connection
conn.close()

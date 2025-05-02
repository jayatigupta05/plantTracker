import sqlite3

# Connect to your database
conn = sqlite3.connect('plants.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print schema for each table
for table_name in tables:
    print(f"\nSchema for table: {table_name[0]}")
    cursor.execute(f"PRAGMA table_info({table_name[0]})")
    schema = cursor.fetchall()
    for column in schema:
        print(column)

conn.close()

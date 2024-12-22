import sqlite3

conn = sqlite3.connect("app/test.db")  # Update to match your database path
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# View table schema
for table in tables:
    print(f"\nSchema for table {table[0]}:")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    print(cursor.fetchall())

conn.close()


# import sqlite3

# conn = sqlite3.connect("app/test.db")
# cursor = conn.cursor()

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print("Tables:", cursor.fetchall())

# conn.close()


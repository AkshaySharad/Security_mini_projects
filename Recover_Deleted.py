# Recover deleted items from a local SQLite database, assuming the database follows the convention of keeping deleted
# items for 30 days in a separate table

import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Get the current date and the date 30 days ago
today = datetime.now().date()
thirty_days_ago = today - timedelta(days=30)

# Query the "deleted_items" table for items deleted within the last 30 days
c.execute("SELECT * FROM deleted_items WHERE deleted_date >= ? AND deleted_date <= ?", (thirty_days_ago, today))
deleted_items = c.fetchall()

# Print the recovered deleted items
if deleted_items:
    print("Recovered Deleted Items:")
    for item in deleted_items:
        print(item)
else:
    print("No deleted items found within the last 30 days.")

# Close the database connection
conn.close()
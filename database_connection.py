import sqlite3
import _sqlite3

conn = sqlite3.connect("Here")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS files (name TEXT, size INTEGER)")
cur.execute("INSERT INTO files VALUES (?, ?)",("REPORT.txt", 2048))
conn.commit()

cur.execute("SELECT * FROM files")
rows = cur.fetchall()

conn.close
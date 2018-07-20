#!/usr/bin/env python3


import sqlite3


connection = sqlite3.connect("master.db", check_same_thread=False)
cursor = connection.cursor()

# Create users table
cursor.execute(
	"""CREATE TABLE users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(16) UNIQUE NOT NULL,
		password VARCHAR(128) NOT NULL,
		first_login DATETIME NOT NULL,
		last_login DATETIME NOT NULL
	);"""
)

cursor.close()
connection.close()
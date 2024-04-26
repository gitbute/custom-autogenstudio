# filename: cms/utils/db.py
import sqlite3 as db
connection = db.connect('file.db')
cursor = connection.cursor()
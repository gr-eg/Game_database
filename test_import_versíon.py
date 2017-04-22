#test file to import qinto the database
import sqlite3
import databaseVersion

connecting to the database
conn = sqlite3.connect(test.sqlite)
c = conn.cursor()
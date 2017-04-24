#test file to import qinto the database
import sqlite3
import databaseVersion


print(databaseVersion.versionCreate())
input('wait')

#connecting to the database
conn = sqlite3.connect(test.sqlite)
c = conn.cursor()

c.execute('''CREATE TABLE versionNumber (version INTEGER PRIMARY KEY)''')

c.execute('''INSET INTO versionNumber (version) VALUES (?)''', databaseVersion.versionCreate())

conn.commit()
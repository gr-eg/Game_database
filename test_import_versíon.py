#test file to import qinto the database
import sqlite3
import databaseVersion


print(databaseVersion.versionCreate())
i = int(databaseVersion.versionCreate())
print(i)
input('wait')

#connecting to the database
conn = sqlite3.connect('test.sqlite')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS versionNumber (version INTEGER)''')

c.execute('''INSERT INTO versionNumber (version) VALUES (?)''', i)

conn.commit()
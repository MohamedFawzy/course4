import sqlite3

conn = sqlite3.connect('emaildb.sqlite')

cur = conn.cursor()

cur.execute('''
DROP TABLE IF  EXISTS counts''')

cur.execute(''' CREATE TABLE counts(email TEXT, count INTEGER) ''')

fname = raw_input('Enter file name: ')
if(len(fname) < 1): fname = 'mbox-short.txt'


fh = open(fname)

for line in fh:
    if not line.startswith('From : '): continue
    pieces = line.split()
    email = pieces[1]
    print email
    cur.execute('SELECT count FROM counts where email = ?',(email,))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE counts set count=count+1 WHERE email = ?',(email,))
    except:
        cur.execute('''INSERT INTO counts(email,count) VALUES(?,1)''', (email,))

    conn.commit

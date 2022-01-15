import sqlite3 as sl
con = sl.connect('data.db')


# with con:
#     con.execute("""
#         CREATE TABLE USER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             location TEXT,
#             time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         );
#     """)


# with con:
#     con.execute("""
#         DROP TABLE USER;
#     """)

# with con:
#     con.execute("""
#         Delete FROM USER;
#     """)

# sql = 'INSERT INTO USER (name, location) values(?, ?)'
# data = [
#     ('Apoorv Mishra', 'Main Gate'),
#     ('Arpit Mishra', 'Main Gate'),
#     ('Mahima', 'Main Gate')
# ]
# with con:
#     con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM USER")
    for row in data:
        print(row)


# query="UPDATE USER SET location=?, time= ? "
# data=('Hostel M', time.time())
#     with con:
#         con.execute(query, data)
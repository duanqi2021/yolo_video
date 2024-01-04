import sys

sys.path.insert(0, '..')

from base.sqlhelper import *

sql = SqlHelper()
sql.select_db(db)

num = sql.execute("insert into user (username, password, name) values ('admin', '123456', 'Admin')")
print('execute num: %d'%num)

result = sql.fetchone("select * from user")
print('one result: %s'%result)

result = sql.fetchall("select * from user")
print('all result: %s'%result)

result = sql.fetchmany("select * from user", size = 3)
print('many result: %s'%result)

# test with
with SqlHelper() as db:
	result = db.fetchone('select * from user')
	print('with result: %s'%result)

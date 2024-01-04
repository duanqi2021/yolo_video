import pymysql
import pymysql.cursors
from config.config import *

# API Reference: http://pymysql.readthedocs.io/en/latest/modules/

class SqlHelper:
	'''mysql helper'''
	def __init__(self):
		self.connection = None
		self.connect()

	def connect(self):
		if not self.connection:
			self.connection = pymysql.connect(
				host = host,
				port = port,
				user = user, 
				password = password, 
				db = db, 
				charset = charset, 
				cursorclass = pymysql.cursors.DictCursor)
		if not self.connection.open:
			self.connection = None
			self.connect()

	def select_db(self, dbname):
		self.connection.select_db(dbname)

	def close(self):
		if self.connection:
			self.connection.close()

	'''run a insert or update sql'''
	def execute(self, sql, args = None):
		num = 0
		with self.connection.cursor() as cursor:
			num = cursor.execute(sql, args)
		self.connection.commit()
		return num

	# def executemany(self, sql, args = None):
	# 	num = 0
	# 	with self.connection.cursor() as cursor:
	# 		num = cursor.executemany(sql, args)
	# 	self.connection.commit()
	# 	return num

	'''fetch one result'''
	def fetchone(self, sql, args = None):
		result = None
		with self.connection.cursor() as cursor:
			cursor.execute(sql, args)
			result = cursor.fetchone()
		return result

	def fetchall(self, sql, args = None):
		result = None
		with self.connection.cursor() as cursor:
			cursor.execute(sql, args)
			result = cursor.fetchall()
		return result

	def fetchmany(self, sql, args = None, size = 100):
		result = None
		with self.connection.cursor() as cursor:
			cursor.execute(sql, args)
			result = cursor.fetchmany(size)
		return result

	def __del__(self):
		self.close()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		return
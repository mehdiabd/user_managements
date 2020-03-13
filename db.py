__author__ = "Mehdi Abdullahi"

from pymongo import MongoClient

try:
	con = MongoClient()
	print('Connected')
except:
	print("Couldn't connect")


class DB:
	def __init__(self, collection):
		self.db = con.user
		self.col = self.db[collection]

	def add(self, user):
		self.col.insert_one(user)

	def fetch(self, id):
		return self.col.find_one({"_id": id})

	def update(self, id, inf):
		return self.col.update_one({{'_id': id}, {'$set': inf}}).modified_count

	def remove(self, u):
		self.col.delete_one({'username': u})

	def find(self, u):
		self.col.find_one({'username': u})

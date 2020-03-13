__author__ = "Mehdi Abdullahi"

from pymongo import MongoClient
from bson import ObjectId

try:
	con = MongoClient()
	print('Connected')
except:
	print("Couldn't connect")


class DB:
	def __init__(self, collection):
		self.db = con.user
		self.col = self.db[collection]

	def add(self, data):
		return self.col.insert_one(data).inserted_id

	def fetch(self, id):
		return self.col.find_one({"_id": ObjectId(id)})

	def update(self, id, inf):
		return self.col.update_one({{'_id': ObjectId(id)}, {'$set': inf}}).modified_count

	def remove(self, id, inf):
		return self.col.delete_one({'_id': ObjectId(id), 'username': inf})

	def find(self, data):
		return self.col.find_many(data)

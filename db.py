__author__ = "Mehdi Abdullahi"

from pymongo import MongoClient

try:
	con = MongoClient()
	print('Connected')
except:
	print("Couldn't connect")

db = con.user

col = db.account

user1 = {
		"name": "Mr.Mehdi",
		"eid": 97,
		"location": "Tehran"
		}

user2 = {
		"name": "Mr.Abdullah",
		"eid": 76,
		"location": "Guilan"
		}

user3 = {
		"name": "Mr.Hashem",
		"eid": 18,
		"location": "Ardebil"
		}

q1 = col.insert_one(user1)
q2 = col.insert_one(user2)
q3 = col.insert_one(user3)

print("Data inserted: ", q1, " , ", q2, " , ", q3)

cursor = col.find()
for rec in cursor:
	print(rec)

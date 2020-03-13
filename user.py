__author__ = "Mehdi Abdullahi"

from db import DB


class User:
    def __init__(self):
        self.uname = ''
        self.pword = ''

    def add(self, data):
        return DB('user').add(data)

    def delete(self, id):
        return self.delete({'_id': id})

    def update(self, id, inf):
        return DB('user').update(id, inf)

    def chpass(self, id, p):
        return DB('user').update(id, {"password": p})

    @staticmethod
    def fetch(id):
        return DB('user').fetch(id)

    def find(self, data):
        return DB('user').find(data)

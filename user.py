__author__ = "Mehdi Abdullahi"


class User:
    def __init__(self):
        self.uname = ''
        self.pword = ''

    def __delete__(self, instance):
        self.__delete__(instance)

    def update(self, u):
        self.uname = u

    def chpass(self, p):
        self.pword = p

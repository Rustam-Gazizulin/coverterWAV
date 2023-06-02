from utils.db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __int__(self, username, email):
        self.username = username
        self.email = email

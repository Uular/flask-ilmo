from ilmo import db
from datetime import datetime


class KmpEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=False)
    email = db.Column(db.String(80), index=True, unique=False)
    phone = db.Column(db.String(20), index=True, unique=False)
    guild = db.Column(db.String(10), index=True, unique=False)
    sitsit = db.Column(db.Boolean())
    station = db.Column(db.String(10), index=True)
    time = db.Column(db.DateTime)
    friend = db.Column(db.String(150), unique=False)
    nationality = db.Column(db.String(150), unique=False)

    def __init__(self, name="", email="", phone="", guild="",
                 sitsit=False, station="", nationality="", friends=""):
        self.name = name
        self.email = email
        self.phone = phone
        self.guild = guild
        self.sitsit = sitsit
        self.station = station
        self.friend = friends
        self.nationality = nationality
        self.time = datetime.now()

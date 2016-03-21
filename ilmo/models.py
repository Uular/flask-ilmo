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


class HumuEntry(db.Model):
    __tablename__ = 'humu_entry'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=False)
    email = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(20), unique=False)
    guild = db.Column(db.String(10), index=True, unique=False)
    allergies = db.Column(db.String(200))
    alcohol = db.Column(db.Boolean())
    mild = db.Column(db.String(15))
    wine = db.Column(db.String(15))
    time = db.Column(db.DateTime)
    avec_id = db.Column(db.Integer, db.ForeignKey('humu_entry.id'))
    avec = db.relationship('HumuEntry', uselist=False)
    is_avec = db.Column(db.Boolean)


    def __init__(self, name="", email="", phone="", guild="", allergies="", alcohol_free=False, wine=None, mild=None, is_avec=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.guild = guild
        self.wine = wine
        self.mild = mild
        self.time = datetime.now()
        self.allergies = allergies
        self.alcohol = alcohol_free
        self.is_avec = is_avec


class OksEntry(db.Model):
    __tablename__ = 'oks_entry'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=False)
    email = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(20), unique=False)
    guild = db.Column(db.String(10), index=True, unique=False)
    allergies = db.Column(db.String(200))
    alcohol = db.Column(db.Boolean())
    mild = db.Column(db.String(15))
    wine = db.Column(db.String(15))
    time = db.Column(db.DateTime)
    #avec_id = db.Column(db.Integer, db.ForeignKey('humu_entry.id'))
    #avec = db.relationship('HumuEntry', uselist=False)
    is_avec = db.Column(db.Boolean)


    def __init__(self, name="", email="", phone="", guild="", allergies="", alcohol_free=False, wine=None, mild=None, is_avec=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.guild = guild
        self.wine = wine
        self.mild = mild
        self.time = datetime.now()
        self.allergies = allergies
        self.alcohol = alcohol_free
        self.is_avec = is_avec

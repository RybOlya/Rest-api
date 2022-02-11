from typing import List
from main import db
class Fish(db.Model): 
   
   id = db.Column(db.Integer, primary_key = True)#об'єкти типу db.Column, які описують модель Fish, primary_key унікальний ідентифікатор цього запису
   name = db.Column(db.String(10))
   origin = db.Column(db.String(20))
   age_in_months = db.Column(db.Integer)
   weight = db.Column(db.Integer)#конструктор згенерує алхімія


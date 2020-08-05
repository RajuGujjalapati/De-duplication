from flask import Flask, request, jsonify,Response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
import pymysql
# from flask_mysqldb import MySQL
import os
#Init app
app = Flask(__name__)
mysql=MySQL()
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nani@localhost:3306/flask_restapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)
ma = Marshmallow(app)

 
# Product Class/Model
class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(100), unique=False)
  lastName = db.Column(db.String(200),unique=False)
  gender = db.Column(db.String(10))
  dob = db.Column(db.Date)
  location=db.Column(db.String(20))
  clientType = db.Column(db.String(20))
  aadharNumber = db.Column(db.String(12))
  panCard = db.Column(db.String(10))

  def __init__(self,firstName, lastName, gender, dob,location,clientType,aadharNumber,panCard):
    self.firstName = firstName
    self.lastName = lastName
    self.gender = gender
    self.dob = dob
    self.location=location
    self.clientType=clientType
    self.aadharNumber=aadharNumber
    self.panCard=panCard


# Product Schema
class UserdataSchema(ma.Schema):
  class Meta:
    fields = ('firstName','lastName','id' ,'gender', 'dob','location','clientType','aadharNumber','pancard')

# Init schema
userdata_schema = UserdataSchema() #for single product
usersdata_schema = UserdataSchema(many=True)#to deal with multiple products

# Create a User
@app.route('/postuser', methods=['POST'])
def add_product():
  firstname = request.json['firstName']
  lastname = request.json['lastName']
  gender = request.json['gender']
  dob = request.json['dob']
  loc = request.json['location']
  clientType = request.json['clientType']
  aadhar = request.json['aadharNumber']
  pan = request.json['panCard']
    #instantiating  the fileds specified while creating the database using class(variable)
  new_data = Users(firstname, lastname, gender, dob,loc,clientType,aadhar,pan)

  db.session.add(new_data) 
  db.session.commit()
  return userdata_schema.jsonify(new_data)

# Get All Users
@app.route('/getallusers', methods=['GET'])
def get_users():
  all_users = Users.query.all()
  result = usersdata_schema.dump(all_users)
  return jsonify(result)
  
@app.route('/getuser/<id>', methods=['GET'])
def get_user(id):
  user = Users.query.get(id)
  return userdata_schema.jsonify(user)

# Update a User
@app.route('/updateuser/<id>', methods=['PUT'])
def update_user(id):
  user = Users.query.get(id)

  fname = request.json['firstName']
  lname = request.json['lastName']
  gender = request.json['gender']
  dob = request.json['dob']
  loc = request.json['location']
  clienttype = request.json['clientType']
  aadhar = request.json['aadharNumber']
  pan = request.json['panCard']

  user.firstName = fname
  user.lastName = lname
  user.gender = gender
  user.dob = dob
  user.loc = loc
  user.clienttype = clienttype
  user.aadhar = aadhar
  user.pan= pan
  db.session.commit()
  return userdata_schema.jsonify(user)

# Delete Product
@app.route('/deluser/<id>', methods=['DELETE'])
def delete_user(id):
  user = Users.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return userdata_schema.jsonify(user)

if __name__ == '__main__':
  app.run(debug=True)
  
from flask import  Flask,request
import urllib
import json

app=Flask(__name__)
# @app.route('/api',defaults={'name':'','age':''})
@app.route('/api/<int:name>/<string:age>')
def getResponse(name,age):
    aadhar=re



# def f(name,age):
#     return "The details are "+str(name)+str(age)+'  '+' data'

if __name__ == '__main__':
  app.run(debug=True)
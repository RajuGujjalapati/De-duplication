# from datapreprocessing import Row_list
from flask import Flask, request, jsonify,Response,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
# from datapreprocessing import df
# from flask_restful import Resource, Api
import pymysql
app = Flask(__name__)
# api=Api(app)
# new_df = df
@app.route('/shakii/<name>')
def data(name):
    # res=request.args.get('name')
    # akm=request.args.get('age')
    # if res!=None:
    #     return "......"
    # else:
    #     return 'sas'
    try:
        if len(name)>=1:
            return name
        else:
            return ''
    except Exception as e:
        return "ehhehe"


if __name__ == '__main__':
  app.run(debug=True)
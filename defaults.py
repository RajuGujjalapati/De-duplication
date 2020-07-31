from flask import  Flask,request
from aadhar_pan_api import aadhar_check, pan_check
import urllib
import json

app=Flask(__name__)
# @app.route('/api',defaults={'name':'','age':''})
@app.route('/mainapi')
def getResponse():
    aadhar = request.args.get('aadhar')
    print("........................................",aadhar)
    pan = request.args.get('pan')
    js={"aadhar":aadhar,"pan":pan}
    # def aa(aadhar):
    if aadhar!=None:
        return aadhar_check(aadhar)
    # return "NOthing"
    # def pa(pan):
    elif pan!=None:
        return pan_check(pan)
    return "Nothing"
    # return "check"




# def f(name,age):
#     return "The details are "+str(name)+str(age)+'  '+' data'

if __name__ == '__main__':
  app.run(threaded=True)
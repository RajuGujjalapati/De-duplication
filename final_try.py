from flask import  Flask,request
from aadhar_pan_api import aadhar_check, pan_check

app=Flask(__name__)
@app.route('/try',defaults={'aadhar':'','pan':''})
@app.route('/try/<aadhar>/<pan>')
def getResponse(aadhar,pan):
    aadhar = request.args.get('aadhar')
    print("........................................",aadhar)
    pan = request.args.get('pan')
    js={"aadhar":aadhar,"pan":pan}
    # def aa(aadhar):
    if aadhar!='':
        return aadhar_check(aadhar)
import requests
from flask import Flask, request
from api import get_users
# req=r'http://127.0.0.1:5000/api/'
# dictio = {"aadhar":3424453546454}
# try:
#     if dictio!=None
# app= Flask(__name__)    
# def dic_test():
#     return {"aadhar":213242434324542,"pancard":"scjfo2315k"}

from collections import defaultdict
from proximityapi import *

# def default_dict():
#     return "The data is Not Present"

# dic=defaultdict(dic_test)

# dic["aadhar"]=213242434324542

# @app.route('/api',methods=['POST'])
# def json_data():
#     req=request.get_json()
#     return req
# from aadhar_pan_api import aadhar_check
d={"aadhar":213242434324542,"pancard":"scjfo2315k","fname":"prasad","lname":"j","gender":"male","cust_type":"customer"}
dict_data=defaultdict(int,d)
for data in dict_data:
    try:
        def return_aadhar():
            if (data['aadhar'])!=0:
                return aadhar_check(data['aadhar'])
            else:
                return "User Not Entered Aadhar Number"

    except Exception as e:
        print(e)
    try:
        def return_pan():
            if (data['pancard'])!=0:
                return pan_check(data['pancard'])
            else:
                return "User Not entered pan number"
    except Exception as e:
        print(e)
    try:
        def return_fname_lname():
            if ((data['fname']) and (data['lname']))!=0:
                return fname_lname((data['fname']),(data['lname']))
            else:
                return "User Not entered wrong url"
    except Exception as e:
        print(e)


    






# try:
#     aadhar=d['aadhar']
#     # d['aadhar']
# except KeyError:
#     d['name']=None
#     d['aadhar']=None
# # @app.route('/api/aadhar/<aadhar>',methods=['GET'])
# def aadh_check(aadhar):
#     res=aadhar_check(d['aadhar'])
 
#     return str(res)




if __name__ == '__main__':
    app.run(debug=True)
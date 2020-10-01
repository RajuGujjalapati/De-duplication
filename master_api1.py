import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from AadharApi import Aadhar
from PanApi import Pancard
from UserAPi import UserData
from DobApi import DobField
app = Flask(__name__)
api = Api(app)
df = pd.read_csv('./Duplicate_cust_data.csv', na_filter=False)
df['Matching_per']=''

# from API_probability_match_users1 import

formatting_data = {"fname":1,"lname":2,"gender":3,"aadhar":6,"pancard":5,"dob":4}
#Master api which calls all api's
class MasterApi(Resource):
    def get(self):
        #predefining some variables to return this data, when the user not entered req. input it returns output with this variables.
        user_dat_ ={'User':"No users data found in given input"}
        dob_ = {"Dob": "No dob data found with given input"}
        aadhar_= {"Aadhar" : "No Aadhar data found with given input"}
        pan_ = {"Pan" : "No Pan data found with given input"}
        #getting the input data.
        data = request.get_json()
        aadhar = data.get('aadhar')
        pancard = data.get('pancard')
        dob = data.get('dob')
        fname = data.get('firstName')
        lname = data.get('lastName')
        gender = data.get('gender')
        #if pan is not None, Then we are calling that api
        if pancard is not None:
            pan_ = Pancard.get(self)
        if aadhar is not None:
            aadhar_ = Aadhar.get(self)
        if dob is not None:
            dob_ = DobField.get(self)
        if (fname or lname or gender) is not None:
            user_dat_ = UserData.get(self)
        result_to_save = (user_dat_,dob_,aadhar_,pan_)
        return jsonify(result_to_save)
# if __name__ == '__main__':
#     api.add_resource(MasterApi, "/masterapi")
#     api.add_resource(UserData, "/user")
#     api.add_resource(Aadhar, "/aadhar")
#     api.add_resource(Pancard, "/pancard")
#     api.add_resource(DobField, "/dobfield")
#     app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)

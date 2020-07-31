# from datapreprocessing import Row_list
from flask import Flask, request, jsonify,Response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
from datapreprocessing import df
import pymysql
app = Flask(__name__)
new_df = df

def aadhar_check(aadhar):
    try:
        if len(aadhar)<=11 or len(aadhar)>=13:
            # raise "Input_Error"
            return ({aadhar:"Check the input and try again"})
        # Iterate over each row 
        store_aadhar=[]
        for index, rows in df.iterrows(): 
            print(rows.aadharNumber) 
            aadharData=[rows['firstName'],rows['lastName'],rows['gender'],rows['dob'],rows['location'],rows['clientType'],rows['aadharNumber'],rows['panCard']]
            store_aadhar.append(aadharData)
        #checking with aadhar data
        for data in (store_aadhar):
            if aadhar in data:
                firstName = data[0]
                lastName = data[1]
                gender=data[2]
                dob=data[3]
                location=data[4]
                clientType=data[5]
                aadharNumber=data[6]
                panCard=data[7]
                final_data_aadhar={"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard}
                print(final_data_aadhar)
                return final_data_aadhar
        else:
            return ({aadhar:"User aadhar details not found"})
    except TypeError:
        return ("No Details Found Please Check Again")

def pan_check(pancard):
    try:
        print("Checking with pan")
        if len(pancard)<=9 or len(pancard)>=11 :
            # raise "Input_Error"
            return ({pancard:"Check the input and try again"})
        store_pan=[]
        for index, rows in new_df.iterrows():
                my_list =[rows.firstName, rows.lastName, rows.gender, rows.dob, rows.location, rows.clientType, rows.aadharNumber, rows.panCard]
                store_pan.append(my_list)
        for data in store_pan:
            if pancard in data:
                firstName = data[0]
                lastName = data[1]
                gender=data[2]
                dob=data[3]
                location=data[4]
                clientType=data[5]
                aadharNumber=data[6]
                panCard=data[7]
                final_data_pan= {"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard}
                return final_data_pan               
        return ({pancard:"User pan details not Found"})
    except TypeError:
        return "No Details Found Please Check Again"


# @app.route('/api', defaults={'aadhar':'','pan':''})
@app.route('/api',methods=['GET'])
def aadhar_pan_check():
# if aadhar!='':
    aadhar=request.args.get('aadhar')
    pancard=request.args.get('pan')
    res=[]
    if aadhar!=None and pancard!=None:
        res.append((aadhar_check(aadhar), pan_check(pancard)))
        return str(res)
    elif pancard!=None:
        return str(pan_check(pancard))
    elif aadhar!=None:
        return str(aadhar_check(aadhar))
    else:
        return "Something wrong"

        
# print(df['panCard'])
# @app.route('/api/pan/<pancard>',methods=['GET'])
    # def pan_check(pancard):
    # elif pancard!=None:
        

if __name__ == '__main__':
  app.run(debug=True)
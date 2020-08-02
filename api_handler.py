# from aadhar_pan_api import *
from datapreprocessing import Row_list,df
from flask import Flask, request, jsonify,Response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
from fuzzywuzzy import fuzz
# from storing_info import *
import pymysql


app = Flask(__name__)
new_df = df
print(df)

formatting_data = {"fname":1,"lname":2,"gen":3,"location":4,"client_type":5,"aadhar":6,"pan":7,"dob":8}

def json_final_output_data():
    req_data = [ data for data in Row_list]
# preprocessed data from list to str
    final_data=[ [','.join(x)] for x in req_data]
    return final_data    

def requireddata(ret_ty):
    res_required=df.iloc[:,ret_ty]#This is like series or dataframe stores only required columns
    # print("XXXXXXXXXXXXXXXXXXXXX",res_required)
    list_data=[]
    for _, rows in res_required.iterrows(): 
            # Create list for the current row 
        sa=[]
        for i in res_required:
            sa.append(rows[i]) 
        list_data.append(sa)
        final_data=[','.join(x) for x in list_data]
    # print(sa)
    # print(",,,,,,,,,,,,,,,,,,,,,",final_data)
    # print(list_data)
    return final_data


def aadhar_check(aadhar):
    try:
        if len(aadhar)<=11 or len(aadhar)>=13:
            # raise "Input_Error"
            return ({aadhar:"Check the input and try again"})
        # Iterate over each row 
        store_aadhar=[]
        for index, rows in df.iterrows(): 
            # print(rows.aadharNumber) 
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
                # print(final_data_aadhar)
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

def preprocess_user_data(ret,ret_ty):
    user_input=str(','.join(ret))   
    print("Comparing  input:",user_input)
    sorted_data={}  
    for data in range(len(requireddata(ret_ty))):

        result_data = fuzz.token_sort_ratio(user_input,requireddata(ret_ty)[data])
        print("Matching Details:",requireddata(ret_ty)[data])
        #saving to dict     
        for x in range(len(json_final_output_data())):
            if data==x:
                sorted_data[result_data]=json_final_output_data()[data]
            else:
                continue
                # sorted_date[result_data]=[json_data()[d] for d in range(len(json_data())) ]
        #sorting data in reverse order
    result=sorted(sorted_data.items(),key=lambda x: x[0],reverse=True)
    result=dict(result)    
    print("..................",result)
    # print(sorted_data)
    conv_to_list=[]
    for per,data in (result.items()):
        joining_to_str = ','.join(data)
        conv_to_lis = joining_to_str.split(',')
        conv_to_list.append((conv_to_lis+[per]))
        print(conv_to_list)
    # res_s={"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per}
    res_s=[]
    for user_data in conv_to_list:
        firstName = user_data[0]
        lastName = user_data[1]
        gender = user_data[2]
        dob= user_data[3]
        location = user_data[4]
        clientType = user_data[5]
        aadharNumber = user_data[6]
        panCard = user_data[7]
        matching_per = user_data[8]
        data_to_store={"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per}
        res_s.append(data_to_store)
        # return jsonify({"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per})
    return str(res_s)
# @app.route('/api', defaults={'aadhar':'','pan':''})


@app.route('/api',methods=['GET'])
def aadhar_pan_users_check():
    data=request.get_json()
    aadhar=data.get('aadhar')
    pancard=data.get('pan')
    fname = data.get('firstName')
    lname = data.get('lastName')
    gender = data.get('gender')
    cust_type = data.get('cust_type')
    dob = data.get('dob')

    # aadhar=request.args.get('aadhar')
    # pancard=request.args.get('pan')
    # fname = request.args.get('firstname')
    # lname = request.args.get('lastname')
    # gender = request.args.get('gender')
    # cust_type = request.args.get('cust_type')
    # dob = request.args.get('dob')
    res=[]
    if aadhar!=None and pancard!=None:
        res.append((aadhar_check(aadhar), pan_check(pancard)))
        return str(res)
    elif pancard!=None:
        return str(pan_check(pancard))
    elif aadhar!=None:
        return str(aadhar_check(aadhar))
    cust_data= {"fname":fname,"lname":lname,"gen":gender,"client_type":cust_type,"dob":dob}

    ret = []
    ret_ty = []
    for key,value in cust_data.items():
        if value is not None:
            ret.append(value)
            ret_ty.append( formatting_data[key] )

    return preprocess_user_data(ret,ret_ty),aadhar_check(aadhar)
        # return jsonify({'aadhar': str(aadhar_check(aadhar))})
    # elif fname!=None and lname!=None and gender!=None and cust_type!=None and dob!=None and aadhar!=None and pancard!=None:
    #     ret=[fname,lname,gender,cust_type,dob, aadhar, pancard]
    #     print("DEBUGGGGGGGGGGGGGGGGGGGGGG")
    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['gen'],formatting_data['client_type'],formatting_data['dob'],formatting_data['aadhar'],formatting_data['pan']]
    #     # print(ret_ty)
    #     return (preprocess_user_data(ret,ret_ty),aadhar_check(aadhar),pan_check(pancard))

    # elif fname!=None and lname!=None and gender!=None and cust_type!=None:
    #     ret=[fname,lname,gender,cust_type]
    #     print("DEBUGGGGGGGGGGGGGGGGGGGGGG2222222222222222222")

    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['gen'],formatting_data['client_type']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty),aadhar_check(aadhar)
    # elif fname!=None and lname!=None and gender!=None:
    #     ret=[fname,lname,gender]
    #     print("DEBUGGGGGGGGGGGGGGGGG33333333333333333333333333333")

    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['gen']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty)
    # elif fname!=None and lname!=None and dob!=None:
    #     ret=[fname,lname,dob]
    #     print(1000*'3')
    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['dob']]
    #     return preprocess_user_data(ret,ret_ty),aadhar_check(aadhar)
    # elif fname!=None and lname!=None:
    #     ret=[fname,lname]
    #     print(1000*'2')
    #     ret_ty=[formatting_data['fname'],formatting_data['lname']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty)
    # elif fname!=None and lname!=None and cust_type!=None and dob!=None:
    #     ret=[fname,lname,gender,cust_type,dob] 
    #     print(1000*'4')
    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['client_type'],formatting_data['dob']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty),aadhar_check(aadhar)
    # elif fname!=None and lname!=None and gender!=None and cust_type!=None:
    #     ret=[fname,lname,gender,cust_type]
    #     print(1000*'5')
    #     ret_ty=[formatting_data['fname'],formatting_data['lname'],formatting_data['gen'],formatting_data['client_type']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty),aadhar_check(aadhar)
    # elif fname!=None:
    #     ret=[fname]
    #     print(type(fname))
    #     ret_ty=[formatting_data['fname']]
    #     # print(ret_ty)
    #     return preprocess_user_data(ret,ret_ty)
    # else:
    #     return "Something wrong"

        
# @app.route('/api',methods=['GET'])
# def json_example():

#     req = request.get_json()
#     fname=req['firstName']
#     lname = req['lastName']
#     gender = req['gender']
#     if fname!=None and lname!=None:
#         ret=[fname]
#         print(type(fname))
#         ret_ty=[formatting_data['fname']]
#         # print(ret_ty)
#         return preprocess_user_data(ret,ret_ty)
    # return preprocess_user_data(a,b)

if __name__ == '__main__':
  app.run(debug=True)
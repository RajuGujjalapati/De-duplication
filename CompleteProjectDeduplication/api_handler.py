# from aadhar_pan_api import *
from datapreprocessing import Row_list,df
from flask import Flask, request, jsonify,Response,render_template
from fuzzywuzzy import fuzz
import ast
import json
app = Flask(__name__)
new_df = df
print(df)
formatting_data = {"fname":1,"lname":2,"gen":3,"location":4,"client_type":5,"aadhar":6,"pancard":7,"dob":8}

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
        for _, rows in df.iterrows(): 
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
                final_data_aadhar={"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":100}
                return final_data_aadhar
        else:
            return ({aadhar:"User aadhar details not found"})
    except TypeError:
        return ({aadhar:"No aadhar Details Found Please Check Again"})
    except Exception as e:
        return e

def pan_check(pancard):
    try:
        print("Checking with pan")
        if len(pancard)<=9 or len(pancard)>=11 :
            # raise "Input_Error"
            return ({pancard:"Check the input  length and try again"})
        store_pan=[]
        for _, rows in new_df.iterrows():
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
                final_data_pan= {"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":100}
                # with open('personal.json', 'a+') as json_file:
                #     json.dump(final_data_pan, json_file)
                #     json_file.write(',')
                return final_data_pan            #c   
        return ({pancard:"User pan details not Found"})
    except TypeError:
        return {pancard:"No Pan Details Found Please Check Again"}

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
    # print("..................",result)
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
    dictionary = {i:d for i, d in enumerate(res_s)}
    return dictionary
        # return jsonify({"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per})
     #we can use dict gives tuple


@app.route('/api',methods=['GET'])
def aadhar_pan_users_check():
    data=request.get_json()
    aadhar=data.get('aadhar')
    pancard=data.get('pancard')

    cust_data = {
        'fname' : data.get('firstName'),
        'lname' : data.get('lastName'),
        'gen' : data.get('gender'),
        'client_type' : data.get('cust_type'),
        'dob' : data.get('dob'),
        'aadhar':data.get('aadhar'),#comment below two if you don't need to check with aadhar and pan
        'pancard':data.get('pancard')
    }

          
    ret = []
    ret_ty = []
    for key,value in cust_data.items():
        if value is not None:
            ret.append(value)
            ret_ty.append( formatting_data[key] ) 
    preprocess_result = preprocess_user_data(ret,ret_ty)
    
    if (pancard is not None) and (aadhar is not None):
        check_result = (aadhar_check(aadhar),pan_check(pancard))#'YOUR_CODE_HERE' # your_code_here
    
    elif (pancard is not None) and (aadhar is None):
        check_result = pan_check(pancard)
    elif (pancard is None) and (aadhar is not None):
        check_result = aadhar_check(aadhar)
    else:
        #use this incase if you dont need to compare with aadhar and pan in check_user dict
        # check_result = ''
        preprocess_result = preprocess_user_data(ret,ret_ty)
        with open("data.json", "a+") as f:
            json.dump(preprocess_result,f)
            f.write(",")
            f.write("\n")
        return preprocess_result
    
    # if len(ret) == 0:
    #     return (check_result)#use jsonify if you dont need to use aadhar and pan in local dict
    result_json_data=((preprocess_result, check_result))
    result_to_save = {i:v for i,v in enumerate(result_json_data)}
    with open("data.json", "a+") as f:
        json.dump((result_to_save),f)
        f.write(",")
        f.write("\n")
    return result_to_save
             

if __name__ == '__main__':
  app.run(debug=True)
import pandas as pd
from flask import Flask, request, jsonify,Response,render_template
from flask_restful import Api, Resource
from rapidfuzz import fuzz,utils
import ast
import json
df = pd.read_csv('./Duplicate_cust_data.csv', na_filter=False)
df['Matching_per'] = ''
# this helps in giving column numbers to get set of columns where not None.
formatting_data = {"fname":1,"lname":2,"gender":3,"aadhar":6,"pancard":5,"dob":4}
result_to_save=''


def record_store(dataf):
    df1_dob = pd.DataFrame(dataf,
                           columns=['cust_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'Pancard',
                                    'aadhar', 'Matching_per'])
    total_df_dob = df1_dob.sort_values('Matching_per', ascending=False)
    res_dob = total_df_dob.to_json(orient="records")
    res_dob = ast.literal_eval(res_dob)
    return res_dob
#userData which handles three columns data.
# class UserData(Resource):
#     def get(self):
#         data = request.get_json()
#         #taking only 3 inputs as per the requirement.
#         cust_data = {
#             'fname': data.get('firstName'),
#             'lname': data.get('lastName'),
#             'gender': data.get('gender')
#         }
#         ret = []  # saving values to pass it for deduplication.
#         ret_ty = []  # passing keys to ret_ty to get that values.
#         for key, value in cust_data.items():
#             if value is not None:
#                 ret.append(value)
#                 ret_ty.append(formatting_data[key])# getting the required numbers of particular column where input is not None
#                 #user input
#         user_input = str(','.join(ret))
#         processed_query = utils.default_process(user_input)
#         total_df =[]#saving json data.
#         for i in df.index:
#             res_required  = " ".join(map(str,df.iloc[i,ret_ty].apply(str).values))#converting rows to strings to match
#             processed_choice = utils.default_process(res_required)# allowing default process
#             result_data = fuzz.token_sort_ratio(processed_query, processed_choice)# applying ration func, which return matching percentages.
#             if result_data>50:
#                 df['Matching_per']=result_data
#                 # print(df.iloc[i,:].to_json())
#                 total_df.append(df.iloc[i,:].tolist())#converting all dataframe to json and appending
#                 # total_df.append(df.iloc[i, :])
#         if len(total_df) == 0: #if there is not matching ones we are returing this one.
#             return {"UserData": "No user data found greater than matching percentage"}
#         # converting all lists to dataframe, and sorting the data by "Match_Per column".
#         print(total_df)
#                                 #df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
#         # df1_dob = pd.DataFrame(total_df,columns=['cust_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'Pancard','aadhar', 'Matching_per'])
#         # total_df_dob = df1_dob.sort_values('Matching_per', ascending=False)
#         # res_dob = total_df_dob.to_json(orient="records")
#         # res_dob = ast.literal_eval(res_dob)# converting string of list to list
#         res_dob = record_store(total_df)
#         print(res_dob)
#         with open('file_check.txt','a') as f:
#             f.write(str(res_dob))
#         result_to_save = {i:v for i, v in enumerate(res_dob)}
#         return result_to_save
#

# Aadhar Api.
# class Aadhar(Resource):
#     def get(self):
#         data = request.get_json()
#         aadhar_details={
#         'aadhar' : data.get('aadhar')
#         }
#         for k,v in aadhar_details.items():
#             if v is not None:
#                 total_df = []
#                 for i in df.index:
#                     user_input = str(v)
#                     processed_query = utils.default_process(user_input)
#                     res_required  = " ".join(map(str,df.loc[i,[k]].apply(str).values))#converting rows to strings to match
#                     processed_choice = utils.default_process(res_required)
#                     result_data = fuzz.token_sort_ratio(processed_query, processed_choice)
#                     if result_data==100: #only checking for exact matchings
#                         df['Matching_per']=result_data
#                         # per_matching.append(result_data)
#                         total_df.append(df.iloc[i,:].tolist())
#          # if the length is 0, then returning this one.
#         if len(total_df) == 0:
#             return {"Aadhar": "No Exact Aadhar User found with given input"}
#         total_df = record_store(total_df)
#         result_to_save = {i: v for i, v in enumerate(total_df)}#CONVERTING ALL DICTS TO REAL JSONS.
#         return result_to_save # str is

#Pan Api
# class Pancard(Resource):
#     def get(self):
#         data = request.get_json()
#         pan_details={
#         'Pancard' : data.get('pancard')
#         }
#         for k,v in pan_details.items():
#             if v is not None:
#                 total_df=[]
#                 for i in df.index:
#                     user_input = str(v)
#                     processed_query = utils.default_process(user_input)
#                     res_required  = " ".join(map(str,df.loc[i,[k]].apply(str).values))#converting rows to strings to match
#                     processed_choice = utils.default_process(res_required)
#                     result_data = fuzz.token_sort_ratio(processed_query, processed_choice)
#                     if result_data==100:#collecting only exact matchings.
#                         df['Matching_per']=result_data
#                         total_df.append(df.iloc[i,:].tolist())#converting to json
#         if len(total_df) == 0:
#             return {"Pandata": "No Exact Pan User found with given input"}
#
#         total_df = record_store(total_df)
#
#         result_to_save = {i: v for i, v in enumerate(total_df)}
#         return (result_to_save)

#proximity Api
# class DobField(Resource):
#     def get(self):
#         data = request.get_json()
#         # considering req. keys for this api.
#         cust_data = {
#             'fname': data.get('firstName'),
#             'lname': data.get('lastName'),
#             'gender': data.get('gender'),
#             'dob': data.get('dob'),
#         }
#         ret = []  # saving values to pass it for deduplication.
#         ret_ty = []  # passing keys to ret_ty to get that values.
#         for key, value in cust_data.items():
#             if value is not None:
#                 ret.append(value)
#                 ret_ty.append(formatting_data[key])
#         user_input = str(','.join(ret))
#         processed_query = utils.default_process(user_input)
#         total_df_d = []#saving json data.
#         for i in df.index:
#             res_required = " ".join(map(str,df.iloc[i,ret_ty].apply(str).values))#converting rows to strings to match
#             processed_choice = utils.default_process(res_required)
#             result_data = fuzz.token_sort_ratio(processed_query, processed_choice)
#             if result_data>50:
#                 df['Matching_per'] = result_data
#                 total_df_d.append(df.iloc[i,:].tolist())
#         if len(total_df_d) == 0:
#             return {"Dob": "No User Dob matching with given input"}
#         total_df_d = record_store(total_df_d)
#         # df1_dob = pd.DataFrame(total_df_d,columns=['cust_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'Pancard','aadhar', 'Matching_per'])
#         # total_df_dob = df1_dob.sort_values('Matching_per', ascending=False)
#         # res_dob = total_df_dob.to_json(orient='records')
#         result_to_save = {i: v for i, v in enumerate(total_df_d)}
#         return (result_to_save)
        # return res_dob

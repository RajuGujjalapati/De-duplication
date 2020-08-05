from sqlalchemy import create_engine
import pymysql
import pandas as pd
import ast 
import json
import datetime
from fuzzywuzzy import process,fuzz
db_connection_str = 'mysql+pymysql://root:nani@localhost/flask_restapi'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM users', con=db_connection)
# print(df['dob'])
# print(df)
######################## Date preprocessing###################
df1=[]
try:
    for i in df['dob']:
        date_time_obj = datetime.datetime.strptime(str(i), "%Y-%m-%d").strftime("%d/%m/%Y")
        df1.append(date_time_obj)
except ValueError:
    print("Check Here for valueerror")
df1=pd.DataFrame({"dob":df1})#new dataframe
df.drop(['dob'],axis=1,inplace=True)
df=pd.concat([df, df1],axis=1)
# print(df)

# Create an empty list 
Row_list =[] 
# Iterate over each row 
for index, rows in df.iterrows(): 
    	# Create list for the current row 
	my_list =[rows.firstName, rows.lastName, rows.gender, rows.dob, rows.location, rows.clientType, rows.aadharNumber, rows.panCard] 
	# append the list to the final list 
	Row_list.append(my_list) 
print(Row_list) 


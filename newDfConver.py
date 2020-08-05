import pandas as pd
import datetime
from random_gen import aadhar_random_list,res
df = pd.read_excel(r'C:\Users\New\OneDrive\Desktop\Tesquirel Solutions\FlaskRestApi_SqlAlchemy\Client-Name-DOB-Data.xlsx')
ret= df['DOB'].dt.date
df1=[]
for i in ret:
    date_time_obj = datetime.datetime.strptime(str(i), "%Y-%m-%d").strftime("%d/%m/%Y")
    df1.append(date_time_obj)
df1=pd.DataFrame({"DOB":df1})#new dataframe
df.drop(['DOB'],axis=1,inplace=True)
df=pd.concat([df, df1],axis=1)
df2=pd.DataFrame({"AadharData":aadhar_random_list,"PanData":res})
df=pd.concat([df,df2],axis=1)
new_col = ["FirstName","LastName","Gender","DOB","AadharNumber","PanCard"]
df.columns = new_col

print(df)
Row_list =[] 
# Iterate over each row 
for index, rows in df.iterrows(): 
    	# Create list for the current row 
        # print(index,rows['FIRST'])
	my_list =[rows.FirstName,rows.AadharNumber,rows.LastName]
	# append the list to the final list 
	Row_list.append(my_list) 
print(Row_list)
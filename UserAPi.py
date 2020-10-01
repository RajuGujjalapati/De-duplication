from API_probability_match_users1 import *
app = Flask(__name__)
api = Api(app)
df = pd.read_csv('./Duplicate_cust_data.csv', na_filter=False)
df['Matching_per']=''
class UserData(Resource):
    def get(self):
        data = request.get_json()
        #taking only 3 inputs as per the requirement.
        cust_data = {
            'fname': data.get('firstName'),
            'lname': data.get('lastName'),
            'gender': data.get('gender')
        }
        ret = []  # saving values to pass it for deduplication.
        ret_ty = []  # passing keys to ret_ty to get that values.
        for key, value in cust_data.items():
            if value is not None:
                ret.append(value)
                ret_ty.append(formatting_data[key])# getting the required numbers of particular column where input is not None
                #user input
        user_input = str(','.join(ret))
        processed_query = utils.default_process(user_input)
        total_df =[]#saving json data.
        for i in df.index:
            res_required  = " ".join(map(str,df.iloc[i,ret_ty].apply(str).values))#converting rows to strings to match
            processed_choice = utils.default_process(res_required)# allowing default process
            result_data = fuzz.token_sort_ratio(processed_query, processed_choice)# applying ration func, which return matching percentages.
            if result_data>50:
                df['Matching_per']=result_data
                # print(df.iloc[i,:].to_json())
                total_df.append(df.iloc[i,:].tolist())#converting all dataframe to json and appending
                # total_df.append(df.iloc[i, :])
        if len(total_df) == 0: #if there is not matching ones we are returing this one.
            return {"UserData": "No user data found greater than matching percentage"}
        # converting all lists to dataframe, and sorting the data by "Match_Per column".
        print(total_df)
                                #df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
        # df1_dob = pd.DataFrame(total_df,columns=['cust_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'Pancard','aadhar', 'Matching_per'])
        # total_df_dob = df1_dob.sort_values('Matching_per', ascending=False)
        # res_dob = total_df_dob.to_json(orient="records")
        # res_dob = ast.literal_eval(res_dob)# converting string of list to list
        res_dob = record_store(total_df)
        print(res_dob)
        with open('file_check.txt','a') as f:
            f.write(str(res_dob))
        result_to_save = {i:v for i, v in enumerate(res_dob)}
        return result_to_save

if __name__ == '__main__':
    api.add_resource(UserData, "/user")
    app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)

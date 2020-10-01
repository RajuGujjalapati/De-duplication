from API_probability_match_users1 import *
app = Flask(__name__)
api = Api(app)
df = pd.read_csv('./Duplicate_cust_data.csv', na_filter=False)
df['Matching_per']=''
class DobField(Resource):
    def get(self):
        data = request.get_json()
        # considering req. keys for this api.
        cust_data = {
            'fname': data.get('firstName'),
            'lname': data.get('lastName'),
            'gender': data.get('gender'),
            'dob': data.get('dob'),
        }
        ret = []  # saving values to pass it for deduplication.
        ret_ty = []  # passing keys to ret_ty to get that values.
        for key, value in cust_data.items():
            if value is not None:
                ret.append(value)
                ret_ty.append(formatting_data[key])
        user_input = str(','.join(ret))
        processed_query = utils.default_process(user_input)
        total_df_d = []#saving json data.
        for i in df.index:
            res_required = " ".join(map(str,df.iloc[i,ret_ty].apply(str).values))#converting rows to strings to match
            processed_choice = utils.default_process(res_required)
            result_data = fuzz.token_sort_ratio(processed_query, processed_choice)
            if result_data > 50:
                df['Matching_per'] = result_data
                total_df_d.append(df.iloc[i,:].tolist())
        if len(total_df_d) == 0:
            return {"Dob": "No User Dob matching with given input"}
        total_df_d = record_store(total_df_d)
        # df1_dob = pd.DataFrame(total_df_d,columns=['cust_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'Pancard','aadhar', 'Matching_per'])
        # total_df_dob = df1_dob.sort_values('Matching_per', ascending=False)
        # res_dob = total_df_dob.to_json(orient='records')
        result_to_save = {i: v for i, v in enumerate(total_df_d)}
        return (result_to_save)
        # return res_dob

if __name__ == '__main__':
    api.add_resource(DobField, "/dobfield")
    app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)
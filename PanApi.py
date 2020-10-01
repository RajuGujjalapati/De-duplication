from API_probability_match_users1 import *
app = Flask(__name__)
api = Api(app)
df = pd.read_csv('./Duplicate_cust_data.csv', na_filter=False)
df['Matching_per']=''
class Pancard(Resource):
    def get(self):
        data = request.get_json()
        pan_details={
        'Pancard' : data.get('pancard')
        }
        for k,v in pan_details.items():
            if v is not None:
                total_df=[]
                for i in df.index:
                    user_input = str(v)
                    processed_query = utils.default_process(user_input)
                    res_required  = " ".join(map(str,df.loc[i,[k]].apply(str).values))#converting rows to strings to match
                    processed_choice = utils.default_process(res_required)
                    result_data = fuzz.token_sort_ratio(processed_query, processed_choice)
                    if result_data==100:#collecting only exact matchings.
                        df['Matching_per']=result_data
                        total_df.append(df.iloc[i,:].tolist())#converting to json
        if len(total_df) == 0:
            return {"Pandata": "No Exact Pan User found with given input"}

        total_df = record_store(total_df)

        result_to_save = {i: v for i, v in enumerate(total_df)}
        return (result_to_save)

if __name__ == '__main__':
    api.add_resource(Pancard, "/pancard")
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)
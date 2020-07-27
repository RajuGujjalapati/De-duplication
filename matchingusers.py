from aadhar_pan_api import aadhar_check,pan_check, app
from fuzzywuzzy import process,fuzz
from datapreprocessing import Row_list
import collections
# app = Flask(__name__)
@app.errorhandler(404)
def error(e):
  return "Please Check Your Url and fill user details accordingly"

@app.route('/api/userdata/<fname>/<lname>/<gender>/<cus_type>',methods=['GET'])
def userdataMatching(fname,lname,gender,cus_type=None):
    ret=fname,lname,gender,cus_type
    user_input=str(','.join(ret))   
    req_data = [ data[0:3]+data[5:6] for data in Row_list]
    final_data=[ [','.join(x)] for x in req_data]
    print(final_data)
    f={}
    for data in final_data:
        results = fuzz.token_sort_ratio(user_input,data)
        f[results]=data
    res=sorted(f.items(),key=lambda x: x[0],reverse=True)
    final_output = [f"The matching percentage is {str(i[0])} for input data {user_input} and compared data is {str(i[1])} '\n' " for i in res]
    return str(final_output)



# if __name__ == '__main__':
#   app.run(debug=True)
from aadhar_pan_api import aadhar_check,pan_check, app, request
from fuzzywuzzy import process,fuzz
from datapreprocessing import Row_list
import collections
# app = Flask(__name__)
@app.errorhandler(404)
def error(e):
  return "Please Check Your Url and fill user details accordingly"

def preprocess_user_data(ret):
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

# @app.route('/api',methods=['GET'])
# def userdataMatching():
#     fname = request.args.get('firstname')
#     lname = request.args.get('lastname')
#     gender = request.args.get('gender')
#     cust_type = request.args.get('cust_type')
#     dob = request.args.get('dob')

    # if fname!=None and lname!=None and gender!=None and cust_type!=None:
    #   ret=fname,lname,gender,cust_type
    #   return preprocess_user_data(ret)
      
    



if __name__ == '__main__':
  app.run(debug=True)
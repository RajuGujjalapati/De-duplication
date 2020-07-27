from matchingusers import *
@app.route('/api/proximityapi/<fname>/<lname>/<gender>/<dob>/<cus_type>',methods=['GET'])
def proximityMatching(fname,lname,gender,dob,cus_type):
    ret=fname,lname,gender,dob,cus_type
    user_input=str(','.join(ret))   
    req_data = [ data[0:6] for data in Row_list]
    final_data=[ [','.join(x)] for x in req_data]
    print(final_data)
    f={}
    for data in final_data:
        results = fuzz.token_sort_ratio(user_input,data)
        f[results]=data
    res=sorted(f.items(),key=lambda x: x[0],reverse=True)
    final_output = [f"The matching percentage is {str(i[0])} for input data {user_input} and compared data is {str(i[1])} '\n' " for i in res]
    return str(final_output)


if __name__ == '__main__':
    app.run(debug=True)
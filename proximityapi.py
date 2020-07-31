from matchingusers import *
from flask import jsonify
JSONIFY_PRETTYPRINT_REGULAR=False
def json_data():
    req_data = [ data for data in Row_list]
#preprocessed data from list to str
    final_data=[ [','.join(x)] for x in req_data]
    return final_data
def requireddata():
    req_data = [ data[0:6] for data in Row_list]
    #preprocessed data from list to str
    final_data=[ [','.join(x)] for x in req_data]
    return final_data
@app.route('/api/proximityapi/<fname>/<lname>/<gender>/<dob>/<cus_type>',methods=['GET'])
def proximityMatching(fname,lname,gender,dob,cus_type):
    ret=fname,lname,gender,dob,cus_type
    user_input=str(','.join(ret))   
    #getting only required columns    
    sorted_data={}  
    for data in range(len(requireddata())):
        result_data = fuzz.token_sort_ratio(user_input,requireddata()[data])
        #saving to dict     
        for x in range(len(json_data())):
            if data==x:
                sorted_data[result_data]=json_data()[data]
            else:
                continue
                # sorted_date[result_data]=[json_data()[d] for d in range(len(json_data())) ]
        #sorting data in reverse order
    result=sorted(sorted_data.items(),key=lambda x: x[0],reverse=True)    
    print(result)
    print(sorted_data)
    conv_to_list=[]
    for per,data in (sorted_data.items()):
        joining_to_str = ','.join(data)
        conv_to_lis = joining_to_str.split(',')
        conv_to_list.append(conv_to_lis)
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
        matching_per = per
        data_to_store={"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per}
        res_s.append(data_to_store)
        # return jsonify({"firstName":firstName,"lastName":lastName,"gender":gender,"dob":dob,"location":location,"clientType":clientType,"aadharNumber":aadharNumber,"panCard":panCard,"Matching Percentage":matching_per})
    return str(res_s)

                # final_output  =  [f"The matching percentage is {str(i[0])} for input data {user_input} and compared data is {str(i[1])} '\n' " for i in res]
                # out={user_input:[str(i[1])+"Matching per:"+str(i[0]) for i in res]}
        



if __name__ == '__main__': 
    app.run(debug=True)
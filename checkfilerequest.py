import json
def aadhar_():
    print( "aadhar success")

def pan_():
    print("pan successs")
def users_pre():
    print("hey success") 
var={'firstName': 'raju', 'lastName': 'g', 'gender': 'male', 'dob': '06/09/1997', 'location': 'tirupati', 'clientType':
'cust', 'aadhar': '123456789124'}
def res():
    for k,v in var.items():
    
        if ('aadhar' is not None) and ('pancard' is None):
            print("aadhar")
            res= aadhar_()
        if ('pancard' is not None) and ('aadhar' is None):
            print("pan")
            res =  pan_()

        if ('aadhar' and 'pancard')!=None:
            print("two")
            res = aadhar_(),pan_()

    return res      # return users_pre()
    
res()
        


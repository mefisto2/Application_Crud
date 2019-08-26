'''
@author: Whitebook
'''
from pymongo import mongo_client
#creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.Employeedata



#Function to insert data into mongo db
def insert():
    try:
        Employeeid = input('Enter Employee id: ')
        Employeename =  input('Enter Name: ')
        Employeeage= input('Enter age: ')
        Employeecountry = input('Enter Country: ')
        db.Employees.insert_one(
            {
            "id": Employeeid,
            "name": Employeename,
            "age" : Employeeage,
            "country" : Employeecountry
            })
        print('Inserted data successfully')
        
    except ImportError:
        platform_specific_module = None
        #print str(e)
        
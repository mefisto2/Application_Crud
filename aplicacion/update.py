'''
@author: Whitebook
'''
from pymongo import MongoClient
#creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


#Fuction to update record to mongo db
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')
        
        db.Employeees.update_one(
        {"id": criteria},
        {
            "$set": {
                "name": name,
                "age": age,
                "country": country
            }
        }
        )
        print("\nRecords updated successfully\n")
        
    except ImportError:
        platform_specific_module = None

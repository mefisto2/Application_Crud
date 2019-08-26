'''
@author: Whitebook
'''
from pymongo import MongoClient

#creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

#Function to update record to mongo db
def delete():
    try:
        criteria = input('\nEnter Employee id to delete\n')
        db.Employeees.delete_many({"id": criteria})
        print('\nDeletion succesful\n')
    except ImportError:
        platform_specific_module = None
        #print str(e)
        
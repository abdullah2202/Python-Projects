import pymongo
from creds import mongo_cred

myClient = pymongo.MongoClient(f"mongodb+srv://testuser:{mongo_cred.test_password}@cluster0.lbyme.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
myDB = myClient["sample_supplies"]
myCol = myDB["sales"]

# Show orders from Denver only
query = {"storeLocation" : "Denver"}
myRes = myCol.find(query)

# Only print orders with more than 5 items
for x in myRes:
    if(len(x["items"]) > 5):
        print(x["saleDate"],", Items:",len(x["items"]))




# print(myDB.list_collection_names())
# print(myClient.list_database_names())

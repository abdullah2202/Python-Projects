import pymongo
from creds import mongo_cred

# myClient = pymongo.MongoClient("mongodb+srv://testuser:@cluster0.lbyme.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


myClient = pymongo.MongoClient(f"mongodb+srv://testuser:PdvuIGdByw5aOfQ6@cluster0.lbyme.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
myDB = myClient["sample_supplies"]
myCol = myDB["sales"]
query = {"storeLocation" : "Denver"}
myRes = myCol.find(query)

# Only print orders with more than 9 items
for x in myRes:
    if(len(x["items"]) > 9):
        print(x["saleDate"],", Items:",len(x["items"]))




# print(myDB.list_collection_names())
# print(myClient.list_database_names())

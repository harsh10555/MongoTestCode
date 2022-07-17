import pymongo

client = pymongo.MongoClient("mongodb+srv://harshv:Austria105@harsh.passlct.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

'''client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)'''

d = {
    "name":"Harsh",
    "email" : "hvsrajput@gmail.com",
    "surname" : "Vardhan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
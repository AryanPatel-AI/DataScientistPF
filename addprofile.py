from pymongo import MongoClient

client = MongoClient("mongodb+srv://aryanpatel66871_db_user:IOEocBjcsqUkqYcP@cluster0.letklkj.mongodb.net/?appName=Cluster0")
mydb = client["portfolio"]
mycol = mydb["profiles"]
mycol.insert_one({
    "name": "Aryan patel",
    "mail": "aryanpatel66871@gmail.com",
})
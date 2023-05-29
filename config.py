import pymongo
import certifi

con_str = "mongodb+srv://fsdi:Test1234@cluster0.l6rt3zh.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore_ch35")
#from downloadbutton6 import mongofeed
from pymongo import MongoClient
from splittest import fun1

#call fun1 from file2.py
data=fun1()
print(data)

client = MongoClient("mongodb://localhost:27017");
print("Connection Successful")
mydb = client["TWEET"]
#mycol = mydb["TWEETCOLL"]
#mydb.mycol.delete_many({})
import json
#records = json.loads(tweets_df1.to_json(orient='records'))
data = json.loads(tweets_df1.to_json(orient='records'))
from datetime import datetime
Date = datetime.now().strftime('%d-%m-%Y')
dict={"Scraped Word":users_name, "Scraped Date":Date, "Data":data}
mydb.mycol.insert_many([dict])

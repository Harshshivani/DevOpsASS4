from flask import request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.todoDB
collection = db.items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = request.json
    collection.insert_one({
        "itemName": data["itemName"],
        "itemDescription": data["itemDescription"]
    })
    return {"status": "success"}

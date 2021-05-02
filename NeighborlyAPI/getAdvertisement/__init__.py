import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    print("------------->", id)

    if id:
        try:
            url = os.environ['DevMongoDBUrl']  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborly']
            collection = database['ads']

            query = {'_id': ObjectId(id)}
            # query = {'_id': id}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
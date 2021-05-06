import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    print(request, " is the request")
    if request:
        try:
            url = os.environ['DevMongoDBUrl']   # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborly']
            collection = database['ads']

            rec_id1 = collection.insert_one(eval(request))
            # rec_id1 = collection.insert_one(eval(request)

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
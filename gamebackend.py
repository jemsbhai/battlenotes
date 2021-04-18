import os
import pymongo
import json
import random
# import psycopg2
import hashlib
import time

from hashlib import sha256







def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()

    
    mongostr = os.environ.get('MONGOSTR')
    client = pymongo.MongoClient(mongostr)
    db = client["battlenotes"]


    retjson = {}

    action = request_json['action']

    if action == "attack":
        col = db.games
        for x in col.find():
            if int(x['id']) == int(request_json['gameid']):
                if 'p1hp' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"p1hp":request_json['p1hp']}})
                if 'p2hp' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"p2hp":request_json['p2hp']}})
                
                if 'value' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"value":request_json['value']}})
                
                difficulty = random.randint(1,10)
                col.update_one({"id": x['id']}, {"$set":{"lastaction":x['turn']}})

                if request_json['player'] == "player1" :
                    col.update_one({"id": x['id']}, {"$set":{"turn":x['defend2']}})
                
                if request_json['player'] == "player2" :
                    col.update_one({"id": x['id']}, {"$set":{"turn":x['defend1']}})



                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['difficulty'] = difficulty
                # retjson['diet'] = diet
                # retjson['allergy'] = allergy
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)


    if action == "defend":
        col = db.games
        for x in col.find():
            if int(x['id']) == int(request_json['gameid']):
                if 'p1hp' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"p1hp":request_json['p1hp']}})
                if 'p2hp' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"p2hp":request_json['p2hp']}})
                
                if 'value' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"value":request_json['value']}})
                
                difficulty = random.randint(1,10)
                col.update_one({"id": x['id']}, {"$set":{"lastaction":x['turn']}})

                if request_json['player'] == "player1" :
                    col.update_one({"id": x['id']}, {"$set":{"turn":x['attack1']}})
                
                if request_json['player'] == "player2" :
                    col.update_one({"id": x['id']}, {"$set":{"turn":x['attack2']}})



                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['difficulty'] = difficulty
                # retjson['diet'] = diet
                # retjson['allergy'] = allergy
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)




    if action == "getgamestatus":
        col = db.games
        for x in col.find():
            if int(x['id']) == int(request_json['gameid']):

                p1hp = x['p1hp']
                p2hp = x['p2hp']
                turn = x['turn']
                lastaction = x['lastaction']
                lastvalue = x['lastvalue']


                retjson = {}

                # retjson['dish'] = userid
                retjson['responsestatus'] = "success"
                retjson['p1hp'] = p1hp
                retjson['p2hp'] = p2hp
                retjson['turn'] = turn
                retjson['lastaction'] = lastaction
                retjson['lastvalue'] = lastvalue
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)




    if action == "addscore" :
        maxid = 1
        col = db.games
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        payload = {}

        uid = id 
        payload["id"] = id
        # payload["uid"] = request_json['uid']
        # payload["name"] = request_json['name']
        payload["userid"] = request_json['userid']
        payload["score"] = request_json['score']
        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['id'] = id

        return json.dumps(retjson)


    if action == "getmyscore":
        col = db.games
        for x in col.find():
            if x['userid'] == request_json['userid']:
                score = x['score']
                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['score'] = score

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)



    if action == "getallscores":
        col = db.games
        scores = []
        for x in col.find():
            entry = {}
            entry['userid'] = x['userid']
            entry['score'] = x['score']
            scores.append(entry)
            
        # retjson['dish'] = userid
        retjson['status'] = "success"
        retjson['scores'] = scores

        return json.dumps(retjson)
        retjson = {}




    if action == "getrandomactivity":
        col = db.scenes

        maxid = 0
        for x in col.find():
            maxid = int(x["id"])
        
        index = random.randint(1, maxid)

        for x in col.find():
            if x['id'] == str(index):
                sid = x['id']
                url = x['url']
                line = x['dialogue']
                retjson = {}

                # retjson['dish'] = userid
                retjson['url'] = url
                retjson['id'] = sid
                retjson['dialogue'] = line

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)    

    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr

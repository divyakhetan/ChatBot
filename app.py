from flask import Flask, request, jsonify
from flask import Flask, jsonify, request, make_response
import json
import requests
import os
URL = "http://numbersapi.com/"

app = Flask(__name__)
@app.route('/',  methods = ['GET'])


def home():
    return "hello from divya"

@app.route('/', methods = ['POST'])
def post():
    #req =request.data
    req = request.get_json(silent = True, force = False) #json to python dictionary
    print(req)
    intentName = req.get('queryResult').get('intent').get('displayName')
    if(intentName == 'Default Welcome Intent'):
        return jsonify({"fulfillmentText" : "Welcome!! You can now know cool facts about any number or year.You can try some of these!\n 1. Tell me something cool about *some number* \n 2. What is some math fact related to *some number* \n 3. Tell me something for which the year *some year* is famous for!! Enjoy! :)"})
    elif(intentName == 'numbers'):
        typeValue = req.get('queryResult').get("parameters").get("type")[0] #first element from list
        if(typeValue == "trivia"):
            number = int(req.get('queryResult').get("parameters").get("number"))
            url =  URL + str(number) + '/' + typeValue + '?json'
            response = requests.get(url)
            txt = json.loads(response.text)["text"]
            print(url)
            return jsonify({"fulfillmentText" : txt})
        elif(typeValue == "math"):
            number = int(req.get('queryResult').get("parameters").get("number"))
            url =  URL + str(number) + '/' + typeValue + '?json'
            response = requests.get(url)
            txt = json.loads(response.text)["text"]
            print(url)
            return jsonify({"fulfillmentText" : txt})
        elif(typeValue == "year"):
            number = int(req.get('queryResult').get("parameters").get("number"))
            url =  URL + str(number) + '/' + typeValue + '?json'
            response = requests.get(url)
            txt = json.loads(response.text)["text"]
            print(url)
            return jsonify({"fulfillmentText" : txt})
    #print(intentName)
    
    return jsonify(req)

if(__name__ == "__main__"):
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

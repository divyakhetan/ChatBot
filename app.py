from flask import Flask, request, jsonify
from flask import Flask, jsonify, request, make_response
import json
import requests
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
        return jsonify({"fulfillmentText" : "Welcome!! You can now know cool facts about any number!! Enjoy! :)"})
    elif(intentName == 'numbers'):
        typeValue = req.get('queryResult').get("parameters").get("type")
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

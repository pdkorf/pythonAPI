from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkDataDict(dataDict, functionName):
    if (functionName == 'add' or functionName == "subtract" or functionName == "multiply"):
        if "x" not in dataDict or "y" not in dataDict:
            return 301
        else:
            return 200
    elif (functionName == "devide"):
        if "x" not in dataDict or "y" not in dataDict:
            return 301
        elif (int(dataDict["y"]) == 0):
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #if i am here, then the resource Add was requested using the POST methods

        #step one: get posted data
        dataDict = request.get_json()

        #step 1b: check if right data is posted data
        status_code = checkDataDict(dataDict, "add")

        if (status_code != 200):
            retJson = {
                "Message": "Error: Not a valid entry",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here, status_code must be 200
        x = dataDict["x"]
        y = dataDict["y"]
        # x = int(x)
        # y = int(y)

        # if not (int(x) or int(y)):
        #     status_code = 303
        #     retJson = {
        #         "Message": "Error: not an integer",
        #         "Status Code": status_code
        #     }
        #     return jsonify(retJson)

        if (type(x) != int  or type(y) != int):
            if (int(x) or int(y)):
                status_code = 200
            else:
                status_code = 303
                retJson = {
                    "Message": "Error: not an integer",
                    "Status Code": status_code
                }
                return jsonify(retJson)

        x = int(x)
        y = int(y)

        #step two: add the posted data
        ret = x+y
        retMap = {
            "Message": ret,
            "Status Code": 200
            }

        #return the response data
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        #if i am here, then the resource subtract was requested using the POST methods

        #step one: get posted data
        dataDict = request.get_json()

        #step 1b: check if right data is posted data
        status_code = checkDataDict(dataDict, "subtract")

        if (status_code != 200):
            retJson = {
                "Message": "Error: Not a valid entry",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here, status_code must be 200
        x = dataDict["x"]
        y = dataDict["y"]

        if (type(x) != int  or type(y) != int):
            if (int(x) or int(y)):
                status_code = 200
            else:
                status_code = 303
                retJson = {
                    "Message": "Error: not an integer",
                    "Status Code": status_code
                }
                return jsonify(retJson)

        x = int(x)
        y = int(y)

        #step two: subtract the posted data
        ret = x-y
        retMap = {
            "Message": ret,
            "Status Code": 200
            }

        #return the response data
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #if i am here, then the resource multiply was requested using the POST methods

        #step one: get posted data
        dataDict = request.get_json()

        #step 1b: check if right data is posted data
        status_code = checkDataDict(dataDict, "multiply")

        if (status_code != 200):
            retJson = {
                "Message": "Error: Not a valid entry",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here, status_code must be 200
        x = dataDict["x"]
        y = dataDict["y"]

        if (type(x) != int  or type(y) != int):
            if (int(x) or int(y)):
                status_code = 200
            else:
                status_code = 303
                retJson = {
                    "Message": "Error: not an integer",
                    "Status Code": status_code
                }
                return jsonify(retJson)

        x = int(x)
        y = int(y)

        #step two: multiply the posted data
        ret = x*y
        retMap = {
            "Message": ret,
            "Status Code": 200
            }

        #return the response data
        return jsonify(retMap)

class Devide(Resource):
    def post(self):
        #if i am here, then the resource devide was requested using the POST methods

        #step one: get posted data
        dataDict = request.get_json()

        #step 1b: check if right data is posted data
        status_code = checkDataDict(dataDict, "devide")

        if (status_code != 200):
            retJson = {
                "Message": "Error: Not a valid entry",
                "Status Code": status_code
            }
            return jsonify(retJson)

        #if i am here, status_code must be 200
        x = dataDict["x"]
        y = dataDict["y"]

        if (type(x) != int  or type(y) != int):
            if (int(x) or int(y)):
                status_code = 200
            else:
                status_code = 303
                retJson = {
                    "Message": "Error: not an integer",
                    "Status Code": status_code
                }
                return jsonify(retJson)

        x = int(x)
        y = int(y)

        #step two: devide the posted data
        ret = (x*1.0) / y
        retMap = {
            "Message": ret,
            "Status Code": 200
            }

        #return the response data
        return jsonify(retMap)



api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Devide, "/devide")

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add_two_nums', methods=["POST"])
def add_2_nums():
    #get x and y from the posted data
    dataDict = request.get_json()

    if "x" not in dataDict:
        return "Hell shit --> No x in header", 305

    if "y" not in dataDict:
        return "WTF --> No y in header", 306

    x = dataDict["x"]
    y = dataDict["y"]
    #return jsonify(dataDict)

    #add z = x+y
    z = x + y

    #prepare a json {"z": z}
    rtnJSON = {
        "z": z
    }

    #return jsonify(map prepared)
    return jsonify(rtnJSON), 200

@app.route('/bye')
def bye():
    age = 10*4

    retJson = {
    'name': 'Paul',
    'leeftijd': age,
    'man' : True,
    'telefoons':[
            {
                'telefoonnaam': 'Iphone',
                'telefoonnummer': 1234
            },
            {
                'telefoonnaam': 'Samsung',
                'telefoonnummer': 1236
            }
        ]
    }
    #return "Bye world"

    return jsonify(retJson)

if __name__ == "__main__":
    #app.run(host="127.0.0.1", port=80)   ----> Komt pas bij deployment
    #app.run(host="127.0.0.1")
    app.run(host="0.0.0.0")

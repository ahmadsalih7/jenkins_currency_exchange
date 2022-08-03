from flask import Flask
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)

@app.route("/")
def homepage():
    return {'healthy' : True}


def get_info():
    HOSTNAME = os.getenv("HOSTNAME") or "LOCL"
    return f'{HOSTNAME} V1 {HOSTNAME[-4:]}'

exchange = [{
    "id": 10002,
    "from": "EUR",
    "to": "INR",
    "conversionMultiple": 75.00,
    "exchangeEnvironmentInfo": get_info() 
}]

class GetRate(Resource):
    def get(self, _from, to):
        for c in exchange:
            if c['from'] != _from or c['to'] != to:
                continue
            else:
                return c


api.add_resource(GetRate, '/currency-exchange/from/<string:_from>/to/<string:to>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))

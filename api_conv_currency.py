from flask import Flask, json, jsonify,make_response,Blueprint,request
import requests
from  functools import wraps
from flask_restplus import Resource, Api

app = Flask(__name__)
blueprint=Blueprint('api',__name__,url_prefix='/api')
api = Api(app)
#app=Api(app)
app.register_blueprint(blueprint)

    #@api.route('/convertor')
class convert_zar(Resource):
    @api.doc(security='apikey')
    def get(self):
        url = "https://ratesapi.io/api/latest?base=ZAR&symbols=USD,GBP,EUR"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data,parse_float=float)
        return jsonify(parsed)
#@api.route('/rates')
class convert_currencies(Resource):
    def get(self):
        curr = ['USD','GBP','EUR']
        parsed = []
        for i in range(len(curr)):
            url = "https://ratesapi.io/api/latest?base=" + curr[i] + "&symbols=ZAR"
            response = requests.get(url)
            data = response.text
            parsed.append(json.loads(data, parse_float=float))
        return jsonify(parsed)

class calc_EUR(Resource):
    def get(self):
        url = "https://ratesapi.io/api/latest?base=EUR&symbols=ZAR"
        response = requests.get(url)
        data = response.text
        parsed = (json.loads(data, parse_float=float))

        return jsonify(parsed)

class calc_USD(Resource):
    def get(self):
        url = "https://ratesapi.io/api/latest?base=USD&symbols=ZAR"
        response = requests.get(url)
        data = response.text
        parsed = (json.loads(data, parse_float=float))

        return jsonify(parsed)

class calc_GBP(Resource):
    def get(self):
        url = "https://ratesapi.io/api/latest?base=GBP&symbols=ZAR"
        response = requests.get(url)
        data = response.text
        parsed = (json.loads(data, parse_float=float))

        return jsonify(parsed)


class customResponse(Resource):
    def get(self):
        eur = calc_EUR().get()
        usd = calc_USD().get()
        gbp = calc_GBP().get()
        euro = eur.json
        dollar = usd.json
        pound = gbp.json

        return {
        "base": "ZAR",
        "date": euro['date'],
        "rates": {
            "EUR": euro['rates']['ZAR'],
            "GBP": pound['rates']['ZAR'],
            "USD": dollar['rates']['ZAR']
            }
        }


api.add_resource(convert_zar,'/convertor')
api.add_resource(convert_currencies,'/rates')
api.add_resource(calc_EUR, '/eur')
api.add_resource(calc_USD, '/usd')
api.add_resource(calc_GBP, '/gbp')
api.add_resource(customResponse, '/cust')

if __name__ == '__main__':
    app.run(debug=True)

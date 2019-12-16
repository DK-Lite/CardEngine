import json, argparse

from engine import *
from db import *
from flask import Flask
from flask_restfull import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1' : {'task' : 'Make Money'},
    'todo1' : {'task' : 'Make Money'},
    'todo1' : {'task' : 'Make Money'},
}

class Todo(Resource):
    def post(self):
        return {'status':'success'}



@app.route("/")
def main():
    arg = argparse.ArgumentParser()
    arg.add_argument('--from', type=int, default='-1')
    arg.add_argument('--to', type=int, default='-1')
    configs=arg.parse_args()

    engine = CardEngine()
    engine.add_card(CardKb(), loader.get_keys()['KB'])
    engine.add_card(CardSc(), loader.get_keys()['SC'])
    engine.add_card(CardUri(), loader.get_keys()['Uri'])
    engine.add_card(CardKbank(), loader.get_keys()['KBANK'])
    engine.add_card(CardHana(), loader.get_keys()['HANA'])
    engine.add_card(CardHyundai(), loader.get_keys()['HYUNDAI'])
    engine.add_card(CardSamsung(), loader.get_keys()['SAMSUNG'])
    engine.add_card(CardShinhan(), loader.get_keys()['SHINHAN'])
    engine.add_card(CardNongHyup(), loader.get_keys()['NONGHYUP'])
    

    with open("db/key/picka_connect.json") as json_file:
        info = json.load(json_file)

    db = PickaDB()
    db.connect(**info)
    datas = db.query('''SELECT * FROM sms_laws ORDER BY id ASC''')
    print(datas)

api.add_

if __name__=='__main__':
    app.run(debug=True)
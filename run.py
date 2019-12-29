from engine import *
from db import *
import json, argparse

def main():

    arg = argparse.ArgumentParser()
    arg.add_argument('--from_id', type=int, default='-1')
    arg.add_argument('--to_id', type=int, default='-1')
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
    datas = db.select('''SELECT * FROM sms_laws ORDER BY id ASC''')
    datas = db.filter(datas)
    datas = datas[configs.from_id : configs.to_id]

    for data in datas:
        try :
            output = engine.recognize(str(data['number']), data['sentence'])
            output['card_issuer'] = output['card_number']
            output['currency'] = 'KRW'
            output['sms_law_id'] = data['id']

            query = create_insert_query('sms_parseds', output)
            db.insert(query)

        except Exception as ex:
            print("Error : " + ex)
        
    # results = []
    # ...
    # with open("output.json", "w", encoding="utf-8") as make_file:
    #     json.dump(results, make_file, ensure_ascii=False, indent="\t")
    
if __name__ == "__main__":
    main()
    
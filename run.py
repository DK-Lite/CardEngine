from engine import *
from db import *
import json, argparse

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
    

    info = {
        'host' : '13.209.40.12',
        'ssh_username' : 'ubuntu',
        'ssh_private_key' : './db/key/picka_common.pem',
        'user' : 'root',
        'password':'vlrtmxbeldh1',
        'database':'picka_v1'
    }

    db = PickaDB()
    db.connect(**info)
    datas = db.query('''SELECT * FROM sms_laws ORDER BY id ASC''')
    print(datas)

    # results = []
    # for data in datas:
    #     results.append(
    #         engine.recognize(str(data['phone_number']), data['sms_sentence'])
    #     )


    # with open("output.json", "w", encoding="utf-8") as make_file:
    #     json.dump(results, make_file, ensure_ascii=False, indent="\t")

    
if __name__ == "__main__":
    main()
    
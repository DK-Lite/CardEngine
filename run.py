from engine import *
import json

def main():

    engine = CardEngine()
    engine.add_card(CardSamsung(), loader.get_keys()['SAMSUNG'])
    engine.add_card(CardHana(), loader.get_keys()['HANA'])

   
    results = []
    for data in loader.get_datas():
        result = engine.recognize(str(data['phone_number']), data['sms_sentence'])
        results.append(result)




    with open("output.json", "w", encoding="utf-8") as make_file:
        json.dump(results, make_file, ensure_ascii=False, indent="\t")

    
if __name__ == "__main__":
    main()
    
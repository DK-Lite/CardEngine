from engine import *
import json

def main():

    engine = CardEngine()
    engine.add_card(CardSamsung(), loader.get_keys()['SAMSUNG'])
    engine.add_card(CardHana(), loader.get_keys()['HANA'])




    # "[Web발신]\n삼성카드승인4909황*호\n05/29 09:56 원서접수\n25,800원 일시불"

    # result = engine.recognize('15888900', "[Web발신]\n삼성카드승인4909황*호\n05/29 09:56 원서접수\n25,800원 일시불")
    # print(result)


   
    results = []
    for data in loader.get_datas():
        result = engine.recognize(str(data['phone_number']), data['sms_sentence'])
        results.append(result)




    with open("output.json", "w", encoding="utf-8") as make_file:
        json.dump(results, make_file, ensure_ascii=False, indent="\t")

    
if __name__ == "__main__":
    main()
    
import os, sys, json

class Loader:
    keys = None
    test_data = []
    def __init__(self):
        with open("engine/data/card_key.json") as json_file:
            self.keys = json.load(json_file)   

        with open("engine/data/test_set/삼성카드_sms.json") as json_file:
           self.test_data += json.load(json_file)
        
        with open("engine/data/test_set/하나카드_sms.json") as json_file:
            self.test_data += json.load(json_file)


    def get_keys(self):
        return self.keys

    def get_datas(self):
        return self.test_data
        

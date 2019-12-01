
class CardEngine:
    cards = dict()
    def __init__(self):
        pass
    
    def add_card(self, card_name, keys):
        for key in keys:
            self.cards[key] = card_name

    def get_card(self, key):
        if not key in self.cards:
            raise KeyError

        return self.cards[key]

    def recognize(self, key, sms):
        try:
            card = self.get_card(key)
            return card(sms)
        except KeyError:
            #print('key is not found')
            return None

        


    
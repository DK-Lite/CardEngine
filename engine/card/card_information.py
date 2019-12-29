
class CardInformation():
    builder = None

    def __init__(self):
        self.builder = { 
            'card_number' : "None", 
            'card_holder' : "None", 
            'date' : "None", 
            'time' : "None", 
            'amount' : "None",
            'use' : "None"
        }
        pass

    def set_number(self, number):
        if number is not None:
            self.builder['card_number'] = number
        return self
    
    def set_holder(self, holder):
        if holder is not None:
            self.builder['card_holder'] = holder
        return self
    def set_date(self, date):
        if date is not None:
            self.builder['date'] = date
        return self
    
    def set_time(self, time):
        if time is not None:
            self.builder['time'] = time
        return self
    
    def set_amount(self, amount):
        if amount is not None:
            self.builder['amount'] = amount
        return self
    
    # Not implemented
    def set_use(self, use):
        if use is not None:
            self.builder['use'] = "None"
        
        return self
    
    def get(self):
        return self.builder



    
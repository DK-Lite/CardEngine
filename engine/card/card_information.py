
class CardInformation():
    builder = None
    
    def __init__(self):
        self.builder = { 
            'number' : None, 
            'holder' : None, 
            'date' : None, 
            'time' : None, 
            'amount' : None,
            'use' : None
        }
        pass

    def set_number(self, number):
        self.builder['number'] = number
        return self
    
    def set_holder(self, holder):
        self.builder['holder'] = holder
        return self
    def set_date(self, date):
        self.builder['date'] = date
        return self
    
    def set_time(self, time):
        self.builder['time'] = time
        return self
    
    def set_amount(self, amount):
        self.builder['amount'] = amount
        return self
    
    def set_use(self, use):
        self.builder['use'] = use
        return self
    
    def get(self):
        return self.builder



    
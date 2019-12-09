import re
from .module import CardModule
from .card_information import CardInformation

class CardSamsung(CardModule):
    def __init__(self):
        pass

    def get_number(self, sms):
        re_number = re.findall(r"\[*삼성+[카드]*[승인]*\]*[0-9]*", sms)
        try:
            return re_number[0]
        except Exception as e:
            return None

    def get_holder(self, sms):
        re_holder = re.findall(r'[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+[*][ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+', sms)
        try:
            return re_holder[0]
        except Exception as e:
            return None

    def get_date(self, sms):
        re_date = re.findall(r'[0-9]*/[0-9]*', sms)
        try:
            return re_date[0]
        except Exception as e:
            return None

    def get_time(self, sms):
        re_time = re.findall(r'[0-9]*:[0-9]*', sms)
        try:
            return re_time[0]
        except Exception as e:
            return None

    def get_amount(self, sms):
        re_money = re.findall(r'[0-9]*,*[0-9]*,*[0-9]*,*[0-9]+원+', sms)
        try:
            return ''.join([ i for i in re_money[0] if i.isdigit()])
        except Exception as e:
            return None

    def get_use(self, sms):
        re_money = re.findall(r'[0-9]*,*[0-9]*,*[0-9]*,*[0-9]+원+', sms)
        try:
            return ''.join([ i for i in re_money[1] if i.isdigit()])
        except Exception as e:
            return None

    def recognize(self, sms):

        number = self.get_number(sms)
        holder = self.get_holder(sms)
        date = self.get_date(sms)
        time = self.get_time(sms)
        amount = self.get_amount(sms)
        use = self.get_use(sms)

        print(number, holder, date, time, amount, use)

        return CardInformation() \
        .set_number(number) \
        .set_holder(holder) \
        .set_date(date) \
        .set_time(time) \
        .set_amount(amount) \
        .set_use(use) \
        .get()


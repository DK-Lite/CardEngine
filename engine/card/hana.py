import re
from .module import CardModule
from .card_information import CardInformation

class CardHana(CardModule):
    def __init__(self):
        pass

    def recognize(self, sms):

        re_number = re.findall(r"하나+[카드]*[\(0-9\)\*]*", sms)
        re_holder = re.findall(r'[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+[*][ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+', sms)
        re_date = re.findall(r'[0-9]*/[0-9]*', sms)
        re_time = re.findall(r'[0-9]*:[0-9]*', sms)
        re_money = re.findall(r'[0-9]*,*[0-9]*,*[0-9]*,*[0-9]*원+', sms)

        try:
            number = re_number[0]
            holder = re_holder[0]
            date = re_date[0]
            time = re_time[0]
            amount = ''.join([ i for i in re_money[0] if i.isdigit()])
            use = ''.join([ i for i in re_money[1] if i.isdigit()])

            return CardInformation() \
            .set_number(number) \
            .set_holder(holder) \
            .set_date(date) \
            .set_time(time) \
            .set_amount(amount) \
            .set_use(use) \
            .get()

        except Exception as e:
            return CardInformation().get()


import re
from .module import CardModule
from .card_information import CardInformation

class CardShinhan(CardModule):
    def __init__(self):
        pass
#[Web발신]\n우리(9269)체크승인\n정*상님\n74,800원\n08/29 21:47\nMANO BEER
#[Web발신]\n우리(9269)승인\n정*상님\n151,530원\n06/30 18:35\n(주)이마트왕십리점\n54TOP적립예정
#[Web발신]\n우리(9303)체크승인\n정*상님\n77,000원\n08/19 13:01\n(주)데일리
#[Web발신]\n[체크.승인]\n12,000원\n우리카드(4*4*)정*상님\n04/09 14:08\n지급가능액36,891원\n박남준미용실

    def get_number(self, sms):
        re_number = re.findall(r"(\[*[신]+[한]+[체크]*[법인]*[승인]*\]*[카드]*\(*[0-9\*]*\))|([ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]*[*]*[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+[님]?)*\(+[0-9\*]*\)+", sms) # SMS에서 카드리스트 뽑는거
        try:
            return re_number[0]
        except Exception as e:
            return None

    def get_holder(self, sms):
        re_holder = re.findall(r'([ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+[*]+[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+)|([ㄱ-ㅎ|ㅏ-ㅣ|가-힣]*[님]+)', sms)
        try:
            return re_holder[0]
        except Exception as e:
            return None

    def get_date(self, sms):
        re_date = re.findall(r'[0-9]*[/]+[0-9]*', sms)
        try:
            return re_date[0]
        except Exception as e:
            return None

    def get_time(self, sms):
        re_time = re.findall(r'[0-9]*:[0-5][0-9]', sms)
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


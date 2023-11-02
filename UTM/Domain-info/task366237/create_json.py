from json import dumps, loads
from uuid import uuid4
from datetime import datetime
from random import randint

class Create:
    def __init__(self):
        self.result = self.open_file()

    def open_file(self):
        with open('/home/kornilov/PycharmProjects/pythonProject/UTM/Domain-info/task366237/test.json') as f:
            jsons = loads(f.read())
        return jsons

    def set_uuid(self):
        self.result['id'] = str(uuid4())
        self.result['requestId'] = str(uuid4())
        self.result['responseId'] = str(uuid4())
        self.result['messageId'] = str(uuid4())
        return self

    def set_docid(self, id):
        self.result['requestContent']['epgu']['orderID'] = id
        print(self.result['requestContent']['epgu']['orderID'])
        return self

    def set_date(self):
        self.result['requestTimestamp'] = str(datetime.now())
        self.result['updateTimestamp'] = str(datetime.now())
        self.result['requestContent']['epgu']['statementDate'] = str(datetime.now().strftime("%Y-%m-%d"))
        return self

    def set_serviceId(self, id):
        self.result['serviceId'] = id
        return self

    def set_typeDoc(self, doc):
        self.result['requestContent']['informationEgais']['typeDoc'] = doc
        print(self.result['requestContent']['informationEgais']['typeDoc'])
        return self

    def set_fsrar(self, fsrar):
        self.result['requestContent']['informationEgais']['fsrarId'] = fsrar
        print(self.result['requestContent']['informationEgais']['fsrarId'])
        return self

    def set_inn(self, inn):
        self.result['requestContent']['applicant']['ul']['inn'] = inn
        print(self.result['requestContent']['applicant']['ul']['inn'])
        return self

    def set_kpp(self, kpp):
        self.result['requestContent']['applicant']['ul']['kpp'] = kpp
        print(self.result['requestContent']['applicant']['ul']['kpp'])
        return self


# n = Create()
# n.set_uuid().set_date().set_docid(randint(11111111, 99999999)).set_serviceId('info-epgu').set_typeDoc('Сведения о поставке').set_fsrar('010000000047').set_inn('7714698320').set_kpp('271744622')
# print(dumps(n.result, ensure_ascii=False))

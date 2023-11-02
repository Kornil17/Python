import json
from uuid import uuid4
from datetime import datetime
class Create:
    def __init__(self):
        self.result = self.open_file()
    def open_file(self):
        with open('test.json') as f:
            jsons = json.loads(f.read())
        return jsons
    def set_uuid(self):
        self.result['id'] = str(uuid4())
        self.result['requestId'] =  str(uuid4())
        self.result['responseId'] =  str(uuid4())
        self.result['messageId'] =  str(uuid4())
        return self
    def set_docid(self, id):
        self.result['requestContent']['epgu']['orderID'] = id
        print(self.result['requestContent']['epgu']['orderID'])
        return self
    def set_date(self):
        self.result['requestTimestamp'] = str(datetime.now())
        self.result['updateTimestamp'] = str(datetime.now())
        return self
    def set_serviceId(self, id):
        self.result['serviceId'] = id
        return self
    def set_typeDoc(self, doc):
        self.result['requestContent']['correctionEgais']['documentsCorrection'][0]['typeDoc'] = doc
        print(self.result['requestContent']['correctionEgais']['documentsCorrection'][0]['typeDoc'])
        return  self
    def set_inn(self, inn):
        self.result['requestContent']['applicant']['ul']['inn'] = inn
        print(self.result['requestContent']['applicant']['ul']['inn'])
        return self
    def set_kpp(self, kpp):
        self.result['requestContent']['applicant']['ul']['kpp'] = kpp
        print(self.result['requestContent']['applicant']['ul']['kpp'])
        return self
    def set_fsrar(self, fsrar):
        self.result['requestContent']['correctionEgais']['documentsCorrection'][0]['fsrarId'] = fsrar
        print(self.result['requestContent']['correctionEgais']['documentsCorrection'][0]['fsrarId'])
        return self
    def set_branch(self, branch):
        self.result['requestContent']['correctionEgais']['branch'] = branch
        print(self.result['requestContent']['correctionEgais']['branch'])
        return self

# n = Create()
# n.set_uuid().set_date().set_docid('999999').set_serviceId('brewers-service').set_typeDoc(1).set_fsrar(1).set_inn(1).set_kpp(1).set_branch('test')
# print(n.result)






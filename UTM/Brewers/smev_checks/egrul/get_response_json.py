import json
import os
from uuid import uuid4
from datetime import datetime
class JSON:
    """formed json for egrul response"""

    def __init__(self, name):
        file_names = {'rf':'egrul_rf.json', 'fias':'egrul_fias.json', 'op':'fns_op.json'}
        self.result = self.open_file(file_names[name])

    def open_file(self, file_name):
        with open(f"/home/kornilov/PycharmProjects/pythonProject/UTM/Brewers/smev_checks/egrul/{file_name}") as f:
            jsons = json.loads(f.read())
        return jsons

    def set_uuid(self, js):
        self.result['id'] = str(uuid4())
        self.result['requestId'] = str(js['requestId'])
        self.result['responseId'] = str(uuid4())
        self.result['messageId'] = str(uuid4())
        self.result['requestContent']['requestId'] = str(js['requestId'])
        return self
    def set_date(self):
        self.result['requestTimestamp'] = str(datetime.now())
        self.result['updateTimestamp'] = str(datetime.now())
        return self
    def set_client_number(self, js):
        self.result['clientInternalNumber'] = js['clientInternalNumber']
        return self

# test = JSON('op')
# js = {"requestId":"007461f1-6291-4095-aa51-a49482d702cc","clientInternalNumber":"3500138728"}
# test.set_uuid(js).set_date().set_client_number(js)
# print(json.dumps(test.result, ensure_ascii=False))


import json


class Parse:
    """class for parsing json from egrul"""

    def __init__(self):
        self.result = {}

    def parse_json(self, js):
        self.result['requestId'] = json.loads(js)['requestId']
        self.result['clientInternalNumber'] = json.loads(js)['clientInternalNumber']
        return self.result


# d = '{"serviceId":"brewers-service","requestId":"007461f1-6291-4095-aa51-a49482d702cc","clientInternalNumber":"3500138728","requestType":"EGRUL","requestContent":{"requestId":"007461f1-6291-4095-aa51-a49482d702cc","innUl":"4951739576"}}'
# test = Parse()
# test.parse_json(d)
# print(json.dumps(test.result, ensure_ascii=False))



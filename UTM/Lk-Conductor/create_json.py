import json

# params = {'filter': '1','page': '1','size': '1','sort': '1',}
class Create:
    """form json for lk-conductor /dashboard/conductor/consideration/with-pagination"""
    def __init__(self):
        self.params = {}
    def set_filter(self, value):
        self.params['filter'] = value
        return self
    def set_page(self, value):
        self.params['page'] = value
        return self
    def set_size(self, value):
        self.params['size'] = value
        return self
    def set_sort(self, value):
        self.params['sort'] = value
        return self
    def clear(self):
        self.params.clear()
        return self

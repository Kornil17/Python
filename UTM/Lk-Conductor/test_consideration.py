import pytest
import requests
from fixtures import test_json, test_request
# command for runnig test in remote server "python -m pytest"

# @pytest.mark.production
@pytest.mark.parametrize('filter, page, size, sort', [
    (1, 1, 1, 1)
])
def test_values(filter, page, size, sort, test_json, test_request):
    var = test_json
    var.set_filter(filter).set_page(page).set_size(size).set_sort(sort)
    print(var.json)
    req = test_request
    response = requests.get(
        req.path,
        params=var.params,
        headers=req.headers,
    )
    print(response.text, response.status_code)
    assert response.status_code == 200


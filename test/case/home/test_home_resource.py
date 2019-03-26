# Created by Dylan
import sys, os, pytest

sys.path.append(os.getcwd() + "/lib/httpMethod")
from Http import Http

http = Http()

# Put API paths here
home_page_path = '/'


@pytest.mark.test
class TestHomeResource:
    def test_get_home_api_1(self):
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_get_home_api_2(self):
        res = http.get()
        assert res.status_code == 200

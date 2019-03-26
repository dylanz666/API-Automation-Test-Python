# Created by Dylan
import sys, os, pytest

sys.path.append(os.getcwd() + "/lib/httpMethod/")
sys.path.append(os.getcwd() + "/lib/common/")
sys.path.append(os.getcwd() + "/lib/utils/")
sys.path.append(os.getcwd() + "/lib/sql/")
from ReadConfig import ReadConfig

read_config = ReadConfig()
sys.path.append('{0}/test/testData/{1}/'.format(os.getcwd(), read_config.read_default_env()))
sys.path.append('{0}/test/requestBody/{1}/'.format(os.getcwd(), read_config.read_default_env()))
from Http import Http
from RandomUtil import random_util
from DateUtil import date_util
from DesUtil import des_util
from QueryDbUtil import query_db_util
from login import login
import home_resource_data
import home_resource_body
import CARRIER

print(random_util.get_random_string())
print(date_util.get_timestamp())
print(des_util.base64_encode("dylan"))

print(home_resource_data.get_data("id"))  # get test data from home_resource_data.py
print(home_resource_body.get_body("getHomeAddress_positive"))  # get request body from home_resource_body.py
print(CARRIER.get_sql("getCarrierInfo"))  # get sql form CARRIER.py

http = Http()
# put API paths here
home_page_path = '/'


# Using fixture:(add fixture function name to your test function)
# Hook for each run.This will be called only once for each run.Not required.
@pytest.fixture(scope='session')
def setup_session(request):
    def teardown_session():
        query_db_util.query("test sql for session")

    request.addfinalizer(teardown_session)
    query_db_util.get_connection()
    login()


# Hook for module, this will be call only once for this file.Not required.
@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        query_db_util.query("test sql for module")

    request.addfinalizer(teardown_module)
    query_db_util.get_connection()
    login()


# Hook for each class.If there are several class in this file,then each of them will call this hook.Not required.
@pytest.fixture(scope='class')
def setup_class(request):
    def teardown_class():
        query_db_util.query("test sql for class")

    request.addfinalizer(teardown_class)
    query_db_util.get_connection()
    login()


# Hook for each function.This will be called for both of test_demo_1 and test_demo_2.Not required.
@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        query_db_util.query("test sql for function")

    request.addfinalizer(teardown_function)
    query_db_util.get_connection()
    login()


@pytest.mark.demo
class TestDemo:
    def test_demo_1(self, setup_session):  # Using session hook
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_2(self, setup_session):  # Using session hook, this actually not call session hook again
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_3(self, setup_module):  # Using module hook
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_4(self, setup_module):  # Using module hook, this actually not call module hook again
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_5(self, setup_class):  # Using class hook
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_6(self, setup_class):  # Using class hook, this actually not call class hook again
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_7(self, setup_function):  # Using function hook
        res = http.get(home_page_path)
        assert res.status_code == 200

    def test_demo_8(self, setup_function):  # Using function hook again
        res = http.get(home_page_path)
        assert res.status_code == 200

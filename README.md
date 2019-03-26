# API-Automation-Test-Python(Python3 + pytest + requests)

# Installation
* __SoftWares that need to be installed initially__: Git,Python 3.x.
* __Sync the code by__: git clone https://github.com/dylanzhang123456/API-Automation-Test-Python.git
* __Install dependencies__: Go to the project and use the command below

```bash
    $ pip install -r requirements.txt
```  
# Project structure
* __lib/asserts__: Some static source, such as .xlsx/.txt/.png/.jpg/.json and so on.
* __lib/common__: The implements of common actions.
* __lib/config__: Configurations for each environment.
* __lib/httpMethod__: The implements of calling APIs.
* __lib/log__: Saved logs that created by logging automatically.
* __lib/sql__: Centralization of sql
* __lib/utils__: Some utils.
* __test/case__: Test cases.
* __test/requestBody__: Http requestBody divided by env.
* __test/testData__: Test data divided by env.

# How to write a test case
* __Please find some clues in test/case/test_demo.py__

# How to run the test?
* __Run all test cases__: 
```bash
    $ pytest --html=report.html
``` 
* __Run a folder's cases__:(Such as "test" folder) 
```bash
    $ pytest test --html=report.html
``` 
* __Run a file's cases__: 
```bash
    $ pytest test/case/home/test_home_resource.py --html=report.html
``` 
* __Run specific class__: 
Add a flag like "@pytest.mark.demo" to the head of your test class/test function and execute below command in project:
```bash
    $ pytest -v -m "demo" --html=report.html
``` 
or:
```bash
    $ pytest -q -m "demo" --html=report.html
``` 
or:
```bash
    $ pytest -s -m "demo" --html=report.html
``` 
or:
```bash
    $ pytest -x -m "demo" --html=report.html
``` 
And run for not demo class:
```bash
    $ pytest -v -m "not demo" --html=report.html
``` 
What are "-v","-q","-s","-x" for: https://www.jianshu.com/p/a754e3d47671

# Specification
```markdown
1.The test file name must start with "test_";
2.The test class name must start with "Test" and should not have int() in it;
3.The test function name must start with "test_"
```

# How to clean pycache
Use below command in your project:
```bash
    $ py.cleanup -p
``` 

# How to update requirements
Use below command in your project:
```bash
    $ pip freeze > requirements.txt
``` 

# Learn more
* __pytest__: 
https://www.jianshu.com/p/a754e3d47671
https://docs.pytest.org/en/latest/index.html
* __pytest-html__: https://pypi.org/project/pytest-html/
* __requests__: http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
* __pycmd__: https://pypi.org/project/pycmd/
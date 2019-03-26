# Created by Dylan
import sys, os, requests

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "../lib/utils"))

from ReadConfig import ReadConfig
from Logger import Logger

read_config = ReadConfig()


class Http:
    def __int__(self, path, headers={}, params={}, data={}, files={}):
        global host, time_out, default_header
        config = read_config.read_config()
        host = config["host"]
        time_out = config["time_out"]
        default_header = config["default_header"]
        self.url = self.get_url(path)
        self.headers = dict(default_header).update(headers)
        self.params = params
        self.data = data
        self.files = files
        self.time_out = time_out

    @staticmethod
    def get_url(path):
        return host + path

    # defined http get method
    def get(self, path="/", headers={}, params={}):
        self.__int__(path=path, headers=headers, params=params)
        try:
            res = requests.get(url=self.url, headers=self.headers, params=self.params,
                               timeout=float(self.time_out))
            Logger.info("[Get] ", self.url, ' ', res.status_code)
            return res
        except TimeoutError:
            print('Time out!')
            return None

    # defined http post method
    def post(self, path="/", headers={}, data={}, files={}):
        self.__int__(path=path, headers=headers, data=data, files=files)
        try:
            res = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                timeout=float(self.time_out))
            Logger.info("[Post] ", self.url, ' ', res.status_code)
            return res
        except TimeoutError:
            print('Time out!')
            return None

    # defined put get method
    def put(self, path="/", headers={}, data={}, files={}):
        self.__int__(path=path, headers=headers, data=data, files=files)
        try:
            res = requests.put(self.url, headers=self.headers, data=self.data, files=self.files,
                               timeout=float(self.time_out))
            Logger.info("[Put] ", self.url, ' ', res.status_code)
            return res
        except TimeoutError:
            print('Time out!')
            return None

    # defined http delete method
    def delete(self, path="/", headers={}):
        self.__int__(path=path, headers=headers)
        try:
            res = requests.delete(self.url, headers=self.headers, timeout=float(self.time_out))
            Logger.info("[Delete] ", self.url, ' ', res.status_code)
            return res
        except TimeoutError:
            print('Time out!')
            return None

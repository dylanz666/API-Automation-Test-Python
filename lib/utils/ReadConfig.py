# Created by Dylan
import json, os


class ReadConfig:
    def __int__(self):
        self.config_folder = os.getcwd() + '/lib/config/'

    def read_config(self):
        env = self.read_default_env()
        config_file = self.config_folder + '{0}.json'.format(env)
        with open(config_file, 'r') as f:
            return json.load(f)

    def read_default_env(self):
        self.__int__()
        system_env = os.getenv("PY_ENV")
        if (system_env == None):
            with open(self.config_folder + 'default.json', 'r') as f:
                return json.load(f)["env"]
        else:
            return system_env

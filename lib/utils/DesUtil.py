# Created by Dylan
import base64


class des_util:
    def __int__(self):
        print("des_util")

    @staticmethod
    def base64_encode(text):
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def base64_decode(text):
        return base64.b64decode(text).decode()

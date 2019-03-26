body = {
    "getHomeAddress_positive": {
        "username": "pr-test",
        "area": "XM"
    }
}


def get_body(key):
    if (key == None):
        return None
    else:
        return body[key]

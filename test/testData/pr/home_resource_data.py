data = {
    "id": 123
}


def get_data(key):
    if (key == None):
        return None
    else:
        return data[key]

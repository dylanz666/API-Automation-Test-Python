sql = {
    "getCarrierInfo": "SELECT * FROM CARRIER"
}


def get_sql(key):
    if (key == None):
        return None
    else:
        return sql[key]

import decimal


def decimalize(data):
    try:
        if type(data) in [int, float]:
            return decimal.Decimal(data)
        elif type(data) == list:
            for ii, _ in enumerate(data):
                data[ii] = decimal.Decimal(data[ii])
            return data
        elif type(data) == tuple:
            data = list(data)
            for ii, _ in enumerate(data):
                data[ii] = decimal.Decimal(data[ii])
            return data
        else:
            raise TypeError
    except TypeError:
        print('Error')
    return -1

# with functools' reduce

from functools import reduce

def process_data(data):
    return reduce(lambda x,y: x * y, [a - b for a,b in data])


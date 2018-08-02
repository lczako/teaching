# Let's implement reduce for real

def process_data(data):
    return reduce(lambda x,y: x * y, [a - b for a,b in data])

def reduce(func, items):

    def rec_func(func, a, b):
        if len(b) > 1:
            return func(a, rec_func(func, b[0], b[1:]))
        else:
            return func(a, b[0])

    return rec_func(func, items[0], items[1:])

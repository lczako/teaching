# Let's implement reduce

def process_data(data):
    return reduce([a - b for a,b in data])

def reduce(items):

    def multiply(a, b):
        print(a, b)
        if len(b) > 1:
            return a * multiply(b[0], b[1:])
        else:
            return a * b[0]

    return multiply(items[0], items[1:])

print(reduce([1, 2, 3]))


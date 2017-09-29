data = [10, 20, 30.0, 40, 50]

def mean():
    sum = 0
    for item in data:
        sum += item
    return sum / len(data)

def data(n):
    s = f'{n:02d}'
    with open('../input/' + s + '.txt', 'r') as f:
        data = f.read()
    return data

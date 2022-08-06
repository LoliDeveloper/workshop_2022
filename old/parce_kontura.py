def parce_kontur(filepath):
    file = open(filepath, 'r')
    data = file.read().split()
    x = []
    y = []
    z = []
    for i in range(len(data)):
        if i % 3 == 0:
            x.append(data[i])
        elif i % 3 == 1:
            y.append(data[i])
        else:
            z.append(data[i])
    return (x,y,z)

from parce_kontura import parce_kontur
import matplotlib.pyplot as plt
import sys
import numpy as np
well_vertices = np.load("well_vertices.npy", "r")

if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = input("Input kontur-filepath")
data = (parce_kontur(filepath))

print("Data file: ", filepath)
print("Data len: ", len(data), ' ', len(data[0]))

x = list(map(float, data[0]))
y = list(map(float, data[1]))
z = list(map(float, data[2]))
#print(x)
#print(y)
fig, (ax1) = plt.subplots()
ax1.plot([x[i] for i in range(len(x))], [y[i] for i in range(len(y))])
ax1.scatter([z[0] for z in well_vertices], [z[1] for z in well_vertices])

y_max = max(y)
x_max = max(x)
y_min = min(y)
x_min = min(x)
a_square = max(y_max - y_min, x_max - x_min)
x_min_coord = x_min
x_max_coord = x_min_coord + a_square
y_min_coord = y_min
y_max_coord = y_min_coord + a_square
plt.xlim(x_min_coord, x_max_coord)
plt.ylim(y_min_coord, y_max_coord)
np.save("boundary", [[x[i],y[i]] for i in range(len(x))])
plt.show()

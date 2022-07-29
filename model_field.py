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
np.save("boundary", [[x[i],y[i]] for i in range(len(x))])
plt.show()

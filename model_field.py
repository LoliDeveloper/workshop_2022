from parce_kontura import parce_kontur
import matplotlib.pyplot as plt
import sys
if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = input("Input konur-filepath")
data = (parce_kontur(filepath))

print("Data file: ",filepath)
print("Data len: ", len(data), ' ', len(data[0]))

x = list(map(float, data[0]))
y = list(map(float, data[1]))
z = list(map(float, data[2]))
print(x)
print(y)
fig, (ax1) = plt.subplots()
ax1.plot([x[i] for i in range(len(x))], [y[i] for i in range(len(y))])
ax1.scatter([x[0] + 20], [y[0]+30])

plt.show()

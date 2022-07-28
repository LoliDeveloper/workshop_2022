import numpy as np
from myplot import plot_verticles
f = open("welltracks.txt", "r")

well = []
data = f.read().split(";")
for track in data:
    track = [x for x in track.splitlines() if (len(x.split())>0 and x.split()[0][0].isnumeric())]
    
    list_lines = []
    for line in track:
        list_lines.append(list(map(float, line.split())))
    if list_lines != []:
        well.append(list_lines)

#print(well) # well[id][line][arg_id]
list_v = []
for x in well:
    list_v.append(x[0][:3])
for l in list_v:
    l[2] = l[2] *( -1)
vertices = np.array(list_v)

print(vertices)

plot_verticles(vertices=vertices, isosurf = True)


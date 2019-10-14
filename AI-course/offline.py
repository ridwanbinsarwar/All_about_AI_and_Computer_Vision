import csv
import math
data = list(csv.reader(open('movies_recommendation_data.csv')))
training = []
test = []
names = {}
i = int(len(data)*(70/100))

for j in range(0, i):
    training.append(data[j])
for j in range(i, len(data)):
    test.append(data[j])
c = 0

for i in data:
    if c == 0:
        c += 1
        continue
    names[int(i[0])] = i[1]


dis = [{}for i in range(200)]
for j in test:
    src = int(j[0])

    lp = 0
    for k in training:
        lp += 1
        if lp == 1:
            continue
        value = 0
        target = 0

        for l in range(2, len(k)):
            target = int(k[0])
            if l == 2:
                value += (float(k[l]) - float(j[l])) ** 2
                continue
            value += (int(k[l])-int(j[l]))*(int(k[l])-int(j[l]))
        value = float(math.sqrt(value))

        dic = dis[src]
        dic[target] = value
        dis[src] = dic


sorted_x = []
for i in range(0, len(dis)):
    sorted_x.append(dict(sorted(dis[i].items(), key=lambda kv: kv[1])))


lis = list(sorted_x[46].keys())
print("5 similar movies of  ", names[46])
for i in range(0, 5):
    print(names[int(lis[i])])


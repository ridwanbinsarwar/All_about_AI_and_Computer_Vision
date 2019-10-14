import math
import pandas as pd

data = pd.read_csv("movies_recommendation_data.csv")

train = data[0:28]
test = data[28:]



allDis = {}

for i in range(0,len(train)):
    imdDef = math.pow((float(test["IMDB Rating"][29]) - float(train["IMDB Rating"][i])),2)
    bioDef = math.pow((float(test["Biography"][29]) - float(train["Biography"][i])), 2)
    drmDef = math.pow((float(test["Drama"][29]) - float(train["Drama"][i])), 2)
    thrDef = math.pow((float(test["Thriller"][29]) - float(train["Thriller"][i])), 2)
    cmdDef = math.pow((float(test["Comedy"][29]) - float(train["Comedy"][i])), 2)
    criDef = math.pow((float(test["Crime"][29]) - float(train["Crime"][i])), 2)
    mysDef = math.pow((float(test["Mystery"][29]) - float(train["Mystery"][i])), 2)
    hisDef = math.pow((float(test["History"][29]) - float(train["History"][i])), 2)

    dis = math.sqrt(imdDef + bioDef + drmDef + thrDef + cmdDef + criDef + mysDef + hisDef)
    allDis[train["Movie Name"][i]] = dis

sortedAns = sorted(allDis.items(), key=lambda x: x[1])
sortedAns = sortedAns[:5]

print("Recommend 5 Movie: ")
for i in sortedAns:
    print(i[0]);

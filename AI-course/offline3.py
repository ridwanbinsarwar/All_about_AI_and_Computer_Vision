import math
import random
from cmath import exp
from math import inf

import pandas as pd
import numpy as np
def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))     # Define sigmoid function
    sig = np.minimum(sig, 0.9999)  # Set upper bound
    sig = np.maximum(sig, 0.0001)  # Set lower bound
    return sig

def cal_hypothesis(df, p):
    s = 1 * p[0]
    k = 1
    for j in range(0, len(df) - 3):
        # print(p[k], df[j], s)
        s += (p[k] * df[j])
        k += 1

    # if s * (-1) < -36:
    #     s = - 36

    E = sigmoid(s)

    j = (int(df[7]) * np.log(E)) + ((1 - int(df[7])) * np.log(1 - E))
    # print(E,j,s,df[7])
    return j, E


data = pd.read_csv('diabetes2.csv')
train = data[:int(len(data) * 0.7)]
test = data.tail(len(data) - len(train))
print(len(test))
param = [1]

train.columns = ['a','b','c','d','e','f','g','h']
train['J'] = 0
train['E'] = 0
# train.insert(8, 'J', 0)
prevj = 0


c = 'a'
for i in range(0,7):
    mn = train[c].mean()
    maxi = train[c].max()
    mini = train[c].min()
    train[c] -= mn
    train[c] /= (maxi-mini)
    c = chr(ord(c) + 1)
    print(c)


for i in range(0, 7):
    param.append(random.randint(1, 5))

print(param)
for l in range(1, 10000):
    for i in range(0, len(train)):
        j, e = cal_hypothesis(train.iloc[i], param)
        train.loc[i, 'J'] = j
        train.loc[i, 'E'] = e

    jTheta = train['J'].sum() * (-(1 / len(train)))
    # train.to_csv('output.csv')
    print(jTheta, abs(prevj-jTheta))
    # print(train.iloc[0])
    if jTheta < 0.11199999 or abs(prevj-jTheta) < 0.001119999999:
        print("reached", jTheta)
        break
    else:
        newParam = []
        for i in range(0, 8):
            cSum = 0
            if i == 0:
                (param[0] - (0.09 / len(train)))
            for j in range(0, len(train)):
                if i == 0:
                    cSum += (train.iloc[j]['E'] - train.iloc[j][7]) * 1
                else:
                    # print((train.iloc[j]['E'] , train.iloc[j][7]) , train.iloc[j][i-1] , j, i)
                    cSum += (train.iloc[j]['E'] - train.iloc[j][7]) * train.iloc[j][i-1]
            v = param[i] - (0.09 / len(train)) * cSum
            newParam.append(v)
        param = newParam
        prevj = jTheta
        # print(param)
p = 0
for i in range(0,len(test)):
    j, e = cal_hypothesis(train.iloc[i], param)
    if e >= 0.5:
        if train.iloc[i][7] == 1:
            print(train.iloc[i][7], 1)
            p += 1
    else:
        if train.iloc[i][7] == 0:
            print(train.iloc[i][7], 0)
            p += 1

print(p)

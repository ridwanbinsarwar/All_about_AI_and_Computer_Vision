import math
import random
import numpy as np
import pandas

data = pandas.read_csv('Mall_Customers.csv');
c1 = [random.randint(1, 100) for i in range(3)]
c2 = [random.randint(1, 100) for i in range(3)]
c3 = [random.randint(1, 100) for i in range(3)]
data.columns = ['x', 'y', 'z']
data['color'] = 'z'

while True:

    data['diff1'] = (pow((data['x'] - c1[0]), 2) + pow((data['y'] - c1[1]), 2)
                     + pow((data['z'] - c1[2]), 2))
    data['diff2'] = (pow((data['x'] - c2[0]), 2) + pow((data['y'] - c2[1]), 2)
                     + pow((data['z'] - c2[2]), 2))
    data['diff3'] = (pow((data['x'] - c3[0]), 2) + pow((data['y'] - c3[1]), 2)
                     + pow((data['z'] - c3[2]), 2))

    data['c1_diff'] = np.sqrt(data['diff1'])
    data['c2_diff'] = np.sqrt(data['diff2'])
    data['c3_diff'] = np.sqrt(data['diff3'])

    for i in range(0,len(data['c1_diff'])):
        mini = min(min(data['c1_diff'][i], data['c2_diff'][i]), data['c3_diff'][i])
        if i == 2:
            print(mini, data['c2_diff'][i])
        if mini == data['c1_diff'][i]:
            data.loc[i , 'color'] = 'r'
        elif mini == data['c2_diff'][i]:
            data.loc[i, 'color'] = 'g'
        else:
            data.loc[i, 'color'] = 'b'

    dataR = data.loc[data['color'] == 'r']
    newC1x = dataR['x'].mean()
    newC1y = dataR['y'].mean()
    newC1z = dataR['z'].mean()

    newC1 = [newC1x, newC1y, newC1z]

    dataR = data.loc[data['color'] == 'g']
    newC1x = dataR['x'].mean()
    newC1y = dataR['y'].mean()
    newC1z = dataR['z'].mean()

    newC2 = [newC1x, newC1y, newC1z]

    dataR = data.loc[data['color'] == 'b']
    newC1x = dataR['x'].mean()
    newC1y = dataR['y'].mean()
    newC1z = dataR['z'].mean()

    newC3 = [newC1x, newC1y, newC1z]

    if c1 == newC1 and c2 == newC2 and c3 == newC3:
        break
    else:
        c1 = newC1
        c2 = newC2
        c3 = newC3


print(c1,c2,c3)
data.to_csv('output.csv')

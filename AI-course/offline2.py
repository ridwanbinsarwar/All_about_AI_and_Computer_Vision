import pandas
train = pandas.read_csv('train.csv')
test = pandas.read_csv('test.csv')
train['xy'] = train['x']*train['y']
train['x2'] = train['x']*train['x']
xy = train['xy'].sum() - (len(train['x'])*train['x'].mean()*train['y'].mean())
xx = train['x2'].sum() - (len(train['x'])*(train['x'].mean()**2))
b1 = xy/xx
b0 = train['y'].mean() - (b1*train['x'].mean())
test['y1'] = b0 + (test['x']*b1)
test['diff'] = (test['y'] - test['y1'])**2
error = test['diff'].sum() / (2*len(test['x']))
print(error)

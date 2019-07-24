import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

features = ['MinTemp','MaxTemp','WindGustSpeed']
data = pd.read_csv('dataset.csv', names = features) 
data = data.replace('No', 0)
data = data.replace('Yes', 1)
labels=['RainTomorrow']
data1= pd.read_csv('dataset.csv', names=labels) 
y= data1

X_train, X_test, y_train, y_test = train_test_split( data, y, test_size = 0.20, random_state = 0)
x=X_train

def tanh(x): 
        return np.tanh(x) 
def der_tanh(x):
    return 1.0 - tanh(x) ** 2
def train_values():
    w1=np.random.randn()
    w2=np.random.randn()
    w3=np.random.randn()
    b=np.random.randn()
    learning_rate=0.2
    iters=30000
    for i in range(0,iters):
        j=np.random.randint(len(x))
        inputs = data[j]
        m=tanh(w1*inputs[0]+w2*inputs[1]+w3*inputs[2]+b)
        predicted=inputs[3]
        cost=((x-predicted)**2)
        dcost_dpred = 2*cost
        dpred_dz = der_tanh(m)
        dz_dw1=inputs[0]
        dz_dw2=inputs[1]
        dz_dw3=inputs[2]
        dz_db=1
        dcost_dz=dcost_dpred*dpred_dz
        dw1=dcost_dz*dz_dw1
        dw2=dcost_dz*dz_dw2
        dw3=dcost_dz*dz_dw3
        db=dcost_dz*dz_db
        w1=w1-learning_rate+dw1
        w2=w2-learning_rate+dw2
        w3=w3-learning_rate+dw3
        b=b-learning_rate+db
    return w1,w2,w3,b,cost
w1, w2,w3, b,cost = train_values()
lists=X_test
pred = w1 * lists[0]+ w2 * lists[1]+ w3*lists[2]+b
out=tanh(pred)
if out<0.5:
    print("\nNo rain tomorrow\n")
else:
    print("\nit will rain tomorrow\n")
print("Acuuracy:",metrics.accuracy_score(y_test,out))

    

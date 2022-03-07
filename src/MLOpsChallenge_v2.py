#!/usr/bin/env python
# coding: utf-8

# In[13]:


from numpyencoder import NumpyEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import numpy as np
import json

def create_prediction():
    x = np.array([6, 16, 26, 36, 46, 56, 64]).reshape((-1, 1))
    y = np.array([4, 18, 20, 22, 24, 35, 45])
    model = LinearRegression().fit(x, y)
    prediction = model.predict(np.array([1]).reshape((-1,1)))
    score_r2 = model.score(x, y)
    return generate_reponse(score_r2, prediction)


# In[14]:


def generate_reponse(score_r2,prediction):
    output = {}
    output['score_r2'] = score_r2
    output['output'] =  json.loads(json.dumps(prediction, cls=NumpyEncoder))
    return output


# In[15]:


def main():
    res = create_prediction()
    print(json.dumps(res))


# In[16]:


if __name__ == '__main__':
    main()


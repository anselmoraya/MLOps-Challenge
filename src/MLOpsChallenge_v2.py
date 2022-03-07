#!/usr/bin/env python
# coding: utf-8

# In[17]:


from numpyencoder import NumpyEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
import json

def predict_linear():
    x = np.array([6, 16, 26, 36, 46, 56, 64]).reshape((-1, 1))
    y = np.array([4, 18, 20, 22, 24, 35, 45])
    model = LinearRegression().fit(x, y)
    return model.predict(np.array([1]).reshape((-1,1)))


# In[2]:


def serialize_results(numpy_array):
    return json.dumps(numpy_array, cls=NumpyEncoder)


# In[3]:


def main():
    res = predict_linear()
    res_json = serialize_results(res)
    print(res_json)


# In[4]:


if __name__ == '__main__':
    main()


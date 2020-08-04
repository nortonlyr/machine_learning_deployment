import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('hiring.csv')
# print(dataset)

dataset['experience'].fillna(0, inplace=True)
#print(dataset)

dataset['test_score(out of 10)'].fillna(dataset['test_score(out of 10)'].mean(), inplace=True)
# print(dataset)

X = dataset.iloc[:, :3]

# convert the strings into interger values
def convert_str_to_int(word):
    word_dict = {'zero': 0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
                 'eleven':11, 'twelve':12, 0: 0}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x : convert_str_to_int(x))

y = dataset.iloc[:, -1]

# In this small dataset, the entire data will be trained, no splitting training and test set

# sklean linear gresion model 
regressor = LinearRegression()

# fitting model with training data
regressor.fit(X,y)

# dump this model into pkl file
pickle.dump(regressor, open('model.pkl', 'wb'))

# load model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2, 9, 6]]))

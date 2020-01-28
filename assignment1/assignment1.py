#!/usr/bin/env python3

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

data = pd.read_csv('./house_prices.csv')

data.describe(include='all')

# Density of Home Prices

sale_price = data.loc[:, ['Price']]

ax = sale_price.plot.kde()
ax.set_xlabel('Price (USD)');

# Data Exploration

cols = ['Rooms', 'SellerG', 'Postcode', 'YearBuilt']
for col in cols:
    x = data.loc[:, [col]]
    y = data.loc[:,['Price']]
    df = pd.concat([x,y], axis=1, sort=False)
    plt.scatter(df[col], df['Price']);
    plt.xlabel(col);
    plt.ylabel('Price');
    plt.show();

# Multivariable Linear Regression Prediction

x = data[['Rooms', 'Postcode']].to_numpy().reshape(-1,2)
y = data[['Price']]

clf = linear_model.LinearRegression()
model = clf.fit(x, y);

new_rooms = 5
new_postcode = 3044

import locale
locale.setlocale(locale.LC_ALL, '')

prediction = model.predict([[new_rooms, new_postcode]])[0][0]
print(''.join(['The Predicted price is: ',locale.currency(prediction, grouping=True)]))




#!/usr/bin/env python3

import pandas as pd

df_tips = pd.read_csv("./data/tips/tips.csv")
df_tips.head(10)
df_tips.describe()
df_tips.describe(include='all')

# Assign independent(y) and dependent(x) variables
x = df_tips.loc[:, ['total_bill', 'size']]
y = df_tips.loc[:, ['tip']]

# Fit linear regression model
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(x,y)

print(regr.score(x,y))

# Display regression model
print("Intercept: ", regr.intercept_)
print("Coefficient: ", regr.coef_)

# Generate a new prediction

new_total_bill = 45.25
new_size = 4

regr.predict([[new_total_bill, new_size]])

# Explore data


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("demand.csv")
data = data.dropna()

fig = px.scatter(data, x="Units Sold", y="Total Price",
                 size='Units Sold')
# fig.show()

# print(data.corr()

correlations = data.corr(method='pearson')
plt.figure(figsize=(15, 12))
sns.heatmap(correlations, cmap="coolwarm", annot=True)
# plt.show()

x = data[["Total Price", "Base Price"]]
y = data["Units Sold"]

xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)

model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)

features = np.array([[150.00, 500.00]])
print(model.predict(features))
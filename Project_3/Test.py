import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3

z = np.array([1, 2])
print(z.shape)
print(X.shape)
print(y.shape)

reg = LinearRegression().fit(X, y)
reg.score(X, y)

import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    )
]
layout = go.Layout(
    title='Global Font',
    font=dict(family='Courier New, monospace', size=18, color='#7f7f7f')
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='global-font')
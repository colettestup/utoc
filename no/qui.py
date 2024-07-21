import plotly.graph_objects as go

x = [0, 1, 2, 3]
y = [5, 10, 15, 20]

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', line_shape='hv'))
fig.update_layout(title='Step Curve Example', xaxis_title='X-axis', yaxis_title='Y-axis')
fig.show()

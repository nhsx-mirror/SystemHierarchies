import plotly.express as px

data = dict(number = [100, 40, 20, 19], stage = ["Trusts", "CCG", "ICS", "Regions"])

fig = px.funnel(data, x= 'number', y = 'stage')
fig.show()
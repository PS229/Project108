import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("project.csv")
fig = ff.create_distplot([df["Avg"].tolist()], ["Averages"], show_hist=False)
fig.show()
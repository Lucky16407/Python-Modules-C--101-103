import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
ef = px.bar(df, x = "Country", y = "InternetUsers", color = "Country")
ef.show()
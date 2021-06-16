import pandas as pd 
import plotly.express as px

df = pd.read_csv("data.csv")
rf = px.scatter(df,x = "Country", y = "InternetUsers", color = "Country", size = "Percentage", size_max  = 60)

rf.show()
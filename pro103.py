import plotly.express as px
import pandas as pd
df=pd.read_csv("PRO-103.csv")
fig=px.scatter(df,x="date",y="cases",color="country",title='No.of covid cases')
fig.show()
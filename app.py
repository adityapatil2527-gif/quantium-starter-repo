import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# load processed dataset
df = pd.read_csv("formatted_sales.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
)

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)

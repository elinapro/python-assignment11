import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')

# print first and last 10 rows
print(df.head(10))
print(df.tail(10))

# clean the data and convert 'strength' to a float
df['strength'] = df['strength'].str.replace('+', '', regex=False)
df['strength'] = pd.to_numeric(df['strength'], errors='coerce')

# plot
fig = px.scatter(
    df,
    x='frequency',
    y='strength',
    color='direction',
    title='Wind Strength vs. Frequency',
    labels={'strength': 'Wind Strength', 'frequency': 'Wind Frequency'}
)

# HTML
fig.write_html("wind.html")
print("Plot saved to wind.html")

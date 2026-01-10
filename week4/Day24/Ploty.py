# Import necessary libraries
import plotly.express as px
import pandas as pd
import dash
from dash import dcc, html

# Plotly: A Powerful Data Visualization Library
# Plotly is an open-source Python library used for creating interactive, visually appealing charts and graphs.
# It helps users to explore data through features like zooming, additional details, and clicking for deeper insights.
# Plotly handles the interactivity with JavaScript behind the scenes, allowing users to focus on writing Python code to build the charts.

# Types of Plotly Plots
# Plotly offers a wide range of plot types, including:
# Line Charts: Used to display trends and patterns in data over time.
# Bar Charts: Used to compare categorical data across different groups.
# Scatter Plots: Used to visualize the relationship between two numerical variables.
# Histograms: Used to display the distribution of a single numerical variable.
# Pie Charts: Used to display proportional data and compare different categories.
# Box Plots: Used to display the distribution of a numerical variable and compare different groups.
# Violin Plots: Used to display the distribution of a numerical variable and compare different groups.
# 3D Scatter Plots: Used to visualize the relationship between three numerical variables.
# Heatmaps: Used to display the relationship between two categorical variables.
# Treemaps: Used to display hierarchical data and compare different categories.

# Enhancements with Plotly
# Plotly offers several enhancements to traditional static plots, including:
# Interactivity: Plotly plots are interactive, allowing users to hover, zoom, and click for more information.
# Customization: Plotly offers a wide range of customization options, including colors, fonts, and layouts.
# Animation: Plotly plots can be animated to show changes over time or to highlight specific data points.
# 3D Visualization: Plotly offers 3D visualization capabilities, allowing users to explore complex data in a more intuitive way.
# Integration with Other Libraries: Plotly integrates seamlessly with other popular Python libraries, including Pandas, NumPy, and Scikit-learn.

# Example Use Cases
# Data Exploration: Use Plotly to explore and visualize data, identifying trends and patterns.
# Business Intelligence: Use Plotly to create interactive dashboards and reports for business stakeholders.
# Research: Use Plotly to visualize and communicate research findings to a wider audience.
# Education: Use Plotly to create interactive visualizations for educational purposes.

# Load the tips dataset
df = px.data.tips()

# Create a line chart
fig_line = px.line(df, y="total_bill")

# Create a bar chart
fig_bar = px.bar(df, x='day', y="total_bill")

# Create a scatter plot
fig_scatter = px.scatter(df, x='total_bill', y="tip")

# Create a histogram
fig_hist = px.histogram(df, x="total_bill")

# Create a pie chart
fig_pie = px.pie(df, values="total_bill", names="day")

# Create a box plot
fig_box = px.box(df, x="day", y="tip")

# Create a violin plot
fig_violin = px.violin(df, x="day", y="tip")

# Create a 3D scatter plot
fig_3d = px.scatter_3d(df, x="total_bill", y="sex", z="tip")

# Create a Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Graph(id='line-chart', figure=fig_line),
    dcc.Graph(id='bar-chart', figure=fig_bar),
    dcc.Graph(id='scatter-plot', figure=fig_scatter),
    dcc.Graph(id='histogram', figure=fig_hist),
    dcc.Graph(id='pie-chart', figure=fig_pie),
    dcc.Graph(id='box-plot', figure=fig_box),
    dcc.Graph(id='violin-plot', figure=fig_violin),
    dcc.Graph(id='3d-scatter-plot', figure=fig_3d),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
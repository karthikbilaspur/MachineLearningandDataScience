# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define a function to create a line chart
def create_line_chart(x, y, title, xlabel, ylabel):
    """
    Create a line chart with the given data.

    Args:
        x (list): X-axis data
        y (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Define a function to create a bar chart
def create_bar_chart(x, y, title, xlabel, ylabel):
    """
    Create a bar chart with the given data.

    Args:
        x (list): X-axis data
        y (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Define a function to create a histogram
def create_histogram(data, bins, title, xlabel, ylabel):
    """
    Create a histogram with the given data.

    Args:
        data (list): Data to plot
        bins (int): Number of bins
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Define a function to create a scatter plot
def create_scatter_plot(x, y, title, xlabel, ylabel):
    """
    Create a scatter plot with the given data.

    Args:
        x (list): X-axis data
        y (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Define a function to create a pie chart
def create_pie_chart(data, labels, title):
    """
    Create a pie chart with the given data.

    Args:
        data (list): Data to plot
        labels (list): Labels for the pie chart
        title (str): Chart title
    """
    plt.pie(data, labels=labels)
    plt.title(title)
    plt.show()

# Define a function to create a box plot
def create_box_plot(data, title, xlabel, ylabel):
    """
    Create a box plot with the given data.

    Args:
        data (list): Data to plot
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.boxplot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Define a function to create a heatmap
def create_heatmap(data, title, xlabel, ylabel):
    """
    Create a heatmap with the given data.

    Args:
        data (2D list): Data to plot
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    plt.imshow(data, cmap='viridis', interpolation='nearest')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Create example charts
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
create_line_chart(x, y, "Line Chart", "X-Axis", "Y-Axis")

x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]
create_bar_chart(x, y, "Bar Chart", "Day", "Total Bill")

data = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
        21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]
create_histogram(data, 10, "Histogram", "Total Bill", "Frequency")

x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]
create_scatter_plot(x, y, "Scatter Plot", "Day", "Total Bill")

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
data = [23, 10, 35, 15, 12]
create_pie_chart(data, cars, "Pie Chart")

data = [[10, 12, 14, 15, 18, 20, 22],
        [8, 9, 11, 13, 17, 19, 21],
        [14, 16, 18, 20, 23, 25, 27]]
create_box_plot(data, "Box Plot", "Groups", "Values")

np.random.seed(0)
data = np.random.rand(10, 10)
create_heatmap(data, "Heatmap", "X-Axis", "Y-Axis")
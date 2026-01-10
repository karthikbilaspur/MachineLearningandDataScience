# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and informative statistical graphics.
# Seaborn is particularly well-suited for visualizing datasets with multiple variables.

# Load the tips dataset
tips = sns.load_dataset('tips')

# Distribution Plot
# A distribution plot is used to visualize the distribution of a single variable.
sns.histplot(tips['total_bill'], kde=True)
plt.title('Total Bill Distribution')
plt.show()

# Categorical Plot
# A categorical plot is used to visualize categorical data.
sns.barplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# Regression Plot
# A regression plot is used to visualize regression models.
sns.regplot(x='total_bill', y='tip', data=tips, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.show()

# Pairwise Plot
# A pairwise plot is used to visualize pairwise relationships between variables.
sns.pairplot(tips, hue='sex')
plt.show()

# Joint Plot
# A joint plot is used to visualize the relationship between two variables.
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
plt.show()

# Heatmap
# A heatmap is used to visualize heatmaps.
flights = sns.load_dataset('flights')
flights_pivot = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(flights_pivot, annot=True, cmap='Blues')
plt.show()

# 1. Line Plot
# A line plot is used to visualize the relationship between two numeric variables.
data = {'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'], 'Age': [21, 23, 20, 24]}
df = pd.DataFrame(data)
plt.plot(df.index, df['Age'])
plt.xlabel('Index')
plt.ylabel('Age')
plt.title('Age Line Plot')
plt.show()

# 2. Scatter Plot
# A scatter plot is used to visualize the relationship between two numeric variables.
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Total Bill vs Tip')
plt.show()

# 3. Box Plot
# A box plot is used to visualize the distribution of a single variable.
sns.boxplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# 4. Violin Plot
# A violin plot is used to visualize the distribution of a single variable.
sns.violinplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# 5. Swarm Plot
# A swarm plot is used to visualize the distribution of a single variable.
sns.swarmplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# 6. Bar Plot
# A bar plot is used to visualize categorical data.
sns.barplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# 7. Point Plot
# A point plot is used to visualize categorical data.
sns.pointplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# 8. Count Plot
# A count plot is used to visualize categorical data.
sns.countplot(x='sex', data=tips)
plt.title('Count of Sex')
plt.show()

# 9. KDE Plot
# A KDE plot is used to visualize the distribution of a single variable.
sns.kdeplot(data=tips['total_bill'], fill=True)
plt.title('Total Bill Distribution')
plt.show()

# Customizing Plots
# Seaborn plots can be customized using various options.
sns.set_style("whitegrid")
sns.boxplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.show()

# Customize the plot style
sns.set_style("whitegrid")

# Customize the color palette
sns.set_palette("husl")

# Create a plot
sns.barplot(x='sex', y='total_bill', data=tips)
plt.title('Total Bill by Sex')
plt.xlabel('Sex')
plt.ylabel('Total Bill')
plt.show()

print("Seaborn is a powerful data visualization library in Python.")
print("It provides a high-level interface for drawing attractive and informative statistical graphics.")
print("Seaborn is particularly well-suited for visualizing datasets with multiple variables.")
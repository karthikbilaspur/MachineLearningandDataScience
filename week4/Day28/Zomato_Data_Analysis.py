# zomato_data_analysis.py

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """Load the Zomato dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def handleRate(value):
    """Handle the rate column by removing denominator characters."""
    value = str(value).split('/')
    value = value[0]
    return float(value)

def clean_data(df):
    """Clean and process the data."""
    df['rate'] = df['rate'].apply(handleRate)
    return df

def explore_restaurant_types(df):
    """Explore the types of restaurants."""
    sns.countplot(x=df['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.show()

def votes_by_restaurant_type(df):
    """Get the count of votes for each restaurant type."""
    grouped_data = df.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.plot(result, c='green', marker='o')
    plt.xlabel('Type of restaurant')
    plt.ylabel('Votes')
    plt.show()

def most_voted_restaurant(df):
    """Find the restaurant with the highest number of votes."""
    max_votes = df['votes'].max()
    restaurant_with_max_votes = df.loc[df['votes'] == max_votes, 'name']
    print('Restaurant(s) with the maximum votes:')
    print(restaurant_with_max_votes)

def online_order_availability(df):
    """Explore the online_order column."""
    sns.countplot(x=df['online_order'])
    plt.show()

def analyze_ratings(df):
    """Check the distribution of ratings."""
    plt.hist(df['rate'], bins=5)
    plt.title('Ratings Distribution')
    plt.show()

def approximate_cost_for_couples(df):
    """Analyze the approx_cost(for two people) column."""
    couple_data = df['approx_cost(for two people)']
    sns.countplot(x=couple_data)
    plt.show()

def ratings_comparison(df):
    """Compare ratings between online and offline orders."""
    plt.figure(figsize=(6, 6))
    sns.boxplot(x='online_order', y='rate', data=df)
    plt.show()

def order_mode_preferences(df):
    """Find the relationship between order mode and restaurant type."""
    pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
    plt.title('Heatmap')
    plt.xlabel('Online Order')
    plt.ylabel('Listed In (Type)')
    plt.show()

def main():
    # Load the dataset
    file_path = '/content/Zomato-data-.csv'  # Update this path to your dataset
    df = load_dataset(file_path)
    
    if df is not None:
        # Clean the data
        df = clean_data(df)
        
        # Explore restaurant types
        explore_restaurant_types(df)
        
        # Votes by restaurant type
        votes_by_restaurant_type(df)
        
        # Most voted restaurant
        most_voted_restaurant(df)
        
        # Online order availability
        online_order_availability(df)
        
        # Analyze ratings
        analyze_ratings(df)
        
        # Approximate cost for couples
        approximate_cost_for_couples(df)
        
        # Ratings comparison
        ratings_comparison(df)
        
        # Order mode preferences
        order_mode_preferences(df)

if __name__ == "__main__":
    main()
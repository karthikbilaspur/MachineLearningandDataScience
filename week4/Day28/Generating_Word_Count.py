# word_cloud_generator.py

# Import necessary libraries
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def load_dataset(file_path):
    """Load the IMDB dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def clean_text_data(df):
    """Clean the text data by removing punctuation, converting to lowercase, and removing stopwords."""
    text = ' '.join(df['review'].astype(str).tolist())
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = text.lower()
    stopwords = set(STOPWORDS)
    text = ' '.join(word for word in text.split() if word not in stopwords)
    return text

def generate_word_cloud(text, width=800, height=400, background_color='white', max_words=None, colormap=None):
    """Generate a word cloud from the cleaned text data."""
    wordcloud = WordCloud(width=width, height=height, background_color=background_color, max_words=max_words, colormap=colormap).generate(text)
    return wordcloud

def display_word_cloud(wordcloud):
    """Display the word cloud."""
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    # Load the dataset
    file_path = '/content/IMDB-Dataset.csv'  # Update this path to your dataset
    df = load_dataset(file_path)
    
    if df is not None:
        # Clean the text data
        text = clean_text_data(df)
        
        # Generate the word cloud
        wordcloud = generate_word_cloud(text)
        
        # Display the word cloud
        display_word_cloud(wordcloud)

        # Customize the word cloud
        customized_wordcloud = generate_word_cloud(text, max_words=100, colormap='coolwarm')
        display_word_cloud(customized_wordcloud)

if __name__ == "__main__":
    main()
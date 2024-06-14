import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Sample dataset creation (replace this with your actual dataset loading logic if needed)
data = {
    'feedback': [
        "Great product, loved it!",
        "The service was terrible, never buying again.",
        "Fast delivery and good customer support.",
        "Could be better, not satisfied with the quality.",
        "Highly recommended, will buy more in the future."
    ]
}
df = pd.DataFrame(data)

# Step 2: Preprocess the text data
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Step 3: Calculate frequency distribution of words
def calculate_word_frequencies(tokens):
    word_freq = Counter(tokens)
    return word_freq

# Step 4: Display top N most frequent words and their frequencies
def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    for word, freq in top_words:
        print(f'{word}: {freq}')

# Step 5: Plot a bar graph of the top N most frequent words
def plot_word_frequencies(word_freq, top_n):
    top_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values(), color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the workflow
def main():
    # Step 2: Preprocess text data
    df['clean_text'] = df['feedback'].apply(preprocess_text)
    
    # Step 3: Flatten tokens
    tokens = [token for sublist in df['clean_text'] for token in sublist]
    
    # Step 4: Calculate word frequencies
    word_freq = calculate_word_frequencies(tokens)
    
    # Step 5: User input for top N words to display
    while True:
        try:
            top_n = int(input("Enter the number of top frequent words to display: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    # Step 6: Display top N words and frequencies
    display_top_words(word_freq, top_n)
    
    # Step 7: Plot bar graph of top N words
    plot_word_frequencies(word_freq, top_n)

if __name__ == '__main__':
    main()

from collections import Counter

def count_word_frequencies(text):
    # Split the text into words
    words = text.split()

    # Count the frequencies of each word
    word_counts = Counter(words)

    # Print the word frequencies
    for word, count in word_counts.items():
        print(word, ":", count)

# Test the function
text = "Hello world. How are you? Hello!"

# Correcting the typo in the import statement
from collections import Counter

# Using Counter to count occurrences in a list
c = Counter([0, 1, 2, 0])  # Counts the occurrences of each item, outcome: {0: 2, 1: 1, 2: 1}

# Iterating over the 10 most common elements in a word count dictionary
for word, count in word_counts.most_common(10):  # 'most_common' returns the most common elements in descending order
    print(word, count)

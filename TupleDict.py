# Strings
single_quoted_string = 'data science'  # Single-quoted string
double_quoted_string = "data science"  # Double-quoted string

# Lists
integer_list = [1, 2, 3]  # A list of integers
heterogeneous_list = ["String", 0.1, True]  # List with different data types (string, float, boolean)
list_of_list = [integer_list, heterogeneous_list, []]  # A list of lists, including an empty list
list_length = len(integer_list)  # Length of integer_list, outcome: 3
list_sum = sum(integer_list)  # Sum of integer_list, outcome: 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of integers from 0 to 9

zero = x[0]  # First element of list x, outcome: 0
one = x[0]  # First element of list x, should be x[1], current outcome: 0
nine = x[-1]  # Last element of list x, outcome: 9
eight = x[-2]  # Second last element of list x, outcome: 8
x[0] = -1  # Changing the first element of x to -1, updated x: [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing
first_three = x[:3]  # First three elements of x, outcome: [-1, 1, 2]
three_to_end = x[3:]  # All elements from index 3 to the end, outcome: [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5]  # Elements from index 1 to 4 (exclusive), outcome: [1, 2, 3, 4]
last_three = x[-3:]  # Last three elements of x, outcome: [7, 8, 9]
without_first_and_last = x[1:-1]  # All elements except the first and last, outcome: [1, 2, 3, 4, 5, 6, 7, 8]
copy_of_x = x[:]  # A copy of list x, outcome: [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 'in' operator
1 in [1, 2, 3]  # Checks if 1 is in the list, outcome: True
0 in [1, 2, 3]  # Checks if 0 is in the list, outcome: False

# extend method - modifies the list by adding elements
x = [1, 2, 3]
x.extend([4, 5, 6])  # Adds [4, 5, 6] to x, modified x: [1, 2, 3, 4, 5, 6]

# Adding without modifying x (creates a new list)
x = [1, 2, 3]
y = x + [4, 5, 6]  # New list y: [1, 2, 3, 4, 5, 6], x remains unchanged: [1, 2, 3]

# Appending - adds a single element to the list
x = [1, 2, 3]
x.append(0)  # Adds 0 to x, modified x: [1, 2, 3, 0]
y = x[-1]  # Last element of x, outcome: 0
z = len(x)  # Length of x, outcome: 4

# Unpacking the elements from a list
x, y = [1, 2]  # Unpacks 1 into x and 2 into y
# Ignoring a value during unpacking
_, y = [1, 2]  # Ignores the first value, y is assigned 2

# Tuples - immutable cousins of lists using ()
my_list = [1, 2]
my_tuple = (1, 2)  # Tuple with values (1, 2)
other_tuple = 3, 4  # Tuple without parentheses (3, 4)
my_list[1] = 3  # Modifies the list, updated my_list: [1, 3]

try:
    my_tuple[1] = 3  # Raises TypeError because tuples are immutable
except TypeError:
    print("cannot modify a tuple")  # Outcome: "cannot modify a tuple"

# Functions
def sum_and_products(x, y):
    return (x + y), (x * y)  # Returns the sum and product of x and y

sp = sum_and_products(2, 3)  # Outcome: (5, 6)
s, p = sum_and_products(5, 10)  # s = 15, p = 50

# Dictionaries
empty_dict = {}  # Empty dictionary
empty_dict2 = dict()  # Another way to create an empty dictionary
grades = {"joel": 80, "Time": 95}  # Dictionary with key-value pairs

joels_grade = grades["joel"]  # Outcome: 80

try:
    kates_grade = grades["Kate"]  # Raises KeyError because "Kate" is not a key in the dictionary
except KeyError:
    print("no grade for Kate!")  # Outcome: "no grade for Kate!"

# get method - avoids KeyError
grades.get("Kate", "No grade available")  # Outcome: "No grade available"

# defaultdict-like functionality with exception handling
word_counts = {}
for word in document:  # Iterating over 'document' (assuming it's a list or iterable)
    if word in word_counts:
        word_counts[word] += 1  # Increments the count if the word is already in the dictionary
    else:
        word_counts[word] = 1  # Adds the word with a count of 1 if it's not in the dictionary

# Handling exceptions in counting
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1  # Attempts to increment the word count
    except KeyError:
        word_counts[word] = 1  # Adds the word with a count of 1 if it's not found

# Using the get method to simplify
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)  # Gets the current count or returns 0 if not found
    word_counts[word] = previous_count + 1  # Increments the count

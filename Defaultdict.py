#importing collections
from collections import defaultdict

word_count = defaultdict(int)
for word in document:
    word_count[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(list)
dd_dict["joel"]["City"] = "Seatle"

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1
# Importing collections
from collections import defaultdict

# defaultdict with int as the default factory (creates default value 0 for int)
word_count = defaultdict(int)
for word in document:
    word_count[word] += 1  # Adds 1 to the count of each word in document

# defaultdict with list as the default factory (creates an empty list by default)
dd_list = defaultdict(list)
dd_list[2].append(1)  # Appends 1 to the list at key 2, outcome: {2: [1]}

# This will raise an error
dd_dict = defaultdict(list)
dd_dict["joel"]["City"] = "Seattle"  # TypeError: list indices must be integers, not str
# Correcting it:
dd_dict = defaultdict(dict)
dd_dict["joel"]["City"] = "Seattle"  # Creates a dictionary for key "joel", outcome: {"joel": {"City": "Seattle"}}

# defaultdict with a custom lambda function
dd_pair = defaultdict(lambda: [0, 0])  # Default value is a list [0, 0]
dd_pair[2][1] = 1  # Modifies the second element of the list at key 2, outcome: {2: [0, 1]}

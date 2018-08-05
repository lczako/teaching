# Python fundamentals (2018-08-04)

## Built-in functions

[All built in functions](https://docs.python.org/3/library/functions.html)

We used the following ones:
* max() -- Returns the largest item from the list
* min() -- Returns the smallest item from the list
* sorted() -- Returns the items from the list in ascending order


## Built in types we used

### List

Lists are used to store a collection of data in an ordered sequence.
Lists are constructed using a pair of square brackets.

```python
# Construction of an empty list
my_empty_list = []

# List with one item
my_one_item_list = ['apple']

# List with multiple items
mylist = ['aba', 'daba', 'aaab']

```
You can access an item in a list using it's index. Indexing starts from zero.

```python
mylist = ['aba', 'daba', 'aaab']
# index   0       1      2


# Accessing 1st item
mylist[1]
# 'daba'
```

You can add a new item to the end of your list using the append() method.

```python
my_list.append('bbba')
# my_list = ['aba', 'daba', 'aaab', 'bbba']
```

[More about lists](https://www.tutorialspoint.com/python/python_lists.htm)

#### List Challenges

* [Count of positives / sum of negatives](https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives)
* [Remove duplicates from list](https://www.codewars.com/kata/remove-duplicates-from-list)


### Dictionaries

Unordered collection of key, value pairs, where the key is a unique identifier where we can find our data and the value is our data.
 Dictionaries are constructed using curly brackets.
```python
# Construct empty dictionary
my_empty_dict = {}

# Construct dictionary
my_dict = {'my_key_1': 'my_value_1', 'my_key_2': 'my_value_2'}

# Access value
my_dict['my_key_2']
# 'my_value_2
```

Dictionary methods we used:
* keys() -- Returns the keys in the dict
* values() -- Returns back the values in the dict
* items() -- Returns back the key value pairs

```python
my_keys = my_dict.keys()
# my_keys = dict_keys(['my_key_1', 'my_key_2'])

my_values = my_dict.vlaues()
# my_values = dict_values(['my_value_1', 'my_value_2'])

my_items = my_dict.items()
# my_items = dict_items([('a', 2), ('b', 3)])
```

[More about dictionaries](https://www.tutorialspoint.com/python/python_dictionary.htm)

#### Dictionary challenges

* [The Hidden Word](https://www.codewars.com/kata/the-hidden-word/train/python)
* [Swap items in a dictionary](https://www.codewars.com/kata/swap-items-in-a-dictionary)

### Tuples

A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Tuples are constructed using parentheses. We access items in the tuple the same way as in a list.

```python
my_tuple = (1, 'a', 12, 'cat')

my_tuple[2]
# 12
```

[More about tuples](https://www.tutorialspoint.com/python/python_tuples.htm)

### Useful tutorial videos

* [Lists, tuples and sets](https://www.youtube.com/watch?v=W8KRzm-HUcc)
* [Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0&t=42s)


## Modes Kata

```python
def modes(data):
    # modes function waits for a parameter 'data' which is a sequence. It can be a string, list, etc..

    # Empty dict we'll use to store item counts.
    counts = {}

    # Populate the dict. The items in data will be used as keys and the values will be the number occurrence of that item in the list
    for key in data:
        if key in counts:
            # Accesses the value under key and increase it with one
            counts[key] += 1
        else:
            # Here we make sure that the key is present in the dictionary and set it to 1
            counts[key] = 1

    # Our counts dictionary is populated, print it out to make it more understandable
    print(counts)

    # Find the number of times the mode appears. Remember .values() is a dictionary method.
    max_occurrence = max(counts.values())

    # Short-circuit if there is no mode.
    min_occurrence = min(counts.values())
    if max_occurrence == min_occurrence:
        return []

    # Initialize an empty list to populate and return.
    result = []
    # Iterates through the keys in the counts dictionary
    for key in counts.keys():
        # Accessing the occurrences by the key (which is an item from our original dictionary)
        if counts[key] == max_occurrence:
            # if its occurrence equals with the max occurrence we add it to the result list
            result.append(key)

    # Due our task is to return the modes in ascending order, we use sorted() built in function to sort it for us.
    return sorted(result)
```

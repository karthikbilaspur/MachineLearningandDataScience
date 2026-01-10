# What is a collection module ? 
# A collection module is a built-in Python module that provides specialized container datatypes
# to store and manage data more efficiently than the built-in data types like lists, tuples,
# and dictionaries. The collections module includes several useful classes that can be used to
# create different types of collections, such as named tuples, deque, Counter, OrderedDict,
# defaultdict, and ChainMap.

# Here are some of the commonly used classes in the collections module:
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap
# 1. namedtuple: A factory function for creating tuple subclasses with named fields.
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
# 2. deque: A double-ended queue that allows you to append and pop elements from both ends efficiently.
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)  # Output: deque([0, 1, 2, 3, 4])
# 3. Counter: A subclass of dict that counts the occurrences of elements in an iterable
c = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(c)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
# 4. OrderedDict: A subclass of dict that maintains the order of keys based on the order of insertion.
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 5. defaultdict: A subclass of dict that provides a default value for a nonexistent key
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# 6. ChainMap: A class that groups multiple dictionaries into a single view.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm['b'])  # Output: 2 (from dict1)
print(cm['c'])  # Output: 4 (from dict2)
# These classes provide powerful and flexible ways to manage collections of data in Python,
# making it easier to write efficient and readable code.

# Example usage of collections module
if __name__ == "__main__":
    # Using namedtuple
    Rectangle = namedtuple('Rectangle', ['length', 'width'])
    rect = Rectangle(10, 5)
    print(f"Rectangle Length: {rect.length}, Width: {rect.width}")

    # Using deque
    queue = deque()
    queue.append('task1')
    queue.append('task2')
    queue.appendleft('task0')
    print(f"Queue: {queue}")

    # Using Counter
    word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_count = Counter(word_list)
    print(f"Word Count: {word_count}")

    # Using OrderedDict
    ordered_dict = OrderedDict()
    ordered_dict['first'] = 1
    ordered_dict['second'] = 2
    ordered_dict['third'] = 3
    print(f"OrderedDict: {ordered_dict}")

    # Using defaultdict
    fruit_count = defaultdict(int)
    fruit_count['apple'] += 1
    fruit_count['banana'] += 2
    print(f"Fruit Count: {fruit_count}")

    # Using ChainMap
    defaults = {'color': 'red', 'size': 'medium'}
    user_settings = {'size': 'large'}
    settings = ChainMap(user_settings, defaults)
    print(f"Settings Color: {settings['color']}, Size: {settings['size']}")

# Example usage of collections module
if __name__ == "__main__":
    # Using namedtuple
    Rectangle = namedtuple('Rectangle', ['length', 'width'])
    rect = Rectangle(10, 5)
    print(f"Rectangle Length: {rect.length}, Width: {rect.width}")

    # Using deque
    queue = deque()
    queue.append('task1')
    queue.append('task2')
    queue.appendleft('task0')
    print(f"Queue: {queue}")

    # Using Counter
    word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_count = Counter(word_list)
    print(f"Word Count: {word_count}")

    # Using OrderedDict
    ordered_dict = OrderedDict()
    ordered_dict['first'] = 1
    ordered_dict['second'] = 2
    ordered_dict['third'] = 3
    print(f"OrderedDict: {ordered_dict}")

    # Using defaultdict
    fruit_count = defaultdict(int)
    fruit_count['apple'] += 1
    fruit_count['banana'] += 2
    print(f"Fruit Count: {fruit_count}")

    # Using ChainMap
    defaults = {'color': 'red', 'size': 'medium'}
    user_settings = {'size': 'large'}
    settings = ChainMap(user_settings, defaults)
    print(f"Settings Color: {settings['color']}, Size: {settings['size']}")


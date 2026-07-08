# =============================================
# PYTHON VARIABLES - Beginner to Advanced
# =============================================

# ==================== BEGINNER ====================

# 1. Basic variable assignment
name = "Alice"          # String
age = 25                # Integer
height = 5.7            # Float
is_student = True       # Boolean
score = None            # NoneType

print(name, age, height, is_student)

# Multiple assignment (unpacking)
x, y, z = 10, 20, 30

# 2. Basic operations
total = age + 5
greeting = "Hello, " + name

# ==================== INTERMEDIATE ====================

# Type hints (recommended for clarity and static analysis tools like mypy)
name: str = "Bob"
age: int = 28
scores: list = [85, 90, 78]
person: dict = {"name": "Bob", "age": 28}

# Unpacking with * and **
coords = (10, 20, 30)
x, y, *rest = coords   # x=10, y=20, rest=[30]

# Walrus Operator := (Python 3.8+) - assign and check in one line
if (n := len(scores)) > 2:
    print(f"More than 2 scores: {n}")

# ==================== ADVANCED / OPTIMIZATION ====================

from typing import List, Dict, Any
from collections import defaultdict
import sys

# 1. Memory efficient class with __slots__
class Player:
    __slots__ = ['name', 'score', 'level']   # Saves memory by avoiding __dict__, faster attribute access
    
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        self.level = 1

# 2. Constants (convention)
MAX_SCORE = 1000
PI = 3.14159

# 3. Defaultdict for cleaner code
word_count: defaultdict = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1

# 4. Immutable variables (use tuple or NamedTuple)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(5, 10)

# ==================== DYNAMIC ATTRIBUTES SECTION ====================

# Advanced technique: Custom class that dynamically handles any attribute
# Useful for configuration objects, data containers, or when attribute names are unknown at design time

class DynamicVar:
    # Initialize private dictionary to store all dynamic attributes
    def __init__(self):
        # We use super().__setattr__ here to avoid infinite recursion
        # because normal self._data = {} would call __setattr__ again
        super().__setattr__('_data', {})   # Private storage for all attributes
    
    # Called automatically when you do obj.any_name = value
    def __setattr__(self, name: str, value: Any) -> None:
        # Special case: allow setting the _data attribute itself without recursion
        if name == "_data":
            super().__setattr__(name, value)
        else:
            # Store everything else in our internal dictionary
            self._data[name] = value
    
    # Called when accessing obj.any_name (if it doesn't exist normally)
    def __getattr__(self, name: str):
        # Return the value from our dict or raise AttributeError if missing
        # Using .get() here to avoid KeyError
        return self._data.get(name)
    
    # Optional: allow deletion of dynamic attributes
    def __delattr__(self, name: str):
        if name in self._data:
            del self._data[name]
        else:
            super().__delattr__(name)

# ==================== USAGE EXAMPLE ====================

# Create dynamic object
config = DynamicVar()

# Set any attributes dynamically (no need to define them in class)
config.api_key = "xyz123"
config.timeout = 30
config.debug = True
config.host = "localhost"

print("Dynamic attributes:")
print("API Key:", config.api_key)
print("Timeout:", config.timeout)
print("Debug mode:", config.debug)

# Memory usage example
print(f"Memory used by list: {sys.getsizeof([1,2,3,4,5])} bytes")

# Best Practices Summary:
# • Use meaningful names
# • Prefer type hints in larger projects
# • Use __slots__ for performance-critical classes
# • Avoid global variables
# • Use constants in UPPER_CASE
# • Dynamic attributes are powerful but use sparingly (can make code harder to debug)
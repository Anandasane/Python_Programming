# --- Numeric Types ---

# Integer (int): Whole numbers, positive or negative, without decimals
count = 42
negative_num = -10
large_num = 1_000_000  # Underscores for readability (Python 3.6+)

# Float: Real numbers with decimal points
price = 19.99
scientific = 2.5e3  # 2.5 * 10^3 = 2500.0

# Complex: Numbers with a real and imaginary part (j or J suffix)
complex_num = 3 + 4j

# --- Text Type ---

# String (str): Immutable sequence of characters
message = "Hello, Python!"
single_quote = 'Single quotes work too'
multiline = """This is a 
multi-line string"""

# --- Sequence Types ---

# List: Ordered, mutable collection of items
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "text", 3.14, True]

# Tuple: Ordered, immutable collection (cannot be changed after creation)
coordinates = (10.5, 20.3)
single_item_tuple = (42,)  # Note the comma to denote a tuple

# Range: Immutable sequence of numbers, often used in loops
count_range = range(5)  # Generates 0, 1, 2, 3, 4

# --- Mapping Type ---

# Dictionary (dict): Unordered collection of key-value pairs
user = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}

# --- Set Types ---

# Set: Unordered collection of unique, mutable items
unique_ids = {1, 2, 3, 3}  # The duplicate '3' is automatically removed

# Frozenset: Immutable version of a set (cannot be modified after creation)
immutable_set = frozenset([1, 2, 3])

# --- Boolean Type ---

# Bool: Represents True or False (subclass of int)
is_valid = True
is_empty = False

# --- Binary Types ---

# Bytes: Immutable sequence of bytes (0-255)
binary_data = b"hello"

# Bytearray: Mutable sequence of bytes
mutable_bytes = bytearray(b"world")
mutable_bytes = 87  # Change 'w' (119) to 'W' (87)

# Memoryview: Allows you to access the internal data of an object that supports the buffer protocol without copying
mv = memoryview(bytearray(b"python"))

# --- None Type ---

# NoneType: Represents the absence of a value
null_value = None

# --- Verification ---
# Let's print the type of each variable to confirm
print(f"count: {type(count)} -> {count}")
print(f"price: {type(price)} -> {price}")
print(f"complex_num: {type(complex_num)} -> {complex_num}")
print(f"message: {type(message)} -> {message}")
print(f"fruits: {type(fruits)} -> {fruits}")
print(f"coordinates: {type(coordinates)} -> {coordinates}")
print(f"user: {type(user)} -> {user}")
print(f"unique_ids: {type(unique_ids)} -> {unique_ids}")
print(f"is_valid: {type(is_valid)} -> {is_valid}")
print(f"binary_data: {type(binary_data)} -> {binary_data}")
print(f"null_value: {type(null_value)} -> {null_value}")
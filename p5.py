# Create a dictionary

my_dict = {

    "name": "John",

    "age": 30,

    "city": "New York"

}

# 1. Print the dictionary items

print("Dictionary items:", my_dict)

# 2. Access items

name = my_dict["name"]

age = my_dict["age"]

print("Accessed items - Name:", name, "Age:", age)

# 3. Use get() - The get() method returns the value of the item with the specified key.

city = my_dict.get("city:", "Unknown")

country = my_dict.get("country:", "Not specified")

print("City:", city, "Country:", country)

# 4. Change values

my_dict["age"] = 31

my_dict["city"] = "San Francisco"

print("Updated dictionary:", my_dict)

# 5. Use len()

dict_length = len(my_dict)

print("Length of the dictionary:", dict_length)
# Sort a List of Dictionaries by a Specific Key
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


# AI-Suggested Version 
def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])


# Usage
sorted_data = sort_dicts_by_key(data, "age")
print(sorted_data)


# Manual Implementation 
def manual_sort_dicts_by_key(data, key):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j][key] > current[key]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data


# Usage 
sorted_data = manual_sort_dicts_by_key(data, "age")
print(sorted_data)



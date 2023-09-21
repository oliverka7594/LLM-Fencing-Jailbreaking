import json

# Load the JSON data
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Initialize a dictionary to store the counts
type_counts = {}

# Iterate through the data
for entry in data:
    types = entry.get('type', None)
    if types is not None:
        if isinstance(types, list):
            for t in types:
                if t is not None:
                    if t not in type_counts:
                        type_counts[t] = 1
                    else:
                        type_counts[t] += 1
        else:
            if types not in type_counts:
                type_counts[types] = 1
            else:
                type_counts[types] += 1

# Write the results to output.txt
with open('raw.txt', 'w') as output_file:
    for t, count in type_counts.items():
        output_file.write(f"{t}: {count}\n")

import json

# Load the JSON data
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Initialize a set to store unique types
unique_types = set()

# Iterate through the data
for entry in data:
    types = entry.get('type', None)
    if types is not None:
        if isinstance(types, list):
            for t in types:
                if t is not None:
                    unique_types.add(t)
        else:
            unique_types.add(types)

# Write the results to output.txt
with open('output.txt', 'w') as output_file:
    output_file.write(f"Total unique types: {len(unique_types)}\n")

    # Initialize a dictionary to store the counts and sources
    type_info = {}

    # Iterate through the data
    for entry in data:
        types = entry.get('type', None)
        source = entry.get('source', None)
        if types is not None and source is not None:
            if isinstance(types, list):
                for t in types:
                    if t is not None:
                        if t not in type_info:
                            type_info[t] = {'count': 1, 'sources': {source}}
                        else:
                            type_info[t]['count'] += 1
                            type_info[t]['sources'].add(source)
            else:
                if types not in type_info:
                    type_info[types] = {'count': 1, 'sources': {source}}
                else:
                    type_info[types]['count'] += 1
                    type_info[types]['sources'].add(source)

    for t, info in type_info.items():
        sources = ', '.join(info['sources'])
        output_file.write(f"{t}: {info['count']}, {sources}\n")

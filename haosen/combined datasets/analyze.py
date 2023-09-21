import json

# Read the JSON file
with open('dataset.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Initialize dictionaries to store counts
type_counts = {}
jailbreak_counts = {}

# Count unique "type" and "jailbreak" values
for entry in data:
    entry_type = entry['type']
    entry_jailbreak = entry['jailbreak']

    # Convert entry_type to a string if it's a list
    if isinstance(entry_type, list):
        entry_type = ','.join(entry_type)

    if entry_type:
        type_counts[entry_type] = type_counts.get(entry_type, 0) + 1

    if entry_jailbreak:
        jailbreak_counts[entry_jailbreak] = jailbreak_counts.get(entry_jailbreak, 0) + 1

# Write the counts to a text file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("Type Counts:\n")
    for entry_type, count in type_counts.items():
        output_file.write(f"{entry_type}: {count}\n")

    output_file.write("\nJailbreak Counts:\n")
    for entry_jailbreak, count in jailbreak_counts.items():
        output_file.write(f"{entry_jailbreak}: {count}\n")

print("Counts have been written to output.txt")

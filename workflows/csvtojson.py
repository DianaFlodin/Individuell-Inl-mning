import csv
import json

# Read CSV file
csv_file_path = 'profiles1.csv'
json_file_path = 'data.json'

data = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Write JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"Converted {csv_file_path} to {json_file_path}")
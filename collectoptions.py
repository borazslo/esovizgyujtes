import os
import json

data_folder = 'data'
output_file = 'pids.json'
result = []

# Iterate over all files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'title' in data and 'pid' in data:
                result.append([data['pid'], data['title']])

# Write the result to the output file
with open(output_file, 'w') as outfile:
    json.dump(result, outfile, indent=4)
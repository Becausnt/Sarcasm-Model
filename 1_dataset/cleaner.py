import json

def ndjson_to_json(ndjson_path: str, json_path: str, attribute_to_remove: str = None) -> None:
    """
    Reads an NDJSON file, removes a specified attribute from each entry if provided,
    and writes the data as a valid JSON array to the output file.
    """
    data = []
    
    # Read each line from the NDJSON file and process it.
    try:
        with open(ndjson_path, "r") as infile:
            for line in infile:
                try:
                    entry = json.loads(line.strip())
                    # If an attribute to remove is provided and the entry is a dict, remove it.
                    if attribute_to_remove and isinstance(entry, dict):
                        entry.pop(attribute_to_remove, None)
                    data.append(entry)
                except json.JSONDecodeError:
                    print(f"Warning: Skipping malformed JSON line in {ndjson_path}")
    except Exception as e:
        print(f"Error reading {ndjson_path}: {e}")
        return

    # Write the entire list as a valid JSON array.
    try:
        with open(json_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
    except Exception as e:
        print(f"Error writing to {json_path}: {e}")

# File paths and attribute configuration.
file_one = "original/Sarcasm_Headlines_Dataset.json"
file_two = "original/Sarcasm_Headlines_Dataset_v2.json"
save_file_one = "clean/Sarcasm_Headlines_Dataset.json"
save_file_two = "clean/Sarcasm_Headlines_Dataset_v2.json"
attribute_to_remove = "article_link"

# Convert the NDJSON files to valid JSON format.
ndjson_to_json(file_one, save_file_one, attribute_to_remove)
ndjson_to_json(file_two, save_file_two, attribute_to_remove)

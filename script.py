import os
import yaml
import json

def convert_yaml_to_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            yaml_filepath = os.path.join(directory, filename)
            json_filepath = os.path.join(directory, filename.replace(".yaml", ".json"))

            # Load YAML file
            with open(yaml_filepath, "r") as yaml_file:
                yaml_data = yaml.safe_load(yaml_file)
            
            # convert YAML to JSON
            json_data = json.dumps(yaml_data, indent=4)

            # write JSON data to file
            with open(json_filepath, "w") as json_file:
                json_file.write(json_data)

            print(f"Converted {filename} to {filename.replace('.yaml', '.json')}")

if __name__ == "__main__":
    directory_path = "./"
    convert_yaml_to_json(directory_path)
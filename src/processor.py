import json

# Loading the files
def load_file(file):
    with open(file) as f:
        data = json.load(f)
    return data

# Validating the data
def validate_data(file):
    # Check if the data is a valid JSON file
    try:
        load_file(file)
        return True
    except ValueError as e:
        print(f"Invalid JSON: {e}")
        return False

def get_most_plays(data):
    # Get the song with the most plays
    most_plays = max(data, key=lambda x: x['plays'])
    return most_plays
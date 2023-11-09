import pandas
import json
import requests
json_data = "https://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en"

# data = requests.get(json_data).json()
# with open('data.json', 'w') as f:
#     json.dump(data, f)
with open('data_.json') as f:
    data = json.load(f)

def count_occurrences(data, value):
    count = 0
    if isinstance(data, dict):
        for values in data.values():
            count += count_occurrences(values, value)
    elif isinstance(data, (list,tuple)):
        for element in data:
            count += count_occurrences(element, value)
    elif isinstance(data, str):
        if value in data:
            count += 1
    return count

print(count_occurrences(data, 'hello'))
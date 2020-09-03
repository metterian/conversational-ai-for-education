import json
from itertools import chain
dataset_path = 'data/persona_label.json'
with open(dataset_path, "r", encoding="utf-8") as f:
    dataset = json.loads(f.read())

# for data in dataset:
#     if "".join((list(data.keys()))) == 'in a hospital':
#         print(list(chain(*data.values())))


for data in dataset:
    for unit, persona_list in data.items():


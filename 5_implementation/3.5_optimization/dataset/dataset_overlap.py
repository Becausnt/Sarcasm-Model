import json

with open('Sarcasm_Headlines_Dataset.json') as f:
    v1_data = json.load(f)

with open('Sarcasm_Headlines_Dataset_v2.json') as f:
    v2_data = json.load(f)

v1_set = set((item['headline'], item['is_sarcastic']) for item in v1_data)
v2_set = set((item['headline'], item['is_sarcastic']) for item in v2_data)

intersection = v1_set & v2_set
only_in_v1 = v1_set - v2_set
only_in_v2 = v2_set - v1_set

print(f"Overlap: {len(intersection)}")
print(f"Only in v1: {len(only_in_v1)}")
print(f"Only in v2: {len(only_in_v2)}")

"""
Overlap: 26602
Only in v1: 0
Only in v2: 1901

-> v2 is just v1 + extras, no optimization to be made here.
"""
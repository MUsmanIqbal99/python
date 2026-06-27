import json

try:
    with open("does_not_exist.json", "r") as f:
        loaded = json.load(f)
    print(loaded)
except FileNotFoundError:
    print("That file doesn't exist yet — no data to load.")

print("Program keeps running!")
import json
with open("file_3.json", "r+") as file:
    data = json.load(file)
    data.insert(0, "Hello Beetroot!")
    print(data)
with open("file_3.json", "w+") as file:
    json.dump(data, file)

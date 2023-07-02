import json
with open("file_2.json", "r+") as file:
    data = json.load(file)
    index = 0
    for i in data:
        if i["location"] == "Moscow, Russia Data Tower":
            data.pop(index)
        else:
            index += 1
with open("file_2.json", "w+") as file:
    json.dump(data, file)

import json
with open("file.json", "r+") as file:
    data = json.load(file)
    for i in data:
        print(i["processor"])
        if i["processor"] == 'AMD Ryzen':
            i["processor"] = 'AMD Ryzen 2'
with open("file.json", "w+") as file:
    json.dump(data, file)

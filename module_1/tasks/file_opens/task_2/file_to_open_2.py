lines = [
    "Це перший рядок.",
    "Це другий рядок.",
    "Це третій рядок.",
    "Це четвертий рядок.",
    "Це п'ятий рядок."]

with open("data.txt", "w") as file:
    for line in lines:
        file.write(f"{line}\n")

"""
First Task
"""

# adress = "@kobzar.com"
# name = "maxim"
# surname = "kostenko"
# print(f"First gmail: {name}.{surname}{adress}")
# print(f"Second gmail: {name[0]}.{surname}{adress}")
# print(f"Third gmail: {name[:3]}{surname[:3]}{adress}")
"""
Second Task
"""
age_person = 13
if age_person >= 18:
    print("Алкоголь продається")
elif age_person <= 18 and age_person >= 14:
    print("Можна купить енергетики")
else:
    print("Беріть що завгодно, окрім алкоголю та енергетиків!")

"""
Third Task
"""
transaction_id_crack = ";yu7i9om0&iymn%"
print(transaction_id_crack[1:-1])

"""
Fourth Task
"""
print(transaction_id_crack[1:-1].replace("&", ""))

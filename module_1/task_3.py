"""
Ex 1
"""
# while True:
#     num_1 = int(input("Please enter the first number: "))
#     num_2 = int(input("Please enter the second number: "))
#     operator = input("Please enter the operator(+, -, *, /) to solve 2 numbers: ")
#     if operator == "+":
#         print(f"Your answer is: {num_1 + num_2}")
#     elif operator == "-":
#         print(f"Your answer is: {num_1 - num_2}")
#     elif operator == "*":
#         print(f"Your answer is: {num_1 * num_2}")
#     elif operator == "/":
#         print(f"Your answer is: {num_1 / num_2}")
#     else:
#         print(f"Please change your operator to (+, -, *, /)")
#     ask = input("Enter 'q' to exit, or any key to continue: ")
#     if ask == "q":
#         break

"""
Ex 2
"""
# info = ["maxim", "kostenko", "@kobzar.com"]
# print(f"First gmail: {info[0]}.{info[1]}{info[2]}")
# print(f"Second gmail: {info[0][0]}-{info[1]}{info[2]}")
# print(f"Third gmail: {info[0][:3]}{info[1][:3]}{info[2]}")

"""
Ex 3
"""
big_info = [["maxim", "sergiy", "irina", "yuriy", "ilya"], ["kostenko", "kucherenko", "zaiets", "perepelko", "altudov"],
            ["@gmail.com", "@uk.com", "@ua.com", "@pl.com", "@us.com"]]
print(f"First gmail: {big_info[0][0]}.{big_info[1][0]}{big_info[2][0]}")
print(f"Second gmail: {big_info[0][1][0]}-{big_info[1][1]}{big_info[-1][1]}")
print(f"Third gmail: {big_info[0][2][:3]}{big_info[1][2][:3]}{big_info[-1][-3]}")
print(f"Fourth gmail: {big_info[0][3][:-1]}{big_info[1][3][-2]}{big_info[2][-2]}")
print(f"Fifth gmail: {(big_info[0][-1]).capitalize()}{(big_info[1][-1]).capitalize()}{big_info[-1][-1]}")


"""
Ex 4
"""
#  магазин я делаю в 4 таске, а может уже сделал xD )

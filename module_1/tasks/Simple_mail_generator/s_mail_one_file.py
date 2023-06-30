def info_gmails(big_info):
    print(f"First gmail: {big_info[0][0]}.{big_info[1][0]}{big_info[2][0]}")
    print(f"Second gmail: {big_info[0][1][0]}-{big_info[1][1]}{big_info[-1][1]}")
    print(f"Third gmail: {big_info[0][2][:3]}{big_info[1][2][:3]}{big_info[-1][-3]}")
    print(f"Fourth gmail: {big_info[0][3][:-1]}{big_info[1][3][-2]}{big_info[2][-2]}")
    print(f"Fifth gmail: {(big_info[0][-1]).capitalize()}{(big_info[1][-1]).capitalize()}{big_info[-1][-1]}")


info_gmails([["maxim", "sergiy", "irina", "yuriy", "ilya"],
             ["kostenko", "kucherenko", "zaiets", "perepelko", "altudov"],
             ["@gmail.com", "@uk.com", "@ua.com", "@pl.com", "@us.com"]])

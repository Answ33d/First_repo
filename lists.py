# shop_list = ["яблука", "молоко", "хліб", "яблука", "вода"]

# shop_list.insert(1,"шоколад")
# shop_list.index("яблука")

# print(shop_list.count("яблука"))
# counting=shop_list.count("яблука")
# print(shop_list)

# if counting>1:
#     shop_list.remove("яблука")

# counting=shop_list.count("яблука")
# print("----------")
# print(shop_list.count("яблука"))
# print(shop_list)
# shop_list.reverse()

# ------------------------------------------------------------------------------------------

# suspects = ["Light", "Misa", "L", "Mello", "Near", "Mikami", "Matsuda"]
# print(suspects)
# suspects.sort()
# print("After Sort")
# print(suspects)

# main_suspects=suspects[0:3]
# print(f'Main suspects - {main_suspects}')

# suspect_check=input("Who is suspect?")
# if suspect_check in suspects:
#     suspects.remove(suspect_check)
#     print(f'{suspect_check} is not under suspicion anymore')
# else:
#     print(f'{suspect_check} is not list')

# misa_index=suspects.index("Misa")
# misa=suspects.pop(misa_index)
# suspects.append(misa)
# print(f'Misa is special {suspects}')

# clues = ["Note", "Apple", "Watch"]

# suspects.extend(clues)
# print(suspects)

# 

# database = [
#     ["Light", 10, "Suspect"],
#     ["L", 0, "Detective"],
#     ["Misa", 7, "Suspect"]
# ]

# looking_for=input("What person are u interrested in?")
# print(f'You are looking for {looking_for}')
# for person_info in database:
#     if looking_for in person_info:
#         print(f'{looking_for} found in list number {database.index(person_info)} Suspec level is - {person_info[1]} Role - {person_info[2]}')
#         break
#     else:
#         print(f'"{looking_for} not found"')

# database[2][2]="Captured"
# print(database[2])

# database.append(["Near", 2, "Detective"])
# print("----------------------")
# print("Near added")
# print(database)

# high_risk=[]
# for persons in database:
#     if persons[1]>=5:
#         high_risk.append(persons[0])

# print(f'Persons with high rist - {high_risk}')
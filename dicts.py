# Task 1
# product = {"brand": "Samsung", "model": "Galaxy S23"}
# print(product)
# product["price"]=32000
# print(product)
# product.update({"in_stock":"True","color":"black" })
# print(product)
# product["price"]=31500
# values=product.values()
# print(values)

# Task2

# menu = {"Latte": 65, "Espresso": 45, "Cappuccino": 60, "Americano": 40, "Flat White": 75}
# print(menu.items())

# menu_drinks=menu.items()

# for drinks in menu_drinks:
#     print(f'{drinks[0]} price is {drinks[1]}')

# budget_drinks={}
# for drinks in menu_drinks:
#     if drinks[1]<=60:
#         budget_drinks[drinks[0]]=drinks[1]
#         print(f'Added {drinks[0]} with price {drinks[1]} to budgete drinks')

# print(budget_drinks)

# Task3

# hotel_rooms = {"101": "Occupied", "102": "Vacant", "105": "Cleaning"}

# room_check=input("Введіть номер кімнати")
# room_status=hotel_rooms.get(room_check)
# if room_status==None:
#     print(f'room with {room_check} not found')
# else:
#     print(f'{room_check} room is {room_status}')

# hotel_rooms.setdefault("201","Vacan t")
# print(hotel_rooms)


rooms={"kitchen": False, "hall": False, "bedroom": False}

while True:
    light_system=input("Which room to turn on the light? (Type stop to shut down)").lower()
    if light_system=="stop":
        break
    elif light_system in rooms and rooms[light_system]==False:
        rooms[light_system]=True
        print(f'Light in {light_system} is turned on')
    elif light_system in rooms and rooms[light_system]==True:
        print(f'Light in {light_system} is already on.')
        room_light=input("Do u want to shut it down? yes/no").lower()
        if room_light=="yes":
            rooms[light_system]=False
            print(f'Light in {light_system} is off')
        elif room_light=="no":
            continue
        else:
            continue
    else:
        print("Room not found")
print("/------------/----------------/----------------/")
light_status=True
for room, status in rooms.items():
    if status==True:
        light_status=False
        print(f'Light in {room} is on . Turn it off for economy')
if light_status==True:
    print("Light is off in every room")
print("/------------/----------------/----------------/")
while True:
    user_input=input("How many floors does your house has? (stop to exit)")
    if user_input=="stop":
        break
    try:
        floors=int(user_input)
        if floors<=0:
            print(f'There are no floors under house. Start from first floor')
        else:
            break
    except ValueError:
        print("Invalid input! Floor must be an integer (number). Try again.")
if user_input=="stop":
    print("System is now offline")
else:
    floors=int(user_input)
    for floor in range(1, floors+1):
        if floor%2==0:
            print(f'Scanners on {floor} floor working')
        elif floor==13:
            print(f'Information about this floor is forbidden {floor}')
        else:
            print(f'Scanners on {floor} floor need manual service')
if user_input=="stop":
    None
else:
    print("System is now offline")
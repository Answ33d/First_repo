password="1234"
admin_list=["Andrew", "Jake"]
admin=False
is_admin=input("Are u an admin? yes/no").lower()
if is_admin == "yes":
    admin_name=input("Enter ur login:")
    if admin_name in admin_list:
        print(f"Welcome, {admin_name}")
        admin=True
    else:
        while admin_name not in admin_list:
            print("Incorrect login")
            admin_name=input("Enter ur login again")
elif is_admin == "no":
    print("Enter password")
    ask_password=input("Enter password:")
    while ask_password != "1234":
        print("Password incorrect, try again")
        ask_password=input("Enter password again:")
is_robot=input("Are u a robot? yes/no").lower()
if is_robot == "no" and admin is True:
    print("U are logged in")
elif is_robot=="no" and admin is False:
    print("U are logged in")
elif is_robot == "yes":
    print("Sorry u are not allowed to log in")
else:
    print("type yes or no")
    is_robot=input("Are u a robot? yes/no").lower()
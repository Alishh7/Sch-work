from Friends import Friend

buddy1 = Friend("Pulkit", 100)
enemy = Friend("Sidhant", 100)

on = 1
while on == 1:
    buddy = input("Sidhant or Pulkit? ").lower()
    choice = input("Do you want to chat, fight, slap, hug, or give a rightHookToTheJaw? ")

    if buddy == "pulkit":
        print(buddy1.get_name())
        print ("score = ", buddy1.get_friendship())
        if choice == "chat":
            buddy1.chat()
            print ("score = ", buddy1.get_friendship())
        elif choice == "fight":
            buddy1.fight()
            print ("score = ", buddy1.get_friendship())
        elif choice == "slap":
            buddy1.slap()
            print ("score = ", buddy1.get_friendship())
        elif choice == "hug":
            buddy1.hug()
            print ("score = ", buddy1.get_friendship())
        elif choice == "rightHookToTheJaw":
            buddy1.rightHookToTheJaw()
            print ("score = ", buddy1.get_friendship())
        else:
            print("Invalid choice")

    elif buddy == "sidhant":
        print(enemy.get_name())
        print ("score = ", buddy1.get_friendship())
        if choice == "chat":
            enemy.chat()
            print ("score = ", buddy1.get_friendship())
        elif choice == "fight":
            enemy.fight()
            print ("score = ", buddy1.get_friendship())
        elif choice == "slap":
            enemy.slap()
            print ("score = ", buddy1.get_friendship())
        elif choice == "hug":
            enemy.hug()
            print ("score = ", buddy1.get_friendship())
        elif choice == "rightHookToTheJaw":
            enemy.rightHookToTheJaw()
            print ("score = ", buddy1.get_friendship())
        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

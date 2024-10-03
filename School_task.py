school = input("Are you going school today? (true/false) ").lower()

if school == "true":
    print ("Go to school and then relax/sleep")
    
elif school == "false":
    homework = input ("do you have homework? (true/false) ").lower()
    if homework == "false":
        print ("relax/sleep")
    elif homework == "true":
        print("do homework then relax/sleep")
    else:
        print("error, wrong input")
else:
    print ("wrong input")

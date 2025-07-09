try:
    name=str(input("enter your name:")).capitalize
    email=str(input("enter your email:")).lower

    
    try:
        mobile=int(input("enter your mobile"))
        if len(str(mobile))==10:
            pass
        else:
            print("invaild mobile 10 digit")
    except:
        print("invaild mobile")
    password=str(input("enter your password:"))
    if password.isalnum():
        pass
    else:
        print("error!")
    confimpassword=str(input("enter your confimpassword:"))
    if confimpassword==password:
        print("register pass com")
    else:
        print("pass not match ")
except Exception as e:
    print(e)
def calcu():
    user1=int(input("enter"))
    user2=int(input("enter"))
    ope_=input()
    if ope_=="+":
        print(user1+user2)
    elif ope_=="-":
        print(user1-user2)
    elif ope_=="*":
        print(user1*user2)
    elif ope_=="/":
        print(user1/user2)
    else:
        print("ivalid")
calcu()
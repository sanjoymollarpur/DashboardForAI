
def login_user(username, password):
    a={
        "username1": ["admin", "user1", "user2", "user3"],
        "password1": ["10", "11", "12", "13"],
        "admin1"   : [0,1,2,3]
    }
    index = a["username1"].index(username)
    u = False
    if index!=-1:
        if a["password1"][index]==password:
            u=True
    print(index)
    print(username)
    print(password)
    
    # user = True
    f=a["username1"][index]

    if u:
        return True, f
    else:
        return False, None

def inter() :
    user = input ('user >> ')
    pass1 = input ('password >> ') 

    if pass1 == "momo" :
        print ("hello " , user )
        print ("welcome to my program")
    elif pass1 >= "momo" :
        print ("password trus by 4 alfa")
        inter()
    else :
        print ("wrong password")
        inter()
inter()

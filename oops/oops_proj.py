class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input(""" Hello, How would you like to proceed
                        1. Press one to signup
                        2. Press two to signin
                        3. Press three to write a post
                        4. Press four to message a friend
                        5. Press any other key to exit \n""")

        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.message_friend() 
        else:
            exit()

    def signup(self):
        email=input("Enter your email: ")
        pwd=input("Enter your password: ")
        self.username=email
        self.password=pwd
        print("you have signedup succesfully") 
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing one in menu")
        else:
            uname=input("Enter your emai: ")
            pwd=input("Enter your password: ")
            if self.username==uname and self.password==pwd:
                print("You have signedin succesfully")
                self.loggedin= True
            else:
                print("please write correct information")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin==True:
            txt=input("Write the thing you want to post: ")
            print("Following content is psted successfully: {txt}")
        else:
            print("You need to signedin first")
        print("\n")
        self.menu()
    
    def message_friend(self):
        if self.loggedin==True:
            txt=input("write message that you want to send: ")
            print("message send successfully: {txt}")
        else:
            print("signedin first")
        print("\n")
        self.menu()

        
user=chatbook()


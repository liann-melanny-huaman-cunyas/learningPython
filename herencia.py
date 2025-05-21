class User :

    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self,username,password):
        if self.username == username and self.password == password:
            return True

        return False

class Admin(User) :
    def __init__(self, username, password,email):
        self.username=username
        self.password=password
        self.email=email

    def sens_email(self):
        print("####### Envaindo correo a", self.email)

    def login(self,username,password):
        if self.username == username and self.password == password:
            self.sens_email()
            return True

        return False

class Organizer(User):
    ...

admin =Admin("Admin1","password","correo@gmail.com")
organizer =Organizer("Organizer1","password")

print(admin.username)
print(admin.password)

print(
    organizer.login("Organizer","password")
)
print(
    admin.login("Admin1","password")
)
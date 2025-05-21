"""
Clases
class <NombreClase> ( ) :

<variable> =NombreClase()

"""
##forma inicial 
class User():
    username=""
    password=""
    email=""


user1=User()

user1.username="lianmelanny"
user1.password="1234"
user1.email="liann@gmail.com"


print("--------------")
print(user1.username)


##segunda forma 

class User :

    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

user1=User(
    username="lianmelanny",
    password="1234",
    email="liann@gmail.com"
)

print("--------------")
print(user1.username)
print(user1.password)
print(user1.email)

##tercera forma

class User :

    def __init__(self,username,password,email=None):
        self.username=username
        self.password=password
        self.email=email

    def say_hello(self):
        print("### Hola soy el usuario", self.username)

    def login(self,username,password):
        if self.username == username and self.password == password:
            self.say_hello()
            return True

        return False

user1=User(
    username="liannmelanny",
    password="1234",
)

print("--------------")
user1.login("liannmelanny","1234")

#### No hay atributos privados
### __password =password private name mangling

class User :

    def __init__(self,username,password,email=None):
        self.username=username
        self.__password=password ## privado
        self.email=email

user1=User(
    username="liannmelanny",
    password="1234",
)

###Properties
##Es un decorador que convierte un método en un atributo de solo lectura
# (o lectura-escritura si se combina con setters). Sirve para controlar
# el acceso a variables internas sin cambiar cómo se acceden desde fuera.

class User:

    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self._email = email  # usamos _email como atributo "privado"

    def say_hello(self):
        print("### Hola soy el usuario", self.username)

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.say_hello()
            return True
        return False

    # Getter
    @property
    def email(self):
        if self._email:
            return self._email
        return "No tiene email"

    # Setter
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("El email debe contener '@'")
        self._email = value


user1 = User(
    username="liannmelanny",
    password="1234"
)

print("Email:", user1.email)  # Muestra: No tiene email

user1.email = "liann@gmail.com"  # Asigna un nuevo email
print("Nuevo email:", user1.email)

# user1.email = "correo_sin_arroba"  # Esto lanzará un error: ValueError

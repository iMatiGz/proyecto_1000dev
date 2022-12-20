from tkinter import *
from tkinter.messagebox import *
from models.home_managers.register_model import *
import views.home_frames.login_view as lv

def go_back(controller):
    controller.show_frame(lv.Login)


def register(email, username, password, confirmed_password, controller):

    if email == "" or username == "" or password == "" or confirmed_password == "" or email == "Correo electrónico" or username == "Nombre de Usuario" or password == "Contraseña" or confirmed_password == "Confirmar contraseña":
        showerror(title="Error", message="Llene todos los campos")
        return False

    if password != confirmed_password:
        showerror(title="Error", message="Contraseñas incorrectas")
        return False

    if user_already_exists(email):
        showerror(title="Error", message="Usuario ya registrado")
        return False

    register_user(email, username, password, 0)
    showinfo(title="Registro exitoso", message="Usuario registrado satisfactoriamente")
    go_back(controller)
    return True
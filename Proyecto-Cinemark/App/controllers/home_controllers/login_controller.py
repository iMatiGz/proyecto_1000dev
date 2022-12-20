from tkinter import *
from tkinter.messagebox import *
from models.home_managers.login_model import *
import views.home_frames.register_view as rv

def register(controller):
    controller.show_frame(rv.Register)


def show_password(password_entry, value):

    if password_entry.get() != "Contraseña":

        if value.get() == 1:
            password_entry.config(show="")

        else:
            password_entry.config(show="*")


def login(email, password, controller):

    if email == "" or password == "" or email == "Correo electrónico" or password == "Contraseña":
        showerror(title="Error", message="Llene todos los campos")
        return False

    user_id = find_user(email, password)
    if user_id == 0:
        showerror(title="Error", message="Usuario o contraseña incorrectos")
        return False

    controller.set_frames_after_login(user_id)
    return True
    

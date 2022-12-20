from tkinter import *
from controllers.home_controllers.register_controller import *

class Register(Frame):

    def __init__(self, parent, views_manager):

        super().__init__(parent)
        self.controller = views_manager
        self.background_img = PhotoImage(file='App\images\home_background.png')
        Label(self, image=self.background_img).place(x=-2, y=-1)
        Frame(self, bg="#FFFFFF", width=390, height=530).place(x=460, y=0)
        
        self.labels()
        self.entries()
        self.buttons()
        self.binds()

    
    def labels(self):

        Label(self, text="Crea tu", font=("Segoe UI", 26, "bold"), justify=CENTER, bg="#FFFFFF", fg="#3f3f3f", bd=0).place(x=475, y=50)
        Label(self, text="Nueva Cuenta", font=("Segoe UI", 26, "bold", "underline"), justify=CENTER, bg="#FFFFFF", fg="#fc971c", bd=0).place(x=605, y=50)

    
    def entries(self):

        self.email_entry = Entry(self, font=("Segoe UI", 12), textvariable=StringVar(value="Correo electrónico"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=32, highlightbackground="#363636", highlightthickness=1, highlightcolor="#00a4db", relief=FLAT)
        self.email_entry.place(x=501, y=170)

        self.username_entry = Entry(self, font=("Segoe UI", 12), textvariable=StringVar(value="Nombre de Usuario"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=32, highlightbackground="#363636", highlightthickness=1, highlightcolor="#00a4db", relief=FLAT)
        self.username_entry.place(x=501, y=220)

        self.password_entry = Entry(self, font=("Segoe UI", 12), textvariable=StringVar(value="Contraseña"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=32, highlightbackground="#363636", highlightthickness=1, highlightcolor="#00a4db", relief=FLAT)
        self.password_entry.place(x=501, y=270)

        self.confirm_password_entry = Entry(self, font=("Segoe UI", 12), textvariable=StringVar(value="Confirmar contraseña"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=32, highlightbackground="#363636", highlightthickness=1, highlightcolor="#00a4db", relief=FLAT)
        self.confirm_password_entry.place(x=501, y=320)


    def buttons(self):

        self.go_back_button = Button(self, text="⬅ Volver", font=("Segoe UI", 12, "bold"), bg="#3769c6", fg="#FFFFFF", width=9, bd=1, activebackground="#2254b1", activeforeground="#FFFFFF", cursor="hand2", command=self.go_back)
        self.go_back_button.place(x=485, y=110)
        
        self.register_button = Button(self, text="REGISTER NOW", font=("Segoe UI", 13, "bold"), bg="#19b536", fg="#FFFFFF", width=30, bd=1, activebackground="#059b22", activeforeground="#FFFFFF", cursor="hand2", command=self.register)
        self.register_button.place(x=500, y=390)

    
    def binds(self):

        self.email_entry.bind("<FocusIn>", self.email_entry_clear_text)
        self.email_entry.bind("<FocusOut>", self.email_entry_show_text)
        self.username_entry.bind("<FocusIn>", self.username_entry_clear_text)
        self.username_entry.bind("<FocusOut>", self.username_entry_show_text)
        self.password_entry.bind("<FocusIn>", self.password_entry_clear_text)
        self.password_entry.bind("<FocusOut>", self.password_entry_show_text)
        self.confirm_password_entry.bind("<FocusIn>", self.confirm_password_entry_clear_text)
        self.confirm_password_entry.bind("<FocusOut>", self.confirm_password_entry_show_text)


    def email_entry_clear_text(self, e):

        if self.email_entry.get() == "Correo electrónico":
            self.email_entry.delete(0, "end")
            self.email_entry.config(fg="#000000")

    
    def email_entry_show_text(self, e):

        if self.email_entry.get() == "":
            self.email_entry.config(fg="#8f8f8f")
            self.email_entry.insert(0, "Correo electrónico")


    def username_entry_clear_text(self, e):

        if self.username_entry.get() == "Nombre de Usuario":
            self.username_entry.delete(0, "end")
            self.username_entry.config(fg="#000000")

    
    def username_entry_show_text(self, e):

        if self.username_entry.get() == "":
            self.username_entry.config(fg="#8f8f8f")
            self.username_entry.insert(0, "Nombre de Usuario")
    

    def password_entry_clear_text(self, e):

        if self.password_entry.get() == "Contraseña":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="#000000", show="*")

    
    def password_entry_show_text(self, e):

        if self.password_entry.get() == "":
            self.password_entry.config(fg="#8f8f8f", show="")
            self.password_entry.insert(0, "Contraseña")

    
    def confirm_password_entry_clear_text(self, e):

        if self.confirm_password_entry.get() == "Confirmar contraseña":
            self.confirm_password_entry.delete(0, "end")
            self.confirm_password_entry.config(fg="#000000", show="*")

    
    def confirm_password_entry_show_text(self, e):

        if self.confirm_password_entry.get() == "":
            self.confirm_password_entry.config(fg="#8f8f8f", show="")
            self.confirm_password_entry.insert(0, "Confirmar contraseña")


    def go_back(self):
        go_back(self.controller)


    def register(self):
        register(
            self.email_entry.get(),
            self.username_entry.get(),
            self.password_entry.get(),
            self.confirm_password_entry.get(),
            self.controller
        )
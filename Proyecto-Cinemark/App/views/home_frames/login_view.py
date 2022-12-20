from tkinter import *
from controllers.home_controllers.login_controller import *

class Login(Frame):

    def __init__(self, parent, views_manager):

        super().__init__(parent)
        self.controller = views_manager
        self.background_img = PhotoImage(file='App\images\home_background.png')
        Label(self, image=self.background_img).place(x=-2,y=-1)
        Frame(self, bg="#FFFFFF", width=390, height=530).place(x=460, y=0)

        self.labels()
        self.entries()
        self.buttons()
        self.other_components()
        self.binds()


    def labels(self):

        Label(self, text="Cinemark", font=("Segoe UI", 38, "bold", "underline"), justify=CENTER, bg="#FFFFFF", fg="#d60954", bd=0).place(x=531, y=93)
        Label(self, text="Bienvenido a", font=("Segoe UI", 31, "bold"), justify=CENTER, bg="#FFFFFF", fg="#1749a6", bd=0).place(x=524, y=50)


    def entries(self):

        self.email_entry = Entry(self, font=("Segoe UI", 12), relief=FLAT, textvariable=StringVar(value="Correo electrónico"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=30, highlightbackground="#363636", highlightthickness=1, highlightcolor="#037dff")
        self.email_entry.place(x=507, y=200)

        self.password_entry = Entry(self, font=("Segoe UI", 12), relief=FLAT, textvariable=StringVar(value="Contraseña"), bg="#FFFFFF", fg="#8f8f8f", bd=7, width=30, highlightbackground="#363636", highlightthickness=1, highlightcolor="#037dff")
        self.password_entry.place(x=507, y=260)


    def buttons(self):

        self.login_button = Button(self, font=("Segoe UI", 13, "bold"), text="LOGIN", width=10, bg="#19b536", fg="#FFFFFF", activebackground="#059b22", activeforeground="#FFFFFF", cursor="hand2", command=self.login)
        self.login_button.place(x=520, y=360)

        self.register_button = Button(self, font=("Segoe UI", 13, "bold"), text="REGISTER", width=10, bg="#3769c6", fg="#FFFFFF", activebackground="#2254b1", activeforeground="#FFFFFF", cursor="hand2", command=self.register)
        self.register_button.place(x=670, y=360)


    def other_components(self):

        self.value = IntVar()
        self.show_password_check = Checkbutton(self, font=("Segoe UI", 11), text="Mostrar contraseña", variable=self.value, bg="#FFFFFF", activebackground="#FFFFFF", cursor="hand2", command=self.show_password)
        self.show_password_check.place(x=502, y=303)


    def binds(self):

        self.email_entry.bind("<FocusIn>", self.email_clear_default_text)
        self.email_entry.bind("<FocusOut>", self.email_show_default_text)
        self.password_entry.bind("<FocusIn>", self.password_clear_default_text)
        self.password_entry.bind("<FocusOut>", self.password_show_default_text)
        self.password_entry.bind("<Return>", self.login)


    def email_clear_default_text(self, e):

        if self.email_entry.get() == "Correo electrónico":
            self.email_entry.delete(0, "end")
            self.email_entry.config(fg="#000000")


    def email_show_default_text(self, e):

        if self.email_entry.get() == "":
            self.email_entry.config(fg="#8f8f8f")
            self.email_entry.insert(0, "Correo electrónico")


    def password_clear_default_text(self, e):

        if self.password_entry.get() == "Contraseña":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="#000000", show="*")


    def password_show_default_text(self, e):

        if self.password_entry.get() == "":
            self.password_entry.config(fg="#8f8f8f", show="")
            self.password_entry.insert(0, "Contraseña")


    def login(self, e=0):
        login(
            self.email_entry.get(),
            self.password_entry.get(),
            self.controller
        )


    def register(self):
        register(self.controller)


    def show_password(self):
        show_password(self.password_entry, self.value)
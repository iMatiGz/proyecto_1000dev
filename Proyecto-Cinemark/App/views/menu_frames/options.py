from tkinter import *
from PIL import Image as ImagePIL, ImageTk
from controllers.menu_controllers.options_controller import *

class Options(Frame):

    def __init__(self, parent, views_manager, user_id):

        super().__init__(parent)
        self.controller = views_manager
        self.user_id = user_id
        self.config(bg="#f7e220")
        Frame(self, bg="#636363", width=850, height=2).place(x=0, y=0)
        Frame(self, bg="#FFFFFF", width=850, height=50).place(x=0, y=2)
        Frame(self, bg="#636363", width=850, height=2).place(x=0, y=50)

        self.icons()
        self.labels()
        self.buttons()


    def icons(self):
        
        self.make_reservation_icon = ImagePIL.open('App\images\make_reservation_icon.png')
        self.make_reservation_icon = self.make_reservation_icon.resize((120, 120), ImagePIL.ANTIALIAS)
        self.make_reservation_icon = ImageTk.PhotoImage(self.make_reservation_icon)
        
        self.see_reservations_icon = ImagePIL.open('App\images\see_reservations_icon.png')
        self.see_reservations_icon = self.see_reservations_icon.resize((120, 120), ImagePIL.ANTIALIAS)
        self.see_reservations_icon = ImageTk.PhotoImage(self.see_reservations_icon)

        self.modify_reservation_icon = ImagePIL.open('App\images\modify_reservation_icon.png')
        self.modify_reservation_icon = self.modify_reservation_icon.resize((120, 120), ImagePIL.ANTIALIAS)
        self.modify_reservation_icon = ImageTk.PhotoImage(self.modify_reservation_icon)

        self.reservation_history_icon = ImagePIL.open('App\images\history_icon.png')
        self.reservation_history_icon = self.reservation_history_icon.resize((120, 120), ImagePIL.ANTIALIAS)
        self.reservation_history_icon = ImageTk.PhotoImage(self.reservation_history_icon)


    def labels(self):

        Label(self, text=f"Bienvenido {username(self.user_id)}", font=("Segoe UI", 20, "bold"), bg="#FFFFFF", fg="#000000", width=53, justify=CENTER, bd=0).place(x=0, y=3)
        
        Label(self, text="MENU PRINCIPAL", font=("Segoe UI", 26, "bold", "underline"), bg="#97e310", fg="#5c8a0a", bd=0, width=34, justify=CENTER).place(x=65, y=60)
        
        Label(self, text="Hacer una reserva", font=("Segoe UI", 15, "bold", "italic"), bg="#7a7a79", fg="#FFFFFF").place(x=138, y=256)
        
        Label(self, text="Tus reservas", font=("Segoe UI", 15, "bold", "italic"), bg="#7a7a79", fg="#FFFFFF").place(x=562, y=256)
        
        Label(self, text="Modificar una reserva", font=("Segoe UI", 15, "bold", "italic"), bg="#7a7a79", fg="#FFFFFF").place(x=119, y=446)
        
        Label(self, text="Historial de reservas", font=("Segoe UI", 15, "bold", "italic"), bg="#7a7a79", fg="#FFFFFF").place(x=523, y=446)


    def buttons(self):

        self.make_reservation_button = Button(self, bg="#FFFFFF", relief=RIDGE, image=self.make_reservation_icon, cursor="hand2", command=self.make_reservation)
        self.make_reservation_button.place(x=162, y=130)

        self.see_reservations_button = Button(self, bg="#FFFFFF", relief=RIDGE, image=self.see_reservations_icon, cursor="hand2", command=self.see_reservations)
        self.see_reservations_button.place(x=560, y=130)

        self.modify_reservation_button = Button(self, bg="#FFFFFF", relief=RIDGE, image=self.modify_reservation_icon, cursor="hand2", command=self.modify_reservation)
        self.modify_reservation_button.place(x=162, y=320)

        self.reservation_history_button = Button(self, bg="#FFFFFF", relief=RIDGE, image=self.reservation_history_icon, cursor="hand2", command=self.reservation_history)
        self.reservation_history_button.place(x=560, y=320)
   

    def make_reservation(self):
        make_reservation(self.controller, self.user_id)

    
    def see_reservations(self):
        see_reservations(self.controller, self.user_id)


    def modify_reservation(self):
        modify_reservation(self.controller, self.user_id)


    def reservation_history(self):
        reservation_history(self.controller, self.user_id)
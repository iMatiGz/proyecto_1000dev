from tkinter import *

class Ticket(Toplevel):

    def __init__(self, movie, date, schedule, user_id, seats, buy_reservation, controller, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.movie = movie
        self.date = date
        self.schedule = schedule
        self.user_id = user_id
        self.seats = seats
        self.buy_reservation = buy_reservation
        self.controller = controller
        self.title("Ticket de compra")
        self.geometry(self.set_geometry())
        self.resizable(False, False)
        self.main_frame = Frame(self, bg="#FFFFFF")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.labels()
        self.button()

        self.mainloop()

    def set_geometry(self):

        x_window = self.winfo_screenwidth() // 2 - 390 // 2
        y_window = self.winfo_screenheight() // 2 - 550 // 2
        screen_position = str(390) + "x" + str(550) + "+" + str(x_window) + "+" + str(y_window - 15)    
        return screen_position


    def labels(self):

        Label(self.main_frame, text="TICKET DE COMPRA", font=("Segoe UI", 16, "bold", "underline"), justify=LEFT, bg="#FFFFFF", fg="#000000", bd=0).place(x=95, y=10)

        Label(self.main_frame, text=f"PELICULA:  {self.movie}\n\n\nFECHA:  {self.date}\n\n\nHORARIO:  {self.schedule}\n\n\nSALA:  {5}\n\n\nASIENTOS:  {self.seats}", font=("Segoe UI", 12, "bold"), justify=LEFT, bg="#FFFFFF", fg="#000000", bd=0, padx=10).place(x=5, y=90)


    def button(self):

        self.buy_button = Button(self.main_frame, text="COMPRAR", font=("Segoe UI", 13, "bold"), bg="#5ee827", fg="#0a0a0a", width=16, bd=1, activebackground="#4ec71e", activeforeground="#0a0a0a", cursor="hand2", command=self.buy)
        self.buy_button.place(x=110, y=500)


    def buy(self):

        self.buy_reservation(self.movie, self.date, self.schedule, self.user_id, self.seats, 5, self.controller)
        self.destroy()
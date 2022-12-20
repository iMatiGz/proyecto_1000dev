from tkinter import *
from controllers.menu_controllers.seats_controller import *


class SeatsWindow(Toplevel):

    def __init__(self, view, save_seats_function, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.view = view
        self.save_seats_function = save_seats_function
        self.title("Selección de Asientos")
        self.resizable(False, False)
        self.geometry(self.set_geometry())
        self.main_frame = Frame(self, bg="#FFFFFF")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.labels()
        self.seats()
        self.buttons()

        self.mainloop()


    def set_geometry(self):

        x_window = self.winfo_screenwidth() // 2 - 550 // 2
        y_window = self.winfo_screenheight() // 2 - 600 // 2
        screen_position = str(550) + "x" + str(600) + "+" + str(x_window) + "+" + str(y_window - 15)    
        return screen_position


    def labels(self):

        Label(self.main_frame, text="-------------------PANTALLA-------------------", font=("Segoe UI", 16), bg="#FFFFFF", bd=0).place(x=65, y=7)
        
        Label(self.main_frame, text="A\nB\nC\nD\nE\nF\nG\nH", font=("Segoe UI", 20), bg="#FFFFFF", bd=0).place(x=53, y=85)
        
        Label(self.main_frame, text="A\nB\nC\nD\nE\nF\nG\nH", font=("Segoe UI", 20), bg="#FFFFFF", bd=0).place(x=470, y=85)
        
        Label(self.main_frame, text="1     2     3    4    5     6    7    8    9    10", font=("Segoe UI", 16), bg="#FFFFFF", bd=0).place(x=92, y=392)
        
        Label(self.main_frame, text="(Máx. 6 asientos)", font=("Segoe UI", 12, "underline"), bg="#FFFFFF", bd=0).place(x=210, y=50)
        
        self.remaining_seats = 6
        self.remaining_seats_label = Label(self.main_frame, text=f"Asientos restantes: {self.remaining_seats}", font=("Segoe UI", 14, "underline"), bg="#FFFFFF", bd=0)
        self.remaining_seats_label.place(x=190, y=435)



    def seats(self):

        self.saved_seats = []

        x_coord = 90
        y_coord = 90
        seat_letter = ("A","B","C","D","E","F","G","H")
        self.seats_list = []

        for row in range(8):
            for column in range(10):

                self.seats_list.append(Seat(self, self.main_frame, seat_letter[row], column+1, x_coord, y_coord))
                x_coord += 37

            x_coord = 90
            y_coord += 37


    def buttons(self):

        self.cancel_button = Button(self.main_frame, text="CANCELAR", font=("Segoe UI", 14, "bold"), bg="#d90910", fg="#FFFFFF", width=17, bd=1, activebackground="#b8070d", activeforeground="#FFFFFF", cursor="hand2", command=self.cancel)
        self.cancel_button.place(x=50, y=540)

        self.clear_selection_button = Button(self.main_frame, text="LIMPIAR SELECCIÓN", font=("Segoe UI", 14, "bold"), bg="#f7b602", fg="#FFFFFF", width=18, bd=1, activebackground="#cf9802", activeforeground="#FFFFFF", cursor="hand2", command=self.clear_selection)
        self.clear_selection_button.place(x=170, y=480)

        self.accept_button = Button(self.main_frame, text="ACEPTAR", font=("Segoe UI", 14, "bold"), bg="#5ee827", fg="#0a0a0a", width=17, bd=1, activebackground="#4ec71e", activeforeground="#0a0a0a", cursor="hand2", command=self.save_seats)
        self.accept_button.place(x=310, y=540)


    def cancel(self):
        close_window(self)

    
    def clear_selection(self):
        clear_selection(self)


    def save_seats(self):
        save_seats(self, self.save_seats_function, self.view)


class Seat:

    def __init__(self, window, main_frame, seat_letter, seat_number, x_coord, y_coord):

        self.is_chosen = False
        self.window = window
        self.seat_letter = seat_letter
        self.seat_number = str(seat_number)
        self.button = Button(main_frame, text="|_|", font=(9), bg="#dffaf4", fg="#000000", command=self.chosen_seat)
        self.button.place(x=x_coord, y=y_coord)
        

    def chosen_seat(self):
        if self.is_chosen is False:
            chosen_seat(self, self.window)

    
    def disable_seat(self):

        self.button.config(state="disabled")

    
    def reset_seat(self):

        self.is_chosen = False
        self.button.config(bg="#bcf7f0", state="normal")
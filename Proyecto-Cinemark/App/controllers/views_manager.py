from tkinter import *
from views.home_frames.login_view import Login
from views.home_frames.register_view import Register
from views.menu_frames.options import Options
from views.menu_frames.make_reserv.make_reservation import MakeReservation
from views.menu_frames.see_reservations import SeeReservations
from views.menu_frames.modify_reservation import ModifyReservation
from views.menu_frames.reservation_history import ReservationHistory

class ViewsManager(Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Inicio de Sesión")
        self.geometry(self.set_geometry())
        self.resizable(False, False)
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=BOTH, expand=True)
        self.main_frame.grid_columnconfigure(0, weight = 1)
        self.main_frame.grid_rowconfigure(0, weight = 1)
        self.home_frames = {}
        for F in (Login, Register):
            frame = F(self.main_frame, self)
            self.home_frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(Login)


    def set_geometry(self):

        x_window = self.winfo_screenwidth() // 2 - 850 // 2
        y_window = self.winfo_screenheight() // 2 - 530 // 2
        screen_position = str(850) + "x" + str(530) + "+" + str(x_window) + "+" + str(y_window - 15)    
        return screen_position


    def show_frame(self, frame, user_id = 0):
        
        self.reset_frame(frame, user_id)

        if user_id == 0:
            frame_in_view = self.home_frames[frame]
        else:
            frame_in_view = self.menu_frames[frame]
            
        frame_in_view.tkraise()

    
    def reset_frame(self, Frame, user_id = 0):
        
        if user_id == 0:
            self.home_frames[Frame].destroy()
            new_frame = Frame(self.main_frame, self)
            self.home_frames[Frame] = new_frame
            new_frame.grid(row = 0, column = 0, sticky = NSEW)

        else:
            self.menu_frames[Frame].destroy()
            new_frame = Frame(self.main_frame, self, user_id)
            self.menu_frames[Frame] = new_frame
            new_frame.grid(row = 0, column = 0, sticky = NSEW)

 
    def set_frames_after_login(self, user_id):

        self.menu_frames = {}
        for F in (Options, MakeReservation, SeeReservations, ModifyReservation, ReservationHistory):
            frame = F(self.main_frame, self, user_id)
            self.menu_frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(Options, user_id)


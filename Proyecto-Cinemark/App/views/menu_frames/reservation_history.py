from tkinter import *

class ReservationHistory(Frame):

    def __init__(self, parent, views_manager, user_id):

        super().__init__(parent)
        self.controller = views_manager
        self.user_id = user_id
        self.config(bg="#FFFF00")
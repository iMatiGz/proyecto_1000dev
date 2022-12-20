from tkinter import *
from tkinter.ttk import Combobox
from controllers.menu_controllers.make_reserv_controller import *

class MakeReservation(Frame):

    def __init__(self, parent, views_manager, user_id):

        super().__init__(parent)
        self.controller = views_manager
        self.user_id = user_id
        self.seats = []
        self.config(bg="#f7e220")
        Frame(self, bg="#636363", width=850, height=2).place(x=0, y=0)
        Frame(self, bg="#FFFFFF", width=850, height=50).place(x=0, y=2)
        Frame(self, bg="#636363", width=850, height=2).place(x=0, y=50)

        self.labels()
        self.comboBox()
        self.buttons()
        self.binds()


    def labels(self):

        Label(self, text="Hacer una reserva", font=("Segoe UI", 20, "bold"), bg="#FFFFFF", fg="#000000", width=53, justify=CENTER).place(x=0, y=3)

        Label(self, text="Selecciona una película", font=("Segoe UI", 14, "bold", "italic"), bg="#f59922", fg="#FFFFFF").place(x=60, y=100)

        self.movie_info_label = Label(self, font=("Segoe UI", 15, "bold"), bg="#f7e220", fg="#000000", justify=LEFT, bd=0)
        self.movie_info_label.place(x=10, y=220)
        
        self.date_label = Label(self, text="Selecciona una fecha", font=("Segoe UI", 14, "bold", "italic"), bg="#f59922", fg="#FFFFFF")
        self.date_label.place(x=340, y=100)

        self.schedule_label = Label(self, text="Selecciona el horario", font=("Segoe UI", 14, "bold", "italic"), bg="#f59922", fg="#FFFFFF")
        self.schedule_label.place(x=600, y=100)


    def comboBox(self):

        self.movie_comboBox = Combobox(self, values=get_movies(), justify=LEFT, state="readonly", font=("Segoe UI", 11), width=25)
        self.movie_comboBox.place(x=55, y=140)

        dates = ["20/12/2022","21/12/2022","22/12/2022","23/12/2022","24/12/2022","25/12/2022","26/12/2022"]
        self.date_comboBox = Combobox(self, values=dates, justify=LEFT, state="disabled", font=("Segoe UI", 11), width=12)
        self.date_comboBox.place(x=375, y=140)

        schedules = ["18:30hs","19:45hs","20:00hs","21:00hs","22:30hs","23:25hs","00:30hs"]
        self.schedule_comboBox = Combobox(self, values=schedules, justify=LEFT, state="disabled", font=("Segoe UI", 11), width=10)
        self.schedule_comboBox.place(x=645, y=140)


    def buttons(self):

        self.go_back_button = Button(self, text="⬅ Volver", font=("Segoe UI", 11, "bold"), bg="#3769c6", fg="#FFFFFF", width=9, bd=1, activebackground="#2254b1", activeforeground="#FFFFFF", cursor="hand2", command=self.go_back)
        self.go_back_button.place(x=9, y=9)

        self.choose_seats_button = Button(self, text="Seleccione sus asientos", font=("Segoe UI", 14, "bold"), state="disabled", bg="#5ee827", fg="#0a0a0a", width=22, bd=1, activebackground="#4ec71e", activeforeground="#0a0a0a", cursor="hand2", command=self.choose_seats)
        self.choose_seats_button.place(x=540, y=360)

        self.go_next_button = Button(self, text="SIGUIENTE", font=("Segoe UI", 14, "bold"), state="disabled", bg="#3769c6", fg="#FFFFFF", width=15, bd=1, activebackground="#2254b1", activeforeground="#FFFFFF", cursor="hand2", command=self.go_next)
        self.go_next_button.place(x=580, y=420)


    def binds(self):

        self.movie_comboBox.bind("<<ComboboxSelected>>", self.movie_selected)
        self.date_comboBox.bind("<<ComboboxSelected>>", self.date_selected)
        self.schedule_comboBox.bind("<<ComboboxSelected>>", self.schedule_selected)
        

    def movie_selected(self, e):
        movie_selected(self, self.movie_comboBox.get())


    def date_selected(self, e):
        date_selected(self)


    def schedule_selected(self, e):
        schedule_selected(self)


    def go_back(self):
        go_back(self.controller, self.user_id)


    def choose_seats(self):
        open_seats_window(self)


    def go_next(self):

        show_reservation_details(
            self.controller,
            self.movie_comboBox.get(),
            self.date_comboBox.get(),
            self.schedule_comboBox.get(),
            self.user_id,
            self.seats
        )
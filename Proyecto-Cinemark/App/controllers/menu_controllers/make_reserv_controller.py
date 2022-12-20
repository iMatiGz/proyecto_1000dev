from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from views.menu_frames import options as op
from views.menu_frames.make_reserv.seats_view import SeatsWindow
from views.menu_frames.make_reserv.ticket_view import Ticket
from models.menu_managers.make_reserv_manager import *

def go_back(controller, user_id):
    controller.show_frame(op.Options, user_id)


def get_movies():

    movies = get_movies_name()
    names = []
    for movie in movies:
        names.append(movie[0])

    return names


def movie_selected(view, movie):

    movie_info = get_movie_info(movie)

    view.movie_info_label.config(text=f"""
        Director: {movie_info[0]}\n
        Género: {movie_info[1]}\n
        Duración: {movie_info[2]}\n
        Fecha de Estreno: {movie_info[3]}
    """)
    view.date_comboBox.config(state="readonly")


def date_selected(view):
    view.schedule_comboBox.config(state="readonly")


def schedule_selected(view):
    view.choose_seats_button.config(state="normal")


def open_seats_window(view):

    SeatsWindow(view, save_seats)


def enable_go_next_button(view):
    view.go_next_button.config(state="normal")


def save_seats(view, seats_list):
    
    enable_go_next_button(view)
    view.seats = seats_list


def show_reservation_details(controller, movie, date, schedule, user_id, seats):

    seats_list = ""
    for seat in seats:
        seats_list += seat + " - "

    Ticket(movie, date, schedule, user_id, seats_list, buy_reservation, controller)


def buy_reservation(movie, date, schedule, user_id, seats, lounge, controller):
    insert_reservation_on_table(movie, date, schedule, user_id, seats, lounge)
    showinfo(title="Compra exitosa", message="Su compra ha sido registrada satisfactoriamente")
    go_back(controller, user_id)
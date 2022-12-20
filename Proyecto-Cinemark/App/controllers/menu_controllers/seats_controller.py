from tkinter import *

def chosen_seat(seat, view):
    seat.button.config(bg="#fcfc0a")
    seat.is_chosen = True
    discount_seats(view)

    if view.remaining_seats == 0:
        disable_seats(view)


def discount_seats(view):

    view.remaining_seats -= 1
    view.remaining_seats_label.config(text=f"Asientos restantes: {view.remaining_seats}")


def disable_seats(view):

    for seat in view.seats_list:
            seat.disable_seat()


def close_window(view):
    view.destroy()


def clear_selection(view):

    view.remaining_seats = 6
    view.remaining_seats_label.config(text=f"Asientos restantes: {view.remaining_seats}")
    for seat in view.seats_list:
         seat.reset_seat()


def save_seats(view, save_seats_function, make_reserv_view):

    chosen_seats = []

    for seat in view.seats_list:
        if seat.is_chosen is True:
            seat_coords = seat.seat_letter + "-" + seat.seat_number
            chosen_seats.append(seat_coords)

    save_seats_function(make_reserv_view, chosen_seats)
    view.destroy()
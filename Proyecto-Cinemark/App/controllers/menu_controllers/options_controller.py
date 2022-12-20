from tkinter import *
from models.menu_managers.options_manager import *
from views.menu_frames.make_reserv import make_reservation as mr
from views.menu_frames import see_reservations as sr, modify_reservation as mod_r, reservation_history as rh

def username(user_id):
    return get_username(user_id)


def make_reservation(controller, user_id):
    controller.show_frame(mr.MakeReservation, user_id)


def see_reservations(controller, user_id):
    controller.show_frame(sr.SeeReservations, user_id)


def modify_reservation(controller, user_id):
    controller.show_frame(mod_r.ModifyReservation, user_id)


def reservation_history(controller, user_id):
    controller.show_frame(rh.ReservationHistory, user_id)
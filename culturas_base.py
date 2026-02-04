from __builtins__ import *
import mover
import basic

def main_trigo():
    basic.verificar_solo(Grounds.Grassland)

def main_madeira():
    main_trigo()
    if (get_pos_x() % 2 == 0) and (get_pos_y() % 2 == 0):
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

def main_cenoura():
    basic.verificar_solo(Grounds.Soil)
    plant(Entities.Carrot)



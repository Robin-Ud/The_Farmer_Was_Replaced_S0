from __builtins__ import *
import mover
import basic

#primeira func pros girassois
def main_girassois():
    
    balde = {}
    lista_cordenadas = []
    mover.ir_pro_inicio()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            
            basic.esperar_crescer_e_colher()
            
            basic.verificar_solo(Grounds.Soil)
            plant(Entities.Sunflower)
            
            if measure() > 10:
                use_item(Items.Water)
            petalas = measure()
            
            if petalas not in balde:
                balde[petalas] = []

            balde[petalas].append((get_pos_x(), get_pos_y()))
            move(North)
        move(East)
    for n_petalas in range(15, 6, -1):

        if n_petalas in balde:
            lista_cordenadas = balde[n_petalas]

        for pos in lista_cordenadas:
            mover.para(pos[0], pos[1])
            while not can_harvest():
                continue
            harvest()


def main_abobora():

    aboboras_podres = []
    mover.ir_pro_inicio()

    for i in range(get_world_size()):
        for j in range(get_world_size()):
            
            if can_harvest():
                harvest()
            basic.verificar_solo(Grounds.Soil)
            plant(Entities.Pumpkin)

            move(North)
        move(East)

    for i in range(get_world_size()):
        for j in range(get_world_size()):

            if not can_harvest():
                aboboras_podres.append((get_pos_x(), get_pos_y()))
                plant(Entities.Pumpkin)
            move(North)
        move(East)

    while aboboras_podres:
        for abobora in aboboras_podres:
            mover.para(abobora[0], abobora[1])
            if can_harvest():
                aboboras_podres.remove(abobora)
            else:
                plant(Entities.Pumpkin)
    pet_the_piggy()
    harvest()

def main_cactus():
    
    mover.ir_pro_inicio()

    #plantar organizando rola?

    for i in range(get_world_size()):
        for j in range(get_world_size()):

            basic.esperar_crescer_e_colher()
            basic.verificar_solo(Grounds.Soil)

            plant(Entities.Cactus)

            #if measure() < measure(South):
             #   swap(South)

            move(North)

        move(East)

    # organizando
    for i in range(get_world_size()):

        organizado = False

        while organizado != True:
            organizado = True
            for j in range(get_world_size()):

                if get_entity_type() != Entities.Cactus:
                    if can_harvest():
                        harvest()
                    basic.verificar_solo(Grounds.Soil)
                    plant(Entities.Cactus)

                if measure() > measure(North) and get_pos_y() != get_world_size()-1:
                    swap(North)
                    organizado = False

                if measure() < measure(South) and (get_pos_y() != 0):
                    swap(South)
                    organizado = False

                move(North)

        move(East)
    for i in range(get_world_size()):

        organizado = False

        while organizado != True:
            organizado = True
            for j in range(get_world_size()):

                if measure() > measure(East) and get_pos_x() != get_world_size()-1:
                    swap(East)
                    organizado = False

                if measure() < measure(West) and (get_pos_x() != 0):
                    swap(West)
                    organizado = False

                move(East)

        move(North)

    harvest()

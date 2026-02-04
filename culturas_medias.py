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
    # --- Parte de Plantar (Mantive igual) ---
    mover.ir_pro_inicio()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() != Entities.Cactus:
                plant(Entities.Cactus)
            move(North)
        move(East)
    
    # --- Parte de Ordenar (Sua lógica corrigida) ---
    organizado = False
    
    while not organizado:
        # Reset obrigatório pro inicio a cada passada completa
        mover.ir_pro_inicio()
        organizado = True 

        for x in range(get_world_size()):
            for y in range(get_world_size()):
                
                # 1. Verifica LESTE (Protegendo pra não bater na parede)
                if x < get_world_size() - 1:
                    if measure(East) < measure():
                        swap(East)
                        organizado = False
                        # NÃO use continue aqui. Deixe ele checar o Norte também.

                # 2. Verifica NORTE (Protegendo pra não bater no teto)
                if y < get_world_size() - 1:
                    if measure(North) < measure():
                        swap(North)
                        organizado = False
                
                # 3. Movimento (Agora ele só sobe se não estiver no teto)
                if y < get_world_size() - 1:
                    move(North)
            
            # --- Correção Crítica ---
            # Terminou a coluna (tá lá no topo). Vai pra direita...
            if x < get_world_size() - 1:
                move(East)
                # ...E DESCE TUDO pro chão (y=0) pra começar a próxima!
                # Sem isso, ele começa a próxima coluna lá de cima.
                while get_pos_y() > 0:
                    move(South)

    harvest()

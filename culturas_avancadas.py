import mover
import basic

def main_dino():
    mover.ir_pro_inicio()
    clear()
    change_hat(Hats.Dinosaur_Hat)
    size = get_world_size() - 1

    def mover_seguro(direcao):
        resultado = move(direcao)
        if not resultado:
            change_hat(Hats.Brown_Hat)
        return resultado

    while True:
        # Sobe de y=0 até y=1 pra começar
        if not mover_seguro(North):
            return

        for col in range(size + 1):
            if col % 2 == 0:
                # Sobe de y=1 até y=11
                while get_pos_y() != size:
                    if not mover_seguro(North):
                        return
            else:
                # Desce de y=11 até y=1
                while get_pos_y() != 1:
                    if not mover_seguro(South):
                        return

            if col != size:
                if not mover_seguro(East):
                    return

        # Na última coluna desce até y=0
        while get_pos_y() != 0:
            if not mover_seguro(South):
                return

        # Volta pra x=0 pela linha y=0
        while get_pos_x() != 0:
            if not mover_seguro(West):
                return

def main_concorcio(meta):
    basic.verificar_solo(Grounds.Grassland)
    
    while (num_items(Items.Hay) and num_items(Items.Wood) and num_items(Items.Carrot)) < meta:
        if get_entity_type():
            culturadesejada, (tx, ty) = get_companion()
        quick_print(culturadesejada, tx, ty)
        mover.para(tx, ty)
        if culturadesejada == Entities.Carrot:
            basic.verificar_solo(Grounds.Soil)
        elif culturadesejada == (Entities.Tree or Entities.Bush):
            basic.verificar_solo(Grounds.Grassland)
            use_item(Items.Water)
            
        else:
            basic.verificar_solo(Grounds.Grassland)
        plant(culturadesejada)

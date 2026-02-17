import mover

def main_dino():
    mover.ir_pro_inicio()
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

main_dino()

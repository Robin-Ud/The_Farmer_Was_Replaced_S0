def mover_no_eixo(destino, atual, direcao_positiva, direcao_negativa):
    distancia = destino - atual
    tamanho = get_world_size()

    # Lógica do "Mundo Redondo" (Toro)
    if distancia > tamanho / 2:
        distancia -= tamanho
    elif distancia < -tamanho / 2:
        distancia += tamanho

    # Execução do movimento
    while distancia != 0:
        if distancia > 0:
            move(direcao_positiva)
            distancia -= 1
        else:
            move(direcao_negativa)
            distancia += 1

def para(x, y):
    # Resolve o eixo X (Leste/Oeste)
    mover_no_eixo(x, get_pos_x(), East, West)
    
    # Resolve o eixo Y (Norte/Sul)
    mover_no_eixo(y, get_pos_y(), North, South)
    
def ir_pro_inicio():
    para(0,0)

def percorrer_campo(acao):
    para(0,0)
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            acao()
            move(North)
        move(East)
    
    
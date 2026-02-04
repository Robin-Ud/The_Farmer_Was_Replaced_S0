from culturas_base import *
from culturas_medias import *

def verificar_solo(tipo_de_solo):
    if can_harvest():
        harvest() 
    if get_ground_type() != tipo_de_solo:
        till()


def farmar(cultura, meta):
    # Mapeamento direto: associa a função ao item
    
    # O CATÁLOGO: Mapeia "Nome" -> (Função, Item)
    # Isso elimina a necessidade de if/else ou múltiplos dicionários
    catalogo = {
        "trigo":   (main_trigo,   Items.Hay),
        "madeira": (main_madeira, Items.Wood),
        "cenoura": (main_cenoura, Items.Carrot),
        "energia": (main_girassois, Items.Power),
        "abobora": (main_abobora, Items.Pumpkin)
    }
    
    usam_percorrer = ["trigo", "madeira", "cenoura"] 
    
    # Verifica se o nome existe para não crashar
    if cultura in catalogo:
        funcao, item = catalogo[cultura]
        
        while num_items(item) < meta:
            if cultura in usam_percorrer:
                mover.percorrer_campo(funcao)
            else:
                funcao()
    else:
        quick_print("Erro: Cultura nao existe na tabela!")



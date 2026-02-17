from culturas_base import *
from culturas_medias import *
from culturas_avancadas import *

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
        "abobora": (main_abobora, Items.Pumpkin),
        "cacto": (main_cactus, Items.Cactus),
        "osso": (main_dino, Items.Bone)
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

def esperar_crescer_e_colher():
    
    if get_entity_type() != Entities.Dead_Pumpkin:
        while not can_harvest() and get_entity_type() != None:
            continue
    if can_harvest():
        harvest()
        
        
def sort_hat():
    chapeus = [
    Hats.Brown_Hat,
    Hats.Cactus_Hat,
    Hats.Carrot_Hat,
    Hats.Gray_Hat,
    Hats.Green_Hat,
    Hats.Pumpkin_Hat,
    Hats.Purple_Hat,
    Hats.Straw_Hat,
    Hats.Sunflower_Hat,
    Hats.Traffic_Cone,
    Hats.Tree_Hat,
    Hats.Wizard_Hat,
    ]

    change_hat(chapeus[num_items(Items.Water) % len(chapeus)])
    quick_print(chapeus[num_items(Items.Water) % len(chapeus)])

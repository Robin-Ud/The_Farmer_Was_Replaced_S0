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

# def farmar_basicos(cultura, meta):
#     # Mapeamento direto: associa a função ao item
#     
#     # O CATÁLOGO: Mapeia "Nome" -> (Função, Item)
#     # Isso elimina a necessidade de if/else ou múltiplos dicionários
#     catalogo = {
#         "trigo":   (main_trigo,   Items.Hay),
#         "madeira": (main_madeira, Items.Wood),
#         "cenoura": (main_cenoura, Items.Carrot)
#     }
# 
#     # Verifica se o nome existe para não crashar
#     if cultura in catalogo:
#         funcao, item = catalogo[cultura]
#         
#         while num_items(item) < meta:
#             mover.percorrer_campo(funcao)
#     else:
#         quick_print("Erro: Cultura nao existe na tabela!")

def farmar_basicos(cultura, meta):
	# Valores padrão (caso digite errado, farma trigo)
	item = Items.Hay
	funcao = main_trigo

	if cultura == "trigo":
		item = Items.Hay
		funcao = main_trigo
	elif cultura == "madeira":
		item = Items.Wood
		funcao = main_madeira
	elif cultura == "cenoura":
		item = Items.Carrot
		funcao = main_cenoura
		
	# Loop de execução
	while num_items(item) < meta:
		mover.percorrer_campo(funcao)

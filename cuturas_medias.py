from __builtins__ import *
import mover
import basic

#primeira func pros girassois
def main_girassois():

	# 1. Criar os baldes (Buckets)
	# Vamos supor que queremos separar girassóis por pétalas (ex: de 12 a 15)
	buckets = {12: [], 13: [], 14: [], 15: []}

	# 2. Escanear o campo e distribuir nos baldes
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			mover.para(x, y)
			petals = measure() # Mede as pétalas do girassol
			if petals in buckets:
				buckets[petals].append((x, y))

	# 3. Colher na ordem desejada (do balde com mais pétalas para o menor)
	for p in sorted(buckets.keys()):
		for coords in buckets[p]:
			mover.para(coords[0], coords[1])
			harvest()

def plant_all():
	basic.verificar_solo(Grounds.Soil)
	plant(Entities.Pumpkin)
	
def farmar_aboboras():
	plantas_saudaveis = 0
	
	#primeiro loop pra plantar
	mover.percorrer_campo(plant_all)
	
	mover.ir_pro_inicio()
	while plantas_saudaveis != get_world_size()**2:
		if can_harvest():
			plantas_saudaveis += 1
		else:
			plant(Entities.Pumpkin)
		if get_pos_y() == get_world_size()-1:
			move(East)
		move(North)
		if plantas_saudaveis == get_world_size()**2:
			break
		if get_pos_x() == 0 and get_pos_y() == 0:
			plantas_saudaveis = 0
		
	harvest()
			

import culturas_base 
from game_defs import *

meta = 1
while True:
	meta *= 1.1
	quick_print(meta*5, meta*4, meta*3)
	culturas_base.farmar_basicos("trigo", meta*5)
	culturas_base.farmar_basicos("madeira", meta*4)
	culturas_base.farmar_basicos("cenoura", meta*3)



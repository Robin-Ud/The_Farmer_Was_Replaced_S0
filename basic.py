def verificar_solo(tipo_de_solo):
	if can_harvest():
		harvest() 
	if get_ground_type() != tipo_de_solo:
		till()




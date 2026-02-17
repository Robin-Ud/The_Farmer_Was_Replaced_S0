from __builtins__ import *
import basic 

meta = 1
while True:
    meta *= 1.6
    if meta > 10000:
        quick_print(meta)
        basic.sort_hat()
    basic.farmar("energia", meta)
    basic.farmar("trigo", meta)
    basic.farmar("madeira", meta)
    basic.farmar("cenoura", meta)
    basic.farmar("abobora", meta)
    basic.farmar("cacto", meta)
    basic.farmar("osso", meta)


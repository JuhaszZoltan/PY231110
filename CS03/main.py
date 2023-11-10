from module import *

hossz:int = 28
min:int = 0
max:int = 20

szamok:list[int] = get_rnd_list(hossz, min, max)
print_table_view(szamok)
pesz:int = get_even_count(szamok)
print(f'páros elemek száma: {pesz} db')
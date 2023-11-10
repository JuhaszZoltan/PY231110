from module import *

elemszam:int = 47
minimum:int = 0
maximum:int = 20

szamok:list[int] = get_rnd_list(elemszam, minimum, maximum)
print_table_view(szamok)
pesz:int = get_even_count(szamok)
print(f'páros elemek száma: {pesz} db')
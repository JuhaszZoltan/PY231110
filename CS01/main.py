from module import *

# írj egy függvényt, ami visszatér egy paraméterben megkapott elemszámú, egész számokatlistával,
# ami véletlenszerű elemekkel van feltöltve.
# A random generálás határértékeit szintén paraméterként adja át


hossz:int = 35
legkisebb:int = 0
legnagyobb:int = 20

lista:list[int] = get_random_list(hossz, legkisebb, legnagyobb)
print(f'páros elemek száma: {get_even_count(lista)} db')
print('a lista elemei:')
print_table_view(lista)
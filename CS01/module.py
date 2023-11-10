from random import randint

def get_random_list(length:int, min:int, max:int) -> list[int]:
    lst:list[int] = []
    for _ in range(length):
        lst.append(randint(min, max))
    return lst


def get_even_count(numbers:list[int]) -> int:
    count:int = 0
    for e in numbers:
        if e % 2 == 0: count += 1
    return count


def print_table_view(numbers:list[int]) -> None:
    for i in range(len(numbers)):
        print(f'{numbers[i]:2}', end=' ')
        if (i+1) % 10 == 0:
            print(end='\n')
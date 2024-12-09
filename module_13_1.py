import asyncio

N_STONES = 5  # количество шаров Атласа
DURATION_MAX = 3  #N_STONES + 1  # максимальное время выполнения упражнения (сек), для сокращения времени работы программы
TIME_COEFFICIENT = 1  # для сокращения времени работы программы установить 0 < TIME_COEFFICIENT < 1


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    # duration_exercise = (DURATION_MAX - power) * TIME_COEFFICIENT  # вариация зависимости duration_exercise от power
    duration_exercise = (DURATION_MAX / power) * TIME_COEFFICIENT
    for i in range(1, N_STONES + 1):
        await asyncio.sleep(duration_exercise)
        print(f'Силач {name} поднял {N_STONES - (N_STONES - i)} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Anton', 3))
    task2 = asyncio.create_task(start_strongman('Boris', 4))
    task3 = asyncio.create_task(start_strongman('Pyotr', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())

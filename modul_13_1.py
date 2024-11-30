import asyncio


async def start_strongman(name: str, power: int):
    if isinstance(name, str) and len(name) >= 1 and isinstance(power, int) and power >= 1:
        print(f'Силач {name} начал соревнование')
        for boll in range(5):
            await asyncio.sleep(round((1/power), 2))
            print(f'Силач {name} поднял шар {boll + 1}')
        print(f'Силач {name} закончил соревнование')
    else:
        return 'Введены некорректные данные'


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task1
    await task2
    await task3

asyncio.run(start_tournament())

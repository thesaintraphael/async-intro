import asyncio
import time

async def coro(seq) -> list:
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    t = asyncio.create_task(coro([1, 2, 3]))
    t2 = asyncio.create_task(coro([10, 5, 0]))
    print('Start:', time.strftime('%X'))
    for res in asyncio.as_completed((t, t2)):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')
    
    print("End:", time.strftime("%X"))
    print(f'Both are done: {all((t.done(), t2.done()))}')

    
    # await t
    # print(f't: type {type(t)}')  # <class '_asyncio.Task'>
    # print(f't done: {t.done()}')


a = asyncio.run(main())

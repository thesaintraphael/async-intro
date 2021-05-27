import asyncio


async def mygen(u : int = 10):
    """Yield powers of 2"""

    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)



async def main():
    # showing syntax only
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f


g, f = asyncio.run(main())
print("g:", g)
print("f:", f)

import asyncio


async def count(num):
    print(num)
    await asyncio.sleep(5)
    print(f'Square of {num} is {num**2}')


async def main():
    tasks = []

    for i in range(2, 11, 2):
        tasks.append(
            asyncio.create_task(
                count(i)
            )
        )

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
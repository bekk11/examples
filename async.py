import asyncio
import time

from datetime import datetime


async def print_nums():
    num = 0
    while True:
        print("Num: {} [{}]".format(num, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 1 == 0:
            print("{} seconds have passed[{}]".format(count, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())

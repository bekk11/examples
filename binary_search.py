import asyncio
from datetime import datetime


async def searchBinary(myList, item):
    first = 0
    last = len(myList) - 1
    foundFlag = False
    while first <= last and not foundFlag:
        mid = (first + last) // 2
        if myList[mid] == item:
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print("Binary {} [{}]".format(foundFlag, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))


async def searchLinear(myList, item):
    nat = False
    for i in myList:
        if i == item:
            nat = True
    print("Lienar {} [{}]".format(nat, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))


async def main():
    task2 = asyncio.create_task(searchLinear([8, 9, 10, 100, 1000, 2000, 3000], 9))
    task1 = asyncio.create_task(searchBinary([8, 9, 10, 100, 1000, 2000, 3000], 9))

    await asyncio.gather(task2, task1)


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
import time


async def output(text, sleep):
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{text} counter: {sleep} seconds')
        sleep -= 1


async def main():
    task_1 = asyncio.create_task(output('First', 1))
    task_2 = asyncio.create_task(output('Second', 2))
    task_3 = asyncio.create_task(output('Third', 3))
    print(f"Started: {time.strftime('%X')}")
    await task_1
    task_2
    task_3
    print(f"Ended: {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())

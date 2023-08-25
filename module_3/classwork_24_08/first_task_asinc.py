import asyncio
import requests

list_of_url = ["https://russianwarship.rip/api/v2/statistics/2022-04-14",
               "https://russianwarship.rip/api/v2/statistics?offset=0&limit=50&date_from=2022-02-24&date_to=2022-03-01",
               "https://russianwarship.rip/api/v2/statistics/latest"]

# async def request1():
#     url = "https://russianwarship.rip/api/v2/statistics/2022-04-14"
#     result = requests.get(url)
#     print(result)
#
#
# async def request2():
#     url = "https://russianwarship.rip/api/v2/statistics?offset=0&limit=50&date_from=2022-02-24&date_to=2022-03-01"
#     result = requests.get(url)
#     print(result.text)
#
#
# async def request3():
#     url = "https://russianwarship.rip/api/v2/statistics/latest"
#     result = requests.get(url)
#     print(result.text)


async def main_request():
    for i in list_of_url:
        print(requests.get(i).text)
        await asyncio.sleep(1)


async def main():
    # task1 = asyncio.create_task(request1())
    # task2 = asyncio.create_task(request2())
    # task3 = asyncio.create_task(request3())
    task_main = asyncio.create_task(main_request())
    await asyncio.gather(task_main)


asyncio.run(main())

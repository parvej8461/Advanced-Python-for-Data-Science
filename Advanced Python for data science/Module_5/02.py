import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = ['https://api.example.com/data1', 'https://api.example.com/data2']
    results = await asyncio.gather(*(fetch_data(url) for url in urls))
    return results

asyncio.run(main())

'''
Asynchronous API Calls
Use asyncio for fetching data from APIs.
'''
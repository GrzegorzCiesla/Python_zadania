import asyncio
import aiohttp
import time

async def pobierz_kurs(session, waluta):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    async with session.get(url) as resp:
        dane = await resp.json()
        return f"Kurs {waluta}: {dane['rates'][0]['mid']}"

async def main():
    waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']
    async with aiohttp.ClientSession() as session:
        zadania = [pobierz_kurs(session, waluta) for waluta in waluty]
        wyniki = await asyncio.gather(*zadania)
        for w in wyniki:
            print(w)

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print(f"Czas asyncio: {time.perf_counter() - start:.2f}s")
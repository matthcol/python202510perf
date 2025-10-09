import asyncio
import aiohttp # ou httpx 
import zstandard as zstd

doc_sources = {
    "python": "https://docs.python.org/3/library/concurrent.futures.html",
    "numpy": "https://numpy.org/doc/stable/reference/index.html",
    "pandas": "https://pandas.pydata.org/docs/reference/index.html",
    "dummy": "https://nourl.nourl",
    "requests": "https://pypi.org/project/requests/",
    "beautiful soup": "https://tedboy.github.io/bs4_doc",
    "scrapy": "https://docs.scrapy.org/en/latest/",
}

# NB: definition de coroutine
async def get_url_async(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url,
                     headers={'Accept-Encoding': 'gzip, deflate'},  
                ) as response:
                if response.status != 200:
                    print(f"Erreur {response.status} pour {url}")
                    return None
                
                return await response.text()
    except Exception as e:
        print(f"Erreur pour {url}: {e}")
        return None
    
async def run_get_urls(urls):
    results = await asyncio.gather(*[get_url_async(url) for url in urls])
    return results


results = asyncio.run(run_get_urls(doc_sources.values()))
print([ (r[:10] if r is not None else 'KO') for r in results ])
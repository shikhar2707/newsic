import os
import datetime
import asyncio
import aiohttp
import time

from newsapi import NewsApiClient
from concurrent.futures import ThreadPoolExecutor

import warnings
warnings.filterwarnings("ignore")





api_key = os.getenv('API_KEY','c18b4db5c23d4e5cbd40ea65392aad0e')






def get_curr_date():
    return datetime.datetime.now().date().strftime("%Y-%d-%m")







async def get(url, session):
    
    try:
        async with session.get(url) as response:
            resp = await response.read()
            return resp.decode('utf-8')
    except Exception as e:
        print(f"Cannot retreive the content for the following URL : {url} due to {e}")
        return " "
    
    
    
    
        
async def main(urls):
    
    session = aiohttp.ClientSession()
    ret = asyncio.gather(*(get(url, session) for url in urls))
    session.close()
    return ret







def refine_content(content):
    
    soup = BeautifulSoup(content, 'html.parser')
    
    cont = ''
    
    for cnt in soup.find_all('p'):
        cont  += str(cnt.text)
        
    return cont











async def retrieve_news(api_key=api_key, query = 'all'):
    
    newsapi = NewsApiClient(api_key=api_key)
    
    top_headlines = newsapi.get_everything(q=query,
                                          language='en',from_param=get_curr_date(),
                                          to=get_curr_date(),page_size=20)
    
    urls = [r.get('url') for r in top_headlines['articles']]
    
    try:
        resp = asyncio.run(main(urls))
        return resp
    except RuntimeError as e:
        
        resp = await asyncio.gather(main(urls))
        
    return resp










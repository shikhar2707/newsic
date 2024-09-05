import importlib

from utils import *
import argparse



async def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', dest='query', type=str, help='Search Object for NewsAPI')
    args = parser.parse_args()
    
    query = args.query
    
    result = await retrieve_news(api_key, query)
    
    contents = [await r.result() for r in result]
    all_ = [refine_content(cont) for cont in contents[0]]
    parsed_text = " ".join(all_)
    print(parsed_text)
    
    sum_ = summary(parsed_text)
    
    print(sum_)
    
    
if __name__ == '__main__':
    asyncio.run(main())
    
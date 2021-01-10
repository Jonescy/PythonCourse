"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/7
"""
import asyncio
import aiohttp
import re
import aiomysql
from lxml import etree

stopping = False

pending_urls = asyncio.Queue()
seen_urls = set()

sem = asyncio.Semaphore(1)


async def fetch(url, session):
    # 限制并发度
    async with sem:
        await asyncio.sleep(1)
        try:
            async with session.get(url) as resp:
                if resp.status in [200, 201, 302, 301]:
                    html = await resp.text()
                    return html
        except Exception as e:
            print(e)


def extract_urls(html):
    urls = []
    doc = etree.HTML(html)
    for link in doc.xpath('//a/@href'):
        if link and link.startswith('http') and link not in seen_urls:
            if re.match(r'https://www\.cnblogs\.com/.*/p/\d+\.html', link):
                urls.append(link)
                pending_urls.put_nowait(link)

    return urls


async def init_urls():
    async with aiohttp.ClientSession() as session:
        urls = [f'https://www.cnblogs.com/sitehome/p/{i}' for i in range(1, 2)]
        for url in urls:
            html = await fetch(url, session)
            extract_urls(html)


async def article_handler(url, session, pool):
    # 获取文章详情，并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    doc = etree.HTML(html)
    title = doc.xpath('//h1[@class="postTitle"]/a/span/text()')
    print(title)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into article(title) values('{}') ".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:

        while not stopping:
            if not pending_urls.empty():
                url = pending_urls.get_nowait()
                # print(f'start get:{url}')
                if url not in seen_urls:
                    loop.create_task(article_handler(url, session, pool))


async def main():
    # 等待mysql链接建立
    pool = await aiomysql.create_pool(host="localhost", port=3306,
                                      user='root', password='1997',
                                      db='aiomysql_test', loop=loop,
                                      use_unicode="utf-8", autocommit=True
                                      )

    loop.create_task(init_urls())
    loop.create_task(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()

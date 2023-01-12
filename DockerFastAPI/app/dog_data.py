import httpx


async def get_dog():
    
    url = f'https://random.dog/woof.json'

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()

        print(resp, resp.text)
        data = resp.json()
  
    dog = data
    return dog

    
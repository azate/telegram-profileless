from aiohttp import ClientSession


async def fetch_image_art_fake() -> bytes:
    async with ClientSession() as session:
        async with session.get(url='https://thisartworkdoesnotexist.com') as response:
            return await response.read()


async def fetch_image_cat_fake() -> bytes:
    async with ClientSession() as session:
        async with session.get(url='https://thiscatdoesnotexist.com') as response:
            return await response.read()


async def fetch_image_human_fake() -> bytes:
    async with ClientSession() as session:
        async with session.get(url='https://thispersondoesnotexist.com/image') as response:
            return await response.read()

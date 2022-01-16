import asyncio
import random
from aiohttp import ClientSession
from dataclasses import dataclass
from envargparse import EnvArgParser
from names import get_first_name, get_last_name
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest

PROVIDER_ART_FAKE = 'art-fake'
PROVIDER_CAT_FAKE = 'cat-fake'
PROVIDER_HUMAN_FAKE = 'human-fake'
PROVIDER_SPACE = 'space'
PROVIDER_RANDOM = 'random'


@dataclass
class Profile:
    image: bytes
    first_name: str
    last_name: str = None
    about: str = None


async def create_profile_art_fake() -> Profile:
    async with ClientSession() as session:
        async with session.get(url='https://thisartworkdoesnotexist.com') as response:
            image = await response.read()

    return Profile(
        image=image,
        first_name=get_first_name(),
        last_name=get_last_name(),
    )


async def create_profile_cat_fake() -> Profile:
    async with ClientSession() as session:
        async with session.get(url='https://thiscatdoesnotexist.com') as response:
            image = await response.read()

    return Profile(
        image=image,
        first_name=get_first_name(),
        last_name=get_last_name(),
    )


async def create_profile_human_fake() -> Profile:
    async with ClientSession() as session:
        async with session.get(url='https://thispersondoesnotexist.com/image') as response:
            image = await response.read()

    return Profile(
        image=image,
        first_name=get_first_name(),
        last_name=get_last_name(),
    )


async def create_profile_space() -> Profile:
    async with ClientSession() as session:
        async with session.get(url='https://source.unsplash.com/featured/?space') as response:
            image = await response.read()

    return Profile(
        image=image,
        first_name=get_first_name(),
        last_name=get_last_name(),
    )


async def create_profile(provider: str) -> Profile:
    if provider == PROVIDER_ART_FAKE:
        return await create_profile_art_fake()
    elif provider == PROVIDER_CAT_FAKE:
        return await create_profile_cat_fake()
    elif provider == PROVIDER_HUMAN_FAKE:
        return await create_profile_human_fake()
    elif provider == PROVIDER_SPACE:
        return await create_profile_space()
    elif provider == PROVIDER_RANDOM:
        return await create_profile(random.choice([
            PROVIDER_ART_FAKE,
            PROVIDER_CAT_FAKE,
            PROVIDER_HUMAN_FAKE,
            PROVIDER_SPACE,
        ]))
    else:
        raise ValueError('Not found provider: {provider}.'.format(provider=provider))


async def run(api_id: int, api_hash: str, api_session: str, provider: str, interval: int):
    while True:
        profile = await create_profile(provider=provider)

        await asyncio.sleep(interval)

        client = TelegramClient(
            api_id=api_id,
            api_hash=api_hash,
            session=StringSession(string=api_session),
        )

        async with client:
            request_delete_photos = DeletePhotosRequest(id=await client.get_profile_photos('me'))
            await client(request=request_delete_photos)

            request_upload_photo = UploadProfilePhotoRequest(file=await client.upload_file(file=profile.image))
            await client(request=request_upload_photo)

            request_update_profile = UpdateProfileRequest(
                first_name=profile.first_name,
                last_name=profile.last_name,
                about=profile.about,
            )
            await client(request=request_update_profile)


if __name__ == '__main__':
    parser = EnvArgParser()
    parser.add_argument('--api-id', env_var='TELEGRAM_PROFILELESS_API_ID', required=True, help='Telegram API ID', type=int)
    parser.add_argument('--api-hash', env_var='TELEGRAM_PROFILELESS_API_HASH', required=True, help='Telegram API hash', type=str)
    parser.add_argument('--api-session', env_var='TELEGRAM_PROFILELESS_API_SESSION', required=True, help='Telegram session', type=str)
    parser.add_argument('--provider', env_var='TELEGRAM_PROFILELESS_PROVIDER', required=True, help='Profile provider', type=str)
    parser.add_argument('--interval', env_var='TELEGRAM_PROFILELESS_INTERVAL', required=False, help='Profile update interval', type=int, default=10)

    args = parser.parse_args()

    asyncio.run(run(
        api_id=args.api_id,
        api_hash=args.api_hash,
        api_session=args.api_session,
        provider=args.provider,
        interval=args.interval,
    ))

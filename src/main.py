import asyncio
import sys

from envargparse import EnvArgParser
from names import get_first_name, get_last_name
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from thisapidoesnotexist import get_person
from datetime import datetime


class AmkearameEntity:
    def __init__(
            self: 'AmkearameEntity',
            first_name: str = None,
            last_name: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name


class Amkearame:
    def __init__(self: 'Amkearame', client: TelegramClient, entity: AmkearameEntity):
        self.client = client
        self.entity = entity

    async def delete_photos(self: 'Amkearame'):
        photos = await self.client.get_profile_photos('me')
        await self.client(DeletePhotosRequest(photos))

    async def upload_profile_fake_photo(self: 'Amkearame'):
        image = get_person().image
        file = await self.client.upload_file(image)
        await self.client(UploadProfilePhotoRequest(file))

    async def set_profile_fake_fullname(self: 'Amkearame'):
        first_name = get_first_name()
        last_name = get_first_name()
        await self.client(UpdateProfileRequest(first_name, last_name))
        self.entity.first_name = first_name
        self.entity.last_name = last_name


async def main():
    parser = EnvArgParser()
    parser.add_argument('--api-id', env_var='AMKEARAME_API_ID', required=True, help='user api id', type=int)
    parser.add_argument('--api-hash', env_var='AMKEARAME_API_HASH', required=True, help='user api hash', type=str)
    parser.add_argument('--delay', env_var='AMKEARAME_DELAY', required=False, help='delay update', type=int, default=60)

    args = parser.parse_args()

    while True:
        try:
            client = TelegramClient('telegram', args.api_id, args.api_hash)
            await client.connect()

            entity = AmkearameEntity()
            amkearame = Amkearame(client, entity)

            await amkearame.delete_photos()
            await amkearame.upload_profile_fake_photo()
            await amkearame.set_profile_fake_fullname()

            print('[+] {}: {} {}'.format(
                datetime.now().strftime('%x %X'),
                amkearame.entity.first_name,
                amkearame.entity.last_name
            ))

            await asyncio.sleep(args.delay)
        except Exception as e:
            print('[-] {}: {}'.format(datetime.now().strftime('%x %X'), e))
            continue


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit(0)

import asyncio
import sys

from envargparse import EnvArgParser
from names import get_first_name, get_last_name
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from thisapidoesnotexist import get_person


async def main():
    parser = EnvArgParser()
    parser.add_argument('--api-id', env_var='API_ID', required=True, help='user api id', type=str)
    parser.add_argument('--api-hash', env_var='API_HASH', required=True, help='user api hash', type=str)
    parser.add_argument('--timer', env_var='TIMER', required=False, help='timer update seconds', type=int, default=60)

    args = parser.parse_args()

    client = TelegramClient('telegram', args.api_id, args.api_hash)
    await client.connect()

    while True:
        image = get_person().image
        await client(DeletePhotosRequest(await client.get_profile_photos('me')))
        file = await client.upload_file(image)
        await client(UploadProfilePhotoRequest(file))

        await client(UpdateProfileRequest(get_first_name(), get_last_name()))

        await asyncio.sleep(args.timer)


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit(0)

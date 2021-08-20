from envargparse import EnvArgParser
from telethon import TelegramClient
from telethon.sessions import StringSession


def login(api_id: int, api_hash: str):
    with TelegramClient(api_id=api_id, api_hash=api_hash, session=StringSession()) as client:
        print(client.session.save())


if __name__ == '__main__':
    parser = EnvArgParser()
    parser.add_argument('--api-id', env_var='TELEGRAM_PROFILELESS_API_ID', required=True, type=int, help='Telegram API ID')
    parser.add_argument('--api-hash', env_var='TELEGRAM_PROFILELESS_API_HASH', required=True, type=str, help='Telegram API hash')

    args = parser.parse_args()

    login(args.api_id, args.api_hash)

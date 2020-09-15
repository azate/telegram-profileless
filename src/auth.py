from envargparse import EnvArgParser
from telethon import TelegramClient


def main():
    parser = EnvArgParser()
    parser.add_argument('--api-id', env_var='AMKEARAME_API_ID', required=True, help='user api id', type=str)
    parser.add_argument('--api-hash', env_var='AMKEARAME_API_HASH', required=True, help='user api hash', type=str)

    args = parser.parse_args()

    client = TelegramClient('telegram', args.api_id, args.api_hash)
    client.start()


if __name__ == '__main__':
    main()

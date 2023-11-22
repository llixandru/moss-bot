from lib.bot import bot
import asyncio
import nest_asyncio

nest_asyncio.apply()

VERSION = "1.0.0"

async def main():
    async with bot:
        await bot.run(VERSION)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
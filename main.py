from discord import DMChannel
from messages import Messages
from discord.ext import commands, tasks
from token import TOKEN
import datetime

bot = commands.Bot(command_prefix='>')
messages = Messages()


@tasks.loop(seconds=4)
async def message_loop():
    user = await bot.fetch_user('926029229102100480')
    now = datetime.datetime.now()
    if now.hour >= 7 and now.hour <= 22:
        if now.hour >= 7 and now.hour <= 10:
            await DMChannel.send(user, messages.get_morning())
        if now.hour >= 21 and now.hour < 24:
            await DMChannel.send(user, messages.get_night())
        else:
            await DMChannel.send(user, messages.get_day())


@message_loop.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting.")


message_loop.start()

bot.run(TOKEN)

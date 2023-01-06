import asyncio
from datetime import datetime, time, timedelta
from discord.ext import commands
from discord import DMChannel
from messages import Messages
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=">")

# Set up authorisation token and user id here
TOKEN = ''
USER_ID = ''

# Set up timezone here; use -timedelta() for -UTC(s)
UTC = +timedelta(hours=13)

# Set up the message times here
MORNING = time(8, 13, 0)  # 8:13 AM
DAY = time(13, 1, 0)  # 1:01 PM
NIGHT = time(21, 32, 0)  # 9:32 PM

messages = Messages()


async def send_morning(user):
    await bot.wait_until_ready()
    print('Bot is sending morning message.')
    await DMChannel.send(user, messages.get_morning())


async def send_day(user):
    await bot.wait_until_ready()
    print('Bot is sending day message.')
    await DMChannel.send(user, messages.get_day())


async def send_night(user):
    await bot.wait_until_ready()
    print('Bot is sending night message.')
    await DMChannel.send(user, messages.get_night())


async def wait_until(time):
    """Sleep until a specified time.

      Args:
          time (datetime.datetime): Time to sleep to.
      """
    now = datetime.utcnow() + UTC
    target_time = datetime.combine(now.date(), time)
    seconds_until_target = (target_time - now).total_seconds()
    await asyncio.sleep(seconds_until_target)


async def wait_until_tomorrow():
    now = datetime.utcnow() + UTC
    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    # Seconds until tomorrow (midnight)
    seconds = (tomorrow - now).total_seconds()
    # Sleep until tomorrow and then the loop will start a new iteration
    await asyncio.sleep(seconds)


async def background_task():
    now = datetime.utcnow() + UTC
    await bot.wait_until_ready()
    print("Bot is ready!")
    # Get the receiver's user class
    user = await bot.fetch_user(USER_ID)
    await send_day(user)

    while True:
        now = datetime.utcnow() + UTC
        if now.time() > NIGHT:
            await wait_until_tomorrow()
            await wait_until(MORNING)
            await send_morning(user)
        elif now.time() > DAY:
            await wait_until(NIGHT)
            await send_night(user)
        else:
            await wait_until(DAY)
            await send_day(user)


if __name__ == "__main__":
    # Ping for web server
    # keep_alive()
    bot.loop.create_task(background_task())
    bot.run(TOKEN)

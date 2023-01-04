import asyncio
from datetime import datetime, time, timedelta
from discord.ext import commands
from discord import DMChannel
from messages import Messages
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

# Set up your authorisation token and receiver's user ID here
TOKEN = ''
USER_ID = ''

MORNING = time(8, 0, 0)  # 8:00 AM
DAY = time(13, 0, 0)  # 1:00 PM
NIGHT = time(21, 30, 0)  # 9:00 PM

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
    now = datetime.utcnow() + timedelta(hours=13)
    target_time = datetime.combine(now.date(), time)
    seconds_until_target = (target_time - now).total_seconds()
    await asyncio.sleep(seconds_until_target)


async def wait_until_tomorrow():
    now = datetime.utcnow() + timedelta(hours=13)
    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    # Seconds until tomorrow (midnight)
    seconds = (tomorrow - now).total_seconds()
    # Sleep until tomorrow and then the loop will start a new iteration
    await asyncio.sleep(seconds)


async def background_task():
    now = datetime.utcnow() + timedelta(hours=13)
    await bot.wait_until_ready()
    print("Bot is ready!")
    # Get the receiver's user class
    user = await bot.fetch_user(USER_ID)
    # Make sure loop doesn't start after MORNING. Otherwise, it will immediately send the
    # first time as negative seconds which will make the sleep yield instantly
    if now.time() > MORNING:
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        # Seconds until tomorrow (midnight)
        seconds = (tomorrow - now).total_seconds()
        # Send the day message
        await send_day(user)
        # Sleep until tomorrow and then the loop will start
        await asyncio.sleep(seconds)
    while True:
        await wait_until(MORNING)
        await send_morning(user)
        await wait_until(DAY)
        await send_day(user)
        await wait_until(NIGHT)
        await send_night(user)

        wait_until_tomorrow()


if __name__ == "__main__":
    bot.loop.create_task(background_task())
    bot.run(TOKEN)

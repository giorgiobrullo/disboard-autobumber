import os
import asyncio
import logging
import colorlog
from discord.ext.commands import Bot
from random import randint
from dotenv import load_dotenv

# Load environment variables from a .env file if using one
load_dotenv()

# Set up custom log level colors
log_colors = {
    'DEBUG': 'cyan',
    'INFO': 'blue',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# Define the log formatter with precise color settings for each part
log_formatter = colorlog.ColoredFormatter(
    # Gray for the timestamp, color for log level, purple for logger name, white for message
    "\033[90m%(asctime)s\033[0m "
    "%(log_color)s%(levelname)-8s\033[0m "
    "\033[35m%(name)-20s\033[0m %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors=log_colors,
    secondary_log_colors={},
    style='%'
)

# Create a handler for console output
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

# Get the root logger and set the logging level
logger = logging.getLogger('discord.client')  # using 'discord.client' to match the logger name style
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

# Retrieve the token and log channel from environment variables to string
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL = os.getenv("LOG_CHANNEL_ID")
CHANNEL_IDS = [int(id) for id in os.getenv("CHANNEL_IDS", "").split(",") if id]

# Exit if token or channel IDs are not provided
if not TOKEN or not CHANNEL_IDS:
    logger.error("Token or channel IDs not provided. Exiting.")
    exit()
else:
    logger.info("Running bot with token " + TOKEN)

bot = Bot(command_prefix="?", self_bot=True, chunk_guilds_at_startup=False)

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
    bot.loop.create_task(auto())

async def auto():
    while True:
        for channel_id in CHANNEL_IDS:
            if channel := bot.get_channel(channel_id):
                if LOG_CHANNEL:
                    log_channel = bot.get_channel(LOG_CHANNEL)
                    logger.info(f"Sent bump command to channel {channel_id} in guild {channel.guild}.")
                    await log_channel.send(f"```Sent bump command!\nChannel ID: {channel_id}\nGuild: {channel.guild}```")
                await bump(channel)
                await asyncio.sleep(randint(20, 30))  # wait after each message
        await asyncio.sleep(randint(7200, 7220))  # wait after each round of messages

async def bump(channel):
    application_commands = await channel.application_commands()
    for command in application_commands:
        if command.name == "bump" and command.application_id == 302050872383242240:
            await command(channel)
            await asyncio.sleep(5)



bot.run(TOKEN)

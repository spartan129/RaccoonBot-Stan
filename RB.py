# Import required libraries
import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import json
import random
from google_images_search import GoogleImagesSearch

# Load environment variables from .env file
load_dotenv()

# Get environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')

# Set up intents for the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Create bot instance and set up slash commands
bot = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

# Set up Google Images Search
gis = GoogleImagesSearch(API_KEY, GOOGLE_CSE_ID)

# Handle command errors
@bot.event
async def on_command_error(ctx, error):
    print(f'Error: {error}')
    await ctx.send(f'Error: {error}')

# Print a message when the bot connects to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Create a slash command for sending raccoon images, gifs, or memes
@slash.slash(
    name='raccoon',
    description='Sends a random raccoon image, gif or meme',
    options=[
        create_option(
            name='type',
            description='Choose the type of raccoon content',
            option_type=3,
            required=False,
            choices=[
                create_choice(name='image', value='image'),
                create_choice(name='gif', value='gif'),
                create_choice(name='meme', value='meme')
            ]
        )
    ]
)
# Define the raccoon command
async def raccoon(ctx, type='image'):
    # Defer the response to let the user know the bot is processing the request
    await ctx.defer()

    # Print a message to the console to indicate the bot is sending a raccoon item
    print(f'{bot.user.name} is sending a raccoon {type}...')

    # Search for raccoon content using Google Images Search
    query = f'raccoon {type}'
    gis.search({'q': query, 'num': 20})

    # Send a random raccoon image, gif, or meme to the user
    if gis.results():
        image_url = random.choice(gis.results()).url
        await ctx.send(content=image_url)
    else:
        await ctx.send(f"Failed to get raccoon {type} :(")

# Run the bot with the provided token
bot.run(TOKEN)

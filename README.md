# RaccoonBot-Stan
This is a 95% AI made python discord bot that can search google for images, gifs, or memes of raccons. This can be used and easily replaced with any similar kind of bot. 

# Raccoon Bot README

This is a simple Discord bot that sends random raccoon images, gifs, or memes using the `/raccoon` slash command. The bot uses the Discord.py library, Discord Slash Commands, and Google Images Search API.

## Requirements

- Python 3.6 or higher
- discord.py library
- discord-py-slash-command library
- python-dotenv library
- google-images-search library

You can install the required libraries using pip:

```bash
pip install discord.py
pip install discord-py-slash-command
pip install python-dotenv
pip install google-images-search
```

## Setup

### Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in with your Discord account.
2. Click on the "New Application" button in the top-right corner.
3. Enter a name for your application and click "Create".
4. In the application's settings, click on the "Bot" tab in the left sidebar, then click "Add Bot" and confirm.
5. Under the "Token" section, click on "Copy" to copy your bot's token. This will be used in the `.env` file.

### Google Cloud Project and Custom Search Engine

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and sign in with your Google account.
2. Click on the project dropdown and select or create the project you want to use for the bot.
3. Enable the [Custom Search JSON API](https://developers.google.com/custom-search/v1/introduction) for your project.
4. Go to the [APIs & Services > Credentials](https://console.cloud.google.com/apis/credentials) page and click "Create credentials" > "API key" to create an API key. Copy the API key, as it will be used in the `.env` file.
5. Visit the [Custom Search Engine](https://programmablesearchengine.google.com/about/) page and click "Get Started".
6. Click on "New Search Engine" and enter the following details:
   - Sites to search: `*.google.com`
   - Language: Choose your preferred language.
   - Name: Enter a name for your search engine.
7. Click "Create" to create the search engine.
8. Edit the search engine settings and enable "Image search" under the "Sites to search" section.
9. Copy the Search Engine ID (cx) from the "Details" section. This will be used in the `.env` file.

### .env File

Create a `.env` file in the same directory as the bot script with the following format:

```
DISCORD_TOKEN=your_discord_bot_token
DISCORD_GUILD=your_discord_guild_name
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
```

Replace the placeholders with your actual Discord bot token, Discord guild (server) name, Google API key, and Google Custom Search Engine ID.

## Running the Bot

To run the bot, simply execute the Python script:

```bash
python raccoon_bot.py
```

### Inviting the Bot to Your Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your application.
2. In the application's settings, click on the "OAuth2" tab in the left sidebar.
3. Under the "Scopes" section, select the "bot" and "applications.commands" checkboxes.
4. Copy the generated URL and open it in a new browser tab.
5. Choose the server you want to invite the bot to and authorize the bot's permissions.

Once the bot is connected, you can use the `/raccoon` slash command to get random raccoon images, gifs, or memes.

## Usage

To use the raccoon command, type `/raccoon` followed by an optional type parameter:

- `/raccoon`: Sends a random raccoon image.
- `/raccoon type:image`: Sends a random raccoon image.
- `/raccoon type:gif`: Sends a random raccoon gif.
- `/raccoon type:meme`: Sends a random raccoon meme.

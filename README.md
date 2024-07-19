# OnlyDmBot

OnlyDmBot is a simple Discord bot that demonstrates how to create a slash command that only works in direct messages (DMs).

## Features

- `/secret`: Share a secret message in a DM.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/OnlyDmBot.git
    cd OnlyDmBot
    ```

2. Create a `settings.json` file in the root directory with your bot token:
    ```json
    {
        "token": "YOUR_DISCORD_BOT_TOKEN"
    }
    ```

3. Run the bot:
    ```bash
    python bot.py
    ```

## Usage

- Invite the bot to your server.
- Send a direct message to the bot with the `/secret` command followed by your secret message.
- The bot will reply with your secret message.

## Note

While there are methods to enforce commands to work only in DMs, most of them are quite complicated. This bot uses a straightforward approach to check if the command is used in a DM and responds accordingly.

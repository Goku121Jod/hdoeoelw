import discord
import json

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]
TRIGGER_MESSAGE = config["trigger_message"]
REPLY_MESSAGE = config["reply_message"]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Important to read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore own messages

    if message.content.lower() == TRIGGER_MESSAGE.lower():
        await message.channel.send(REPLY_MESSAGE)

client.run(TOKEN)

import discord
import json

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]
TRIGGER_MESSAGE = config["trigger_message"]
EMBED_TITLE = config["embed_title"]
EMBED_BALANCE = config["embed_balance"]
EMBED_FOOTER = config["embed_footer"]
THUMBNAIL_URL = config["embed_thumbnail_url"]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.strip().lower() == TRIGGER_MESSAGE.lower():
        embed = discord.Embed(title=EMBED_TITLE, color=0x2f3136)
        embed.add_field(name="Balance", value=f"🪙 {EMBED_BALANCE}", inline=False)
        embed.set_footer(text=EMBED_FOOTER)
        embed.set_thumbnail(url=THUMBNAIL_URL)
        await message.channel.send(embed=embed)

client.run(TOKEN)

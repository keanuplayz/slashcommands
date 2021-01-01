import discord
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, auto_register=True)

guild_ids = [644875385452101633]  # Put your testing server ID.


@client.event
async def on_ready():
    print("Ready!")
    print(f"Logged in as {client.user.name} ({client.user.id})")


@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(content=f"Pong! ({client.latency*1000}ms)")


@slash.slash(
    name="echo",
    guild_ids=guild_ids,
    options=[
        manage_commands.create_option("string", "A random piece of text.", 3, True)
    ],
)
async def _echo(ctx, string):
    await ctx.send(content=string)


@slash.slash(
    name="mention",
    guild_ids=guild_ids,
    options=[manage_commands.create_option("user", "A user to ping", 6, True)],
)
async def _mention(ctx, user):
    await ctx.send(content=user.mention)


client.run(os.getenv("TOKEN"))

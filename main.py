import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="s!", intents=discord.Intents.all())

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

slash = SlashCommand(client, auto_register=True, auto_delete=True)

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


@slash.slash(
    name="calc",
    guild_ids=guild_ids,
    options=[
        manage_commands.create_option("digit", "number to add", 4, True),
        manage_commands.create_option("digit2", "another number", 4, True),
    ],
)
async def _calc(ctx, number1, number2):
    result = number1 + number2
    await ctx.send(content=result)


@slash.slash(
    name="embed",
    guild_ids=guild_ids,
    options=[
        manage_commands.create_option("title", "Embed title to set.", 3, True),
        manage_commands.create_option(
            "description", "Embed description to set.", 3, True
        ),
        manage_commands.create_option("footer", "Embed footer to set.", 3, True),
        manage_commands.create_option("author", "Embed header to set.", 3, True),
        manage_commands.create_option("thumbnail", "Embed thumbnail to set.", 3, False),
        manage_commands.create_option("image", "Embed image to set.", 3, False),
    ],
)
async def _embed(ctx, title, desc, footer, author, thumbnail=None, image=None):
    embed = discord.Embed(title=str(title), description=str(desc))
    embed.set_author(name=str(author))
    embed.set_footer(text=str(footer))
    embed.set_thumbnail(url=str(thumbnail))
    embed.set_image(url=str(image))
    await ctx.send(embeds=[embed])


@slash.slash(
    name="hide",
    guild_ids=guild_ids,
    options=[
        manage_commands.create_option("string", "A random piece of text.", 3, True)
    ],
)
async def _hide(ctx, string):
    await ctx.send(content=string, hidden=True)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            f"This command does not exist. Use `{client.command_prefix}help` to view all available commands."
        )


@client.command()
async def test(ctx):
    await ctx.send("heuue")


client.run(os.getenv("TOKEN"))

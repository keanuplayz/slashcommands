import discord
from discord.ext import commands


class Experimental(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def edned(self, cxt, arg):
        if arg == "1":
            homo = discord.Embed(
                title="AAAAAAAAAAAAAAA",
                type="rich",
                description="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            )
            homo.set_image(
                url="https://www.westlanders.nu/Content/Uploads/Nieuws%202017/Evenementen/DrPhil-1280x720px-Shareimage.jpg"
            )
            await cxt.send(embed=homo)
        if arg == "2":
            dieke = discord.Embed(
                title="AAAAAAAA",
                type="rich",
                description="heuj",
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            )
            await cxt.send(embed=dieke)


def setup(client):
    client.add_cog(Experimental(client))

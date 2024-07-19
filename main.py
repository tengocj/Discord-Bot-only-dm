import discord
from discord.ext import commands
import json

class OnlyDmBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="secret", description="Share a secret message")
    async def secret(self, ctx: commands.Context, message: str):
        if not isinstance(ctx.channel, discord.channel.PartialMessageable):
            await ctx.respond("This command can only be used in direct messages.", ephemeral=True)
            return
        await ctx.send(f"Your secret message is: {message}")

# Load settings from settings.json
with open('settings.json') as f:
    settings = json.load(f)
    TOKEN = settings['token']

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)


bot.add_cog(OnlyDmBot(bot))

bot.run(TOKEN)

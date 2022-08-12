from discord.ext import commands

class three(commands.Cog, name = "3"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot: commands.Bot):
    bot.add_cog(three(bot))
from discord.ext import commands

class two(commands.Cog, name = "3"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot: commands.Bot):
    # INTENTIONAL ERROR I SWEAR
    bot.add_cog(tw(bot))
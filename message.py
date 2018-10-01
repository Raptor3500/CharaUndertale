import discord

class message():
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(message(bot))

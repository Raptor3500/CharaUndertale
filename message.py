import discord

class message():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if 'Hi' or 'hi' in message.content:
            await self.bot.send_message(message.channel, "Hi")



def setup(bot):
    bot.add_cog(message(bot))

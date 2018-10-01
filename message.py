import discord

class message():
    def __init__(self, bot):
        self.bot = bot
        
    async def on_message(self, message):
        if 'hi chara' or 'Hi chara' or 'hi Chara' or 'Hi Chara' or 'hello chara' or 'Hello chara' or 'Hello Chara' or 'hello Chara' in message.content:
           await self.bot.send_message(message.channel, "Hello")



def setup(bot):
    bot.add_cog(message(bot))

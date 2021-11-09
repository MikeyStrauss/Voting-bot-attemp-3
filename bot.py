import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix = '!V')
 
@bot.event
async def on_ready():
    print ("I fucking coded this on my own from a yt video. I am hackerman")
 
async def react(message):
    custom_emojis = [
    "<:upvote:907451207302385664>",                                      # emoji ids need the quotations ie. "" keep them                                          
    "<:downvote:907451206769725471>",
    "<:emoji:id>"
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
        print(emoji, guild_emoji_names)                # debugging your shite remove the "#" if you wanna see print in cmd console
        #print(emoji in guild_emoji_names)
        if emoji in guild_emoji_names:
            await message.add_reaction(emoji)
 
@bot.event                                             
async def on_message(message):
    if message.channel.id == 907451886125342780:                
            await react(message)                        # channelid and authorid do not need quotations ie. "" remove them
 
bot.run("OTA3NDUzNDc0OTkwNTk2MTk5.YYnZ6A.feC_dC6S24I8DjyyDFEshti9mUM")

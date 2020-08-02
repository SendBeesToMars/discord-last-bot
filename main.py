from discord.ext import commands
import discord
import os

TOKEN = os.environ.get('DOOTDOOT_TOKEN')
FLAG = False

bot = commands.Bot(command_prefix="thisisnotrequired:)")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_voice_state_update(member: discord.Member, before, after): 
    global FLAG
    
    general_channel = None
    # gets channel
    for i in bot.get_all_channels():
        if i.name == "gen":
            general_channel = i
        
    if after.channel != None and len(after.channel.members) >= 1 and FLAG == False:
        FLAG = True
        print(f"Flag set: {FLAG}")
    if after.channel == None and FLAG == True:
        if len(before.channel.members) == 0:
            print(member.name)  
            FLAG = False
            await general_channel.send("I am responding to your message")  

if __name__ == "__main__":
    bot.run(TOKEN)
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
    
    role = None
    general_channel = None
    
    # gets role
    for i in member.guild.roles:
        if i.name == "the last":
            role = i
            print(i.members)
    
    # gets channel
    for i in bot.get_all_channels():
        if i.name == "gen":
            general_channel = i
        
    # sets flag if people in channel equates greater than set ammount
    if after.channel != None and len(after.channel.members) >= 1 and FLAG == False:
        FLAG = True
        print(f"Flag set: {FLAG}")
        
    # if last to leave
    if after.channel == None and FLAG == True:
        if len(before.channel.members) == 0:
            print(member.name)  
            FLAG = False
            await general_channel.send(f"<@{member.id}> youre last :P")
            # removes role from everyone 
            for m in member.guild.members:
                try:
                    await m.remove_roles(role)
                except:
                    print("Couldnt remove role")
            # sets role to last to leave
            await bot.set_roles(member, role)
                

if __name__ == "__main__":
    bot.run(TOKEN)
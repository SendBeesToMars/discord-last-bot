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
    
    # gets role
    role =              discord.utils.get(member.guild.roles, name="the last")
    
    # gets channel
    general_channel =   discord.utils.get(bot.get_all_channels(), name="gen")
        
    # sets flag if people in channel equates greater than set ammount
    if after.channel != None and len(after.channel.members) >= 3 and FLAG == False:
        FLAG = True
        print(f"Flag set: {FLAG}")
        
    # if last to leave
    if after.channel == None and FLAG == True:
        if len(before.channel.members) == 0:
            print(member.name)  
            FLAG = False
            await general_channel.send(f"<@{member.id}> hehe")
            # removes role from everyone 
            for member in role.members:
                await member.remove_roles(role)
            # sets role to last to leave
            await member.add_roles(role)
                

if __name__ == "__main__":
    bot.run(TOKEN)
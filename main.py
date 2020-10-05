from discord.ext import commands
import discord
import os
import time

TOKEN = os.environ.get('DOOTDOOT_TOKEN')
FLAG = False

bot = commands.Bot(command_prefix="thisisnotrequired:)")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
    """ sets role to last person to leave voice channel.
        Removes role from previous role holders. 
        Sends a message in chat, with last person tagged """
    global FLAG
    
    FLAG_PLYER_NUM = 3
    
    # gets role
    role =              discord.utils.get(member.guild.roles, name="test role")
    
    # gets channel
    general_channel =   discord.utils.get(bot.get_all_channels(), name="bot")
        
    # sets flag if people in channel equates greater than set ammount
    if after.channel != None and len(after.channel.members) >= FLAG_PLYER_NUM and FLAG == False:
        flag_timer = time.time() # time object
        FLAG = True
        print(f"Flag set: {FLAG}")
        
    # @'s a person if he joins and leaves the vc too quickly
    if after.channel != None and len(after.channel.members) >= FLAG_PLYER_NUM-1 and FLAG == True:
        if time.time() - flag_timer <= 5:
            FLAG = False
            print(member.name)
            await general_channel.send(f"<@{member.id}> suh")
            # removes role from everyone 
            for i in role.members:
                await i.remove_roles(role)
            # sets role to last to leave
            await member.add_roles(role)            
        
    # if last to leave
    if after.channel == None and FLAG == True:
        if len(before.channel.members) == 0:
            print(member.name)  
            FLAG = False
            await general_channel.send(f"<@{member.id}> suh")
            # removes role from everyone 
            for i in role.members:
                await i.remove_roles(role)
            # sets role to last to leave
            await member.add_roles(role)
                

if __name__ == "__main__":
    bot.run(TOKEN)
    
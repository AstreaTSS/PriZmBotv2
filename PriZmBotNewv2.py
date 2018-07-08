# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py was used for basic blueprints for the rest of this project
# Uses discord.py
# Remember to change the token to the working one and back to 'Nope' before you send anything to Github.

import discord
from discord.ext import commands
import datetime
import asyncio
import time
import random

TOKEN = 'NOPE'

#client = discord.Client()

description = '''A bot for the use of PriZm, a Splatoon 2 clan.'''

bot = commands.Bot(command_prefix='!', description=description)

a = datetime.datetime.today().weekday()

counter = 0
quadice = 0
pbpractice = 0
stop = 0
sn1 = str(1)
sn2 = str(1)
sn3 = str(1)
sn4 = str(1)

def randompass():
    global sn1
    global sn2
    global sn3
    global sn4
    
    n1 = random.randint(1, 8)
    if n1 >=5:
        n1 = n1 + 1
    n2 = random.randint(1, 8)
    if n2 >=5:
        n2 = n2 + 1
    n3 = random.randint(1, 8)
    if n3 >=5:
        n3 = n3 + 1
    n4 = random.randint(1, 8)
    if n4 >=5:
        n4 = n4 + 1
    sn1 = str(n1)
    sn2 = str(n2)
    sn3 = str(n3)
    sn4 = str(n4)
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    global counter
    global a
    global quadice
    global pbpractice
    global stop
    
    global sn1
    global sn2
    global sn3
    global sn4
    
    user = message.author
    lieut = discord.utils.get(user.server.roles, name="Lieutenant")
    cocap = discord.utils.get(user.server.roles, name="Co-Captain")
    cap = discord.utils.get(user.server.roles, name="Captain")
    clancap = discord.utils.get(user.server.roles, name="Clan Captain")
    
    channel2 = bot.get_channel("457939628209602560")
    infanc = bot.get_channel("462286782080483350")
    alpanc = bot.get_channel("465547475839746058")
    msg3 = ('Hello <@&457299107371941888>! Practice starts now!')
    msg5 = ('Hello <@&457299107371941888>! Practice starts now! The list will be put out depending on who reacted to the previous message.')
    
    #if message.author == client.user:
       #return
        
    if message.content.startswith("!run"):
        counter = counter + 1
        if counter <= 1:
            await bot.send_message(message.channel, "Bot running in background!")
            while True:
                a = datetime.datetime.today().weekday()
                times = time.strftime('%H:%M')
                
                if stop <= 0:
                # this first one is meant for testing. delete before final release
                    #if times == '13:06':
                        #pbpractice = 1
                        
                # actual practices
                    if times == '14:30':  #2:30 PM
                        if a == 6:
                            quadice = 1
                            
                    if times == '15:00':  #3 PM
                        if a == 6:
                            await bot.send_message(channel2, msg5)
                            
                    if times == '17:30':  #5:30 PM
                        if a == 4:
                            quadice = 1
                            
                    if times == '18:00':  #6 PM
                        if a == 4:
                            await bot.send_message(channel2, msg5)
                            
                    if times == '18:30':  #6:30 PM
                        if a == 6:
                            pbpractice = 1
                            
                    if times == '19:00':  #7 PM
                        if a == 6:
                            await bot.send_message(channel2, msg3)
                        if a == 1:
                            pbpractice = 1
                        elif a == 2:
                            quadice = 1
                        elif a == 3:
                            pbpractice = 1
                        elif a == 5:
                            pbpractice = 1
                            
                    if times == '19:30':  #7:30 PM
                        if a == 1:
                            await bot.send_message(channel2, msg3)
                        elif a == 2:
                            await bot.send_message(channel2, msg5)
                        elif a == 3:
                            await bot.send_message(channel2, msg3)
                        elif a == 5:
                            await bot.send_message(channel2, msg3)
                        
                    await asyncio.sleep(1)
                    
                    if quadice == 1:
                        randompass()
                        msg4 = ('Hi <@&457299107371941888>! Practice starts in 30 minutes and will be a Squad, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        await bot.send_message(channel2, msg4)
                        quadice = 0
                        stop = 1
                    
                    if pbpractice == 1:
                        randompass()
                        msg2 = ('Hello <@&457299107371941888>! Practice starts in 30 minutes and will be a Private Battle. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        await bot.send_message(channel2, msg2)
                        pbpractice = 0
                        stop = 1
                        
                elif stop == 1:
                    await asyncio.sleep(60)
                    
        else:
            await bot.send_message(message.channel, 'Bot already started!')
    
    if message.content.startswith('!pb'):
        pbpractice = 1
    
    if message.content.startswith('!squad'):
        quadice = 1
        
    if message.content.startswith('!pbstart'):
        await bot.send_message(channel2, msg3)
    
    if message.content.startswith('!squadstart'):
        await bot.send_message(channel2, msg5)
        
    if message.content.startswith('!omepassed'):
        allowed = false
        user = message.author
        roles = user.roles
        
        if clancap in roles:
            allowed = true
        elif cap in roles:
            allowed = true
        elif cocap in roles:
            allowed = true
        elif lieut in roles:
            allowed = true
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Omega")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Omega!").format(message)
            await bot.send_message(channel2, welbome)
        
            curname = str(message.mentions[0].display_name)
            begin = 'pZ'
            omechara = "\u25B3"
            supbegin = begin + omechara
            
            if curname.startswith("pZ△"):
                newnick = curname
            elif curname.startswith("pZ▲"):
                newnick = curname.replace("pZ▲", supbegin)
            elif curname.startswith("pZ∴"):
                newnick = curname.replace("pZ∴", supbegin)
            elif curname.startswith("pZ◆"):
                newnick = curname.replace("pZ◆", supbegin)
            else:
                newnick = begin + omechara + curname
                
            await bot.change_nickname(message.mentions[0], newnick)
            
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
            
    if message.content.startswith('!infpassed'):
        allowed = false
        user = message.author
        roles = user.roles
        
        if clancap in roles:
            allowed = true
        elif cap in roles:
            allowed = true
        elif cocap in roles:
            allowed = true
        elif lieut in roles:
            allowed = true
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Infinite")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Infinite!").format(message)
            await bot.send_message(infanc, welbome)
        
            curname = str(message.mentions[0].display_name)
            begin = 'pZ'
            infchara = "\u25B2"
            supbegin = begin + infchara
            
            if curname.startswith("pZ△"):
                newnick = curname.replace("pZ△", supbegin)
            elif curname.startswith("pZ▲"):
                newnick = curname
            elif curname.startswith("pZ∴"):
                newnick = curname.replace("pZ∴", supbegin)
            elif curname.startswith("pZ◆"):
                newnick = curname.replace("pZ◆", supbegin)
            else:
                newnick = begin + infchara + curname
                
            await bot.change_nickname(message.mentions[0], newnick)
            
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
            

    if message.content.startswith('!alppassed'):
        allowed = false
        user = message.author
        roles = user.roles
        
        if clancap in roles:
            allowed = true
        elif cap in roles:
            allowed = true
        elif cocap in roles:
            allowed = true
        elif lieut in roles:
            allowed = true
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Alpha")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Alpha!").format(message)
            await bot.send_message(alpanc, welbome)
        
            curname = str(message.mentions[0].display_name)
            begin = 'pZ'
            alpchara = "\u2234"
            supbegin = begin + alpchara
            
            if curname.startswith("pZ△"):
                newnick = curname.replace("pZ△", supbegin)
            elif curname.startswith("pZ▲"):
                newnick = curname.replace("pZ▲", supbegin)
            elif curname.startswith("pZ∴"):
                newnick = curname
            elif curname.startswith("pZ◆"):
                newnick = curname.replace("pZ◆", supbegin)
            else:
                newnick = begin + alpchara + curname
                
            await bot.change_nickname(message.mentions[0], newnick)
            
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
        
    
    if message.content.startswith('!captain'):
        allowed = false
        user = message.author
        roles = user.roles
        
        if clancap in roles:
            allowed = true
        elif cap in roles:
            allowed = true
        elif cocap in roles:
            allowed = true
        elif lieut in roles:
            allowed = true
            
            
        if allowed:
            curname = str(message.mentions[0].display_name)
            begin = 'pZ'
            capchara = "\u25C6"
            supbegin = begin + capchara
            
            if curname.startswith("pZ△"):
                newnick = curname.replace("pZ△", supbegin)
                await bot.send_message(message.channel, "Name changed.")
            elif curname.startswith("pZ▲"):
                newnick = curname.replace("pZ▲", supbegin)
                await bot.send_message(message.channel, "Name changed.")
            elif curname.startswith("pZ∴"):
                newnick = curname.replace("pZ∴", supbegin)
                await bot.send_message(message.channel, "Name changed.")
            elif curname.startswith("pZ◆"):
                newnick = curname
                await bot.send_message(message.channel, "You're already a captain!")
            else:
                newnick = begin + capchara + curname
                await bot.send_message(message.channel, "Name changed.")
                
            await bot.change_nickname(message.mentions[0], newnick)
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
        
        
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
        
    if message.content.startswith("Hi"):
        if message.author.id == '461701686235234334':
            pong = "🏓"
            await bot.add_reaction(message, pong)
    
    if message.content.startswith("Let's"):
        if message.author.id == '461701686235234334':
            clap = "👏"
            await bot.add_reaction(message, clap)
    
    #await bot.process_commands(message)
        
bot.run(TOKEN)

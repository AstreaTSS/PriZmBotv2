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
practice = 0
stop = 0

clancap = None
cap = None
cocap = None
lieut = None
admin = None

curname = None
newnick = None

sn1 = str(1)
sn2 = str(1)
sn3 = str(1)
sn4 = str(1)

roles = [4, 5, 6]
allowed = False

def nickchange(symbol):
    global curname
    global newnick
    
    begin = 'pZ'
    supbegin = begin + symbol
    
    if curname.startswith(supbegin):
        newnick = curname
    if curname.startswith("pZ△"):
        newnick = curname.replace("pZ△", supbegin)
    elif curname.startswith("pZ▲"):
        newnick = curname.replace("pZ▲", supbegin)
    elif curname.startswith("pZ∴"):
        newnick = curname.replace("pZ∴", supbegin)
    elif curname.startswith("pZ◆"):
        newnick = curname.replace("pZ◆", supbegin)
    else:
        newnick = begin + symbol + curname
    
def permissions(autrid):
    global roles
    global allowed
    global clancap
    global cap
    global cocap
    global lieut
    global admin
    
    if clancap in roles:
            allowed = True
    elif cap in roles:
            allowed = True
    elif cocap in roles:
            allowed = True
    elif lieut in roles:
            allowed = True
    elif admin in roles:
            allowed = True
    elif autrid == '229350299909881876':
            allowed = True
            
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
    global practice
    global stop
    
    global roles
    global allowed
    
    global clancap
    global cap
    global cocap
    global lieut
    global admin
    
    global curname
    global newnick
    
    global sn1
    global sn2
    global sn3
    global sn4
    
    user = message.author
    lieut = discord.utils.get(user.server.roles, name="Lieutenant")
    cocap = discord.utils.get(user.server.roles, name="Co-Captain")
    cap = discord.utils.get(user.server.roles, name="Captain")
    clancap = discord.utils.get(user.server.roles, name="Clan Captain")
    admin = discord.utils.get(user.server.roles, name="Admin")
    
    omemention = discord.utils.get(user.server.roles, name="Omega").mention
    channel2 = bot.get_channel("457939628209602560")
    infanc = bot.get_channel("462286782080483350")
    alpanc = bot.get_channel("465547475839746058")
    msg3 = ('Hello ' + omemention +'! Practice starts now!')
    msg5 = ('Hello <@&457299107371941888>! Practice starts now! The list will be put out depending on who reacted to the previous message.')
    
    canceled = False
        
    if message.content.startswith("!run"):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            counter = counter + 1
            if counter <= 1:
                await bot.send_message(message.channel, "Bot running in background!")
                while True:
                    a = datetime.datetime.today().weekday()
                    times = time.strftime('%H:%M')
                    
                    if stop <= 0:
                            
                    # actual practices
                        if times == '14:30':  #2:30 PM
                            if canceled:
                                practice = 1
                            else:
                                if a == 6:
                                    quadice = 1
                                    practice = 1
                                
                        if times == '15:00':  #3 PM
                            if canceled:
                                practice = 1
                            else:
                                if a == 6:
                                    # await bot.send_message(channel2, msg5)
                                    await bot.send_message(channel2, msg3)
                                
                        if times == '18:30':  #6:30 PM
                            if canceled:
                                practice = 1
                            else:
                                if a == 6:
                                    pbpractice = 1
                                    practice = 1
                                elif a == 5:
                                    practice = 1
                                
                        if times == '19:00':  #7 PM
                            if canceled:
                                practice = 1
                            else:
                                if a == 6:
                                    await bot.send_message(channel2, msg3)
                                elif a == 2:
                                    quadice = 1
                                    practice = 1
                                elif a == 3:
                                    pbpractice = 1
                                    practice = 1
                                elif a == 4:
                                    practice = 1
                                elif a == 5:
                                    await bot.send_message(channel2, msg3)
                                
                        if times == '19:30':  #7:30 PM
                            if canceled:
                                practice = 1
                            else:
                                if a == 2:
                                    #await bot.send_message(channel2, msg5)
                                    await bot.send_message(channel2, msg3)
                                elif a == 3:
                                    await bot.send_message(channel2, msg3)
                                elif a == 4:
                                    await bot.send_message(channel2, msg3)
                            
                        await asyncio.sleep(1)
                        
                        if practice == 1:
                            if canceled:
                                practice = 0
                                stop = 1
                            else:
                                randompass()
                                msg4 = ('Hi '+ omemention + '! Practice starts in 30 minutes, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                                await bot.send_message(channel2, msg4)
                                practice = 0
                                stop = 1
                            
                        # if quadice == 1:
                        #     randompass()
                        #     msg4 = ('Hi <@&457299107371941888>! Practice starts in 30 minutes and will be a Squad, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        #     await bot.send_message(channel2, msg4)
                        #     quadice = 0
                        #     stop = 1
                        
                        # if pbpractice == 1:
                        #     randompass()
                        #     msg2 = ('Hello <@&457299107371941888>! Practice starts in 30 minutes and will be a Private Battle. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        #     await bot.send_message(channel2, msg2)
                        #     pbpractice = 0
                        #     stop = 1
                            
                    elif stop == 1:
                        await asyncio.sleep(60)
                        stop = 0
                        
            else:
                await bot.send_message(message.channel, 'Bot already started!')
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
    
    # if message.content.startswith('!pb'):
    #     pbpractice = 1
    
    # if message.content.startswith('!squad'):
    #     quadice = 1
        
    # if message.content.startswith('!pbstart'):
    #     await bot.send_message(channel2, msg3)
    
    # if message.content.startswith('!squadstart'):
    #     await bot.send_message(channel2, msg5)
    
    if message.content.startswith('!canprac'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            canceled = True
            await bot.send_message(message.channel, "Practice canceled. Oof.")
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
    
    if message.content.startswith('!practice'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            practice = 1
            await bot.send_message(message.channel, "Command successful.")
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
    
    if message.content.startswith('!pracstart'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            await bot.send_message(channel2, msg3)
            await bot.send_message(message.channel, "Command successful.")
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
     
    if message.content.startswith('!omepassed'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Omega")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Omega!").format(message)
            await bot.send_message(channel2, welbome)
            
            curname = str(message.mentions[0].display_name)
            nickchange("△")
                
            await bot.change_nickname(message.mentions[0], newnick)
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
            
    if message.content.startswith('!infpassed'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Infinite")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Infinite!").format(message)
            await bot.send_message(infanc, welbome)
        
            curname = str(message.mentions[0].display_name)
            nickchange("▲")
                
            await bot.change_nickname(message.mentions[0], newnick)
            
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
            

    if message.content.startswith('!alppassed'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            mentioned = message.mentions[0].id
            role = discord.utils.get(user.server.roles, name="Alpha")
            await bot.add_roles(message.mentions[0], role)
            welbome = ("Let's welcome <@" + mentioned + "> to Alpha!").format(message)
            await bot.send_message(alpanc, welbome)
        
            curname = str(message.mentions[0].display_name)
            nickchange("∴")
                
            await bot.change_nickname(message.mentions[0], newnick)
            
            await bot.send_message(message.channel, "Command successful.")
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
        
    
    if message.content.startswith('!captain'):
        allowed = False
        user = message.author
        roles = user.roles
        
        permissions(message.author.id)
            
        if allowed:
            curname = str(message.mentions[0].display_name)
            nickchange("◆")
            
            if curname == newnick:
                bot.send_message(message.channel, "You already have the captain symbol. I'll probably crash now...")
            else:
                bot.send_message(message.channel, "Name changed.")
                
            await bot.change_nickname(message.mentions[0], newnick)
            
        else:
            await bot.send_message(message.channel, "You are not allowed to execute this command.")
            
            
    if message.content.startswith('!pzhelp'):
        await bot.send_message(message.channel, "https://pastebin.com/sBQrV3s3")
        
    if message.content.startswith('!pzchangelog'):
        await bot.send_message(message.channel, "https://pastebin.com/Ejyi0hWx")
        
    if message.content.startswith('!pzhello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
        
    if message.content.startswith('!pzbotcode'):
        await bot.send_message(message.channel, "https://github.com/Sonic4999/PriZmBotv2")
        
    if message.content.startswith("Hi"):
        if message.author.id == '465946454264119306':
            pong = "🏓"
            await bot.add_reaction(message, pong)
    
    if message.content.startswith("Let's"):
        if message.author.id == '465946454264119306':
            clap = "👏"
            await bot.add_reaction(message, clap)
        
bot.run(TOKEN)

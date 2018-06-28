# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py was used for basic blueprints for the rest of this project
# Uses discord.py
# Remember to change the token to the working one and back to 'Nope' before you send anything to Github.
import discord
import datetime
import asyncio
import time
import random

TOKEN = 'NOPE'

client = discord.Client()

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

@client.event
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
    
    
    channel2 = client.get_channel("457939628209602560")
    msg3 = ('Hello <@&457299107371941888>! Practice starts now!')
    
    #if message.author == client.user:
       #return
        
    if message.content.startswith("!run"):
        counter = counter + 1 
        if counter <= 1:
            await client.send_message(message.channel, "Bot running in background!")
            while True:
                a = datetime.datetime.today().weekday()
                times = time.strftime('%H:%M')
                
                if stop <= 0:
                # this first one is meant for testing. delete before final release
                    if times == '13:06':
                        pbpractice = 1
                        
                # actual practices
                    if times == '14:30':
                        if a == 6:
                            quadice = 1
                    if times == '15:00':
                        if a == 6:
                            await client.send_message(channel2, msg3)
                    if times == '18:30':
                        if a == 5:
                            quadice = 1
                    if times == '19:00':
                        if 2 <= a <= 4:
                            quadice = 1
                        elif a == 5:
                            await client.send_message(channel2, msg3)
                        elif a == 6:
                            pbpractice = 1
                    if times == '19:30':
                        if 2 <= a <= 4:
                            await client.send_message(channel2, msg3)
                        elif a == 6:
                            await client.send_message(channel2, msg3)
                    await asyncio.sleep(1)
                    
                    if quadice == 1:
                        print('test')
                    
                    if pbpractice == 1:
                        randompass()
                        msg2 = ('Hello <@&457299107371941888>! Practice starts in 30 minutes and will be a Private Battle. The pass will be: ' + sn1 + sn2 + sn3 + sn4).format(message)
                        await client.send_message(channel2, msg2)
                        pbpractice = 0
                        stop = 1
                        
                elif stop == 1:
                    await asyncio.sleep(60)
                    
        else:
            await message.channel.send('Bot already started!')
    
    if message.content.startswith('!pb'):
        pbpractice = 1
        
    if message.content.startswith('!pbstart'):
        await client.send_message(channel2, msg3)
    
    if message.content.startswith('!captain'):
        curname = str(message.author.display_name)
        begin = 'pZ'
        capchara = "\u25C6"
        supbegin = begin + capchara
        
        if curname.startswith("pZ△"):
            newnick = curname.replace("pZ△", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ▲"):
            newnick = curname.replace("pZ▲", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ∴"):
            newnick = curname.replace("pZ∴", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ◆"):
            newnick = curname
            await client.send_message(message.channel, "You're already a captain!")
        else:
            newnick = begin + capchara + curname
            await client.send_message(message.channel, "Name changed.")
            
        await client.change_nickname(message.author, newnick)
        
    if message.content.startswith('!omega'):
        curname = str(message.author.display_name)
        begin = 'pZ'
        omechara = "\u25B3"
        supbegin = begin + omechara
        
        if curname.startswith("pZ△"):
            newnick = curname
            await client.send_message(message.channel, "You're already in Omega!")
        elif curname.startswith("pZ▲"):
            newnick = curname.replace("pZ▲", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ∴"):
            newnick = curname.replace("pZ∴", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ◆"):
            newnick = curname.replace("pZ◆", supbegin)
            await client.send_message(message.channel, "Name changed.")
        else:
            newnick = begin + omechara + curname
            await client.send_message(message.channel, "Name changed.")
            
        await client.change_nickname(message.author, newnick)

    if message.content.startswith('!infinite'):
        curname = str(message.author.display_name)
        begin = 'pZ'
        infchara = "\u25B2"
        supbegin = begin + infchara
        
        if curname.startswith("pZ△"):
            newnick = curname.replace("pZ△", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ▲"):
            newnick = curname
            await client.send_message(message.channel, "You're already in Infinite!")
        elif curname.startswith("pZ∴"):
            newnick = curname.replace("pZ∴", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ◆"):
            newnick = curname.replace("pZ◆", supbegin)
            await client.send_message(message.channel, "Name changed.")
        else:
            newnick = begin + infchara + curname
            await client.send_message(message.channel, "Name changed.")
            
        await client.change_nickname(message.author, newnick)
        
    if message.content.startswith('!alpha'):
        curname = str(message.author.display_name)
        begin = 'pZ'
        alpchara = "\u2234"
        supbegin = begin + alpchara
        
        if curname.startswith("pZ△"):
            newnick = curname.replace("pZ△", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ▲"):
            newnick = curname.replace("pZ▲", supbegin)
            await client.send_message(message.channel, "Name changed.")
        elif curname.startswith("pZ∴"):
            newnick = curname
            await client.send_message(message.channel, "You're already in Alpha!")
        elif curname.startswith("pZ◆"):
            newnick = curname.replace("pZ◆", supbegin)
            await client.send_message(message.channel, "Name changed.")
        else:
            newnick = begin + alpchara + curname
            await client.send_message(message.channel, "Name changed.")
            
        await client.change_nickname(message.author, newnick)
        

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!test'):
        await client.send_message(message.channel, "Hi!")
        
    #if message.content.startswith('Hi!'):
        #author = str(message.author)
        #if author == 'PriZmBot#7447':
            #idz = message.id
            #wave = "👋"
            #await client.add_reaction(message, wave)
            
            #res = await client.wait_for_reaction(['👋'])
            #thing = str(reaction.user)
            #if thing == 'PriZmBot#7447':
                #print('hi')
            #else:
                #await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

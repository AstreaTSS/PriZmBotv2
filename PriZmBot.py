# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py was used for basic blueprints for the rest of this project
# Uses discord.py rewrite
# This project is for my Splatoon 2 mentor, Jeepers. Thank you for everything.
import discord
import datetime
import asyncio
import time
import random

TOKEN = 'NDYxNzAxNjg2MjM1MjM0MzM0.DhXIuA.1iCIvZVVjHQJs3m-pd29hxfaSS4'

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
    
    channel2 = client.get_channel(457939628209602560)
    msg3 = ('Hello <@&457299107371941888>! Practice starts now!')
    
    if message.author == client.user:
        return
        
    if message.content.startswith("!run"):
        counter = counter + 1 
        if counter <= 1:
            await message.channel.send('Bot running in background!')
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
                            await channel2.send(msg3)
                    if times == '18:30':
                        if a == 5:
                            quadice = 1
                    if times == '19:00':
                        if 2 <= a <= 4:
                            quadice = 1
                        elif a == 5:
                            await channel2.send(msg3)
                        elif a == 6:
                            pbpractice = 1
                    if times == '19:30':
                        if 2 <= a <= 4:
                            await channel2.send(msg3)
                        elif a == 6:
                            await channel2.send(msg3)
                    await asyncio.sleep(1)
                    
                    if quadice == 1:
                        print('test')
                    
                    if pbpractice == 1:
                        randompass()
                        msg2 = ('Hello <@&457299107371941888>! Practice starts in 30 minutes and will be a Private Battle. The pass will be: ' + sn1 + sn2 + sn3 + sn4).format(message)
                        await channel2.send(msg2)
                        pbpractice = 0
                        stop = 1
                        
                elif stop == 1:
                    await asyncio.sleep(60)
                    
        else:
            await message.channel.send('Bot already started!')
    
    if message.content.startswith('!pb'):
        pbpractice = 1
        
    if message.content.startswith('!pbstart'):
        await channel2.send(msg3)
    
    if message.content.startswith('!captain'):
        curnick = discord.Member.nick
        print(curnick)
        begin = 'pZ'
        capchara = "\u25C6"
        newnick = begin + capchara + curnick
        await discord.Member.edit(nick, newnick)

    if message.content.startswith('!hello'):
        channel = client.get_channel(457939628209602560)
        msg = 'Hello {0.author.mention}'.format(message)
        await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

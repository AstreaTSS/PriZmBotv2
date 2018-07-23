# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py was used for basic blueprints for the rest of this project
# Uses discord.py
# Remember to change the token to the working one and back to 'Nope' before you send anything to Github.

import discord
from discord.ext import commands
import datetime
import asyncio
import time
import random

from config import *
from changelog import *

# client = discord.Client()

description = '''A bot for the use of PriZm, a Splatoon 2 clan.'''

bot = commands.Bot(command_prefix='!', description=description)

day = datetime.datetime.today().weekday()

counter = 0
quadice = 0
pbpractice = 0
omeprac = 0
alpprac = 0
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

roles = None
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
    elif autrid == '465946454264119306':
        allowed = True


def randompass():
    global sn1
    global sn2
    global sn3
    global sn4

    n1 = random.randint(1, 8)
    if n1 >= 5:
        n1 = n1 + 1
    n2 = random.randint(1, 8)
    if n2 >= 5:
        n2 = n2 + 1
    n3 = random.randint(1, 8)
    if n3 >= 5:
        n3 = n3 + 1
    n4 = random.randint(1, 8)
    if n4 >= 5:
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

    if mainServer:
        bots = bot.get_channel('416865837610172418')
    elif developServer:
        bots = bot.get_channel('429720487678050308')

    msg = await bot.send_message(bots, '!run')
    await bot.delete_message(msg)


@bot.event
async def on_message(message):
    global counter
    global quadice
    global pbpractice
    global omeprac
    global alpprac
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

    blop = 0
    alpgo = None

    if message.server is None and message.author != bot.user:
        oof = 1

    else:

        if blop < 1:
            if mainServer:
                user = message.author
                lieut = discord.utils.get(user.server.roles, name="Lieutenant")
                cocap = discord.utils.get(user.server.roles, name="Co-captains ◆")
                cap = discord.utils.get(user.server.roles, name="Captains ◆")
                clancap = discord.utils.get(user.server.roles, name="Clan Captain")
                admin = discord.utils.get(user.server.roles, name="Moderator")

                omerole = discord.utils.get(user.server.roles, name="Omega △")
                infrole = discord.utils.get(user.server.roles, name="Infinite ▲")
                alprole = discord.utils.get(user.server.roles, name="Alpha ∴")

                channel2 = bot.get_channel("458329789854646319")
                infanc = bot.get_channel("458329789854646319")
                alpanc = bot.get_channel("458329789854646319")

            elif developServer:
                user = message.author
                lieut = discord.utils.get(user.server.roles, name="Lieutenant")
                cocap = discord.utils.get(user.server.roles, name="Co-Captain")
                cap = discord.utils.get(user.server.roles, name="Captain")
                clancap = discord.utils.get(user.server.roles, name="Clan Captain")
                admin = discord.utils.get(user.server.roles, name="Admin")

                omerole = discord.utils.get(user.server.roles, name="Omega")
                infrole = discord.utils.get(user.server.roles, name="Infinite")
                alprole = discord.utils.get(user.server.roles, name="Alpha")

                channel2 = bot.get_channel("457939628209602560")
                infanc = bot.get_channel("462286782080483350")
                alpanc = bot.get_channel("465547475839746058")

            omemention = omerole.mention
            alpmention = alprole.mention

            msg5 = (
                'Hello <@&457299107371941888>! Practice starts now! The list will be put out depending on who reacted to the previous message.')
            msg3 = ('Hello ' + omemention + '! Practice starts now! Again, the pass is ' + sn1 + sn2 + sn3 + sn4 + "!")

            alpgo = "Hello " + alpmention + '! Practice starts now! Again, the pass is ' + sn1 + sn2 + sn3 + sn4 + "!"
            omecan = 0
            alpcan = 0
            blop = 1

        if message.content == "!run":
            allowed = False
            user = message.author
            roles = user.roles

            permissions(message.author.id)

            if allowed:
                counter = counter + 1
                if counter <= 1:
                    while True:

                        msg3 = ('Hello ' + omemention + '! Practice starts now! Again, the pass is ' + sn1 + sn2 + sn3 + sn4 + "!")
                        alpgo = ("Hello " + alpmention + '! Practice starts now! Again, the pass is ' + sn1 + sn2 + sn3 + sn4 + "!")

                        if omecan == 3:
                            omecan = 0

                        if alpcan == 3:
                            alpcan = 0

                        day = datetime.datetime.today().weekday()
                        times = time.strftime('%H:%M')

                        if stop <= 0:

                            # actual practices
                            if times == '14:30':  # 2:30 PM
                                if day == 6:
                                    quadice = 1
                                    omeprac = 1

                            if times == '15:00':  # 3 PM
                                if day == 6:
                                    if omecan > 0 and omecan < 3:
                                        omeprac = 1
                                    else:
                                        # await bot.send_message(channel2, msg5)
                                        await bot.send_message(channel2, msg3)
                                        stop = 1

                            if times == '16:30':  # 4:30 PM
                                if day == 5:
                                    alpprac = 1
                                elif day == 6:
                                    alpprac = 1

                            if times == '17:00':  # 5 PM
                                if day == 5:
                                    if alpcan > 0 and alpcan < 3:
                                        alpprac = 1
                                    else:
                                        await bot.send_message(alpanc, alpgo)
                                elif day == 6:
                                    if alpcan > 0 and alpcan < 3:
                                        alpprac = 1
                                    else:
                                        await bot.send_message(alpanc, alpgo)

                            if times == '18:30':  # 6:30 PM
                                if day == 6:
                                    pbpractice = 1
                                    omeprac = 1
                                elif day == 5:
                                    omeprac = 1

                            if times == '19:00':  # 7 PM
                                if day == 6:
                                    if omecan > 0 and omecan < 3:
                                        omeprac = 1
                                    else:
                                        await bot.send_message(channel2, msg3)
                                        stop = 1
                                elif day == 2:
                                    quadice = 1
                                    omeprac = 1
                                elif day == 3:
                                    pbpractice = 1
                                    omeprac = 1
                                elif day == 4:
                                    omeprac = 1
                                elif day == 5:
                                    if omecan > 0 and omecan < 3:
                                        omeprac = 1
                                    else:
                                        await bot.send_message(channel2, msg3)
                                        stop = 1

                            if times == '19:30':  # 7:30 PM
                                if omecan > 0 and omecan < 3:
                                    omeprac = 1
                                else:
                                    if day == 2:
                                        # await bot.send_message(channel2, msg5)
                                        await bot.send_message(channel2, msg3)
                                        stop = 1
                                    elif day == 3:
                                        await bot.send_message(channel2, msg3)
                                        stop = 1
                                    elif day == 4:
                                        await bot.send_message(channel2, msg3)
                                        stop = 1

                            if omeprac == 1:
                                if 0 < omecan < 3:
                                    omeprac = 0
                                    stop = 1
                                    omecan = omecan + 1
                                else:
                                    randompass()
                                    msg4 = ('Hi ' + omemention + '! Practice starts in 30 minutes, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                                    slop = await bot.send_message(channel2, msg4)

                                    pong = "🏓"
                                    await bot.add_reaction(slop, pong)
                                    omeprac = 0
                                    stop = 1

                            if alpprac == 1:
                                print("hello")
                                if 0 < alpcan < 3:
                                    alpprac = 0
                                    stop = 1
                                    alpcan = alpcan + 1
                                else:
                                    randompass()
                                    nou = ('Hi ' + alpmention + '! Practice starts in 30 minutes, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                                    lop = await bot.send_message(alpanc, nou)

                                    pong = "🏓"
                                    await bot.add_reaction(lop, pong)
                                    alpprac = 0
                                    stop = 1

                            await asyncio.sleep(1)

                        elif stop == 1:
                            await asyncio.sleep(60)
                            stop = 0

                else:
                    await bot.send_message(message.channel, 'Bot already started!')
            else:
                await bot.send_message(message.channel, "You are not allowed to execute this command.")
        
        
        if message.content == '!canprac':
            allowed = False
            user = message.author
            roles = user.roles

            permissions(message.author.id)
            
            if allowed:
                loop = True
                
                await bot.send_message(message.channel,
                                           "```\nFor what division?\n1: Omega\n2: Alpha\n3: Cancel\nRespond to the number that correlates with the division you want. (and respond only with that number)\n```")
                while loop:
                    msg = await bot.wait_for_message(author=message.author)

                    if msg.content == ("1"):
                        loop = False
                        omecan = 1
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("2"):
                        loop = False
                        alpcan = 1
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("3"):
                        loop = False
                        await bot.send_message(msg.channel, "Canceled")
                    else:
                        await bot.send_message(msg.channel, "Your response doesn't seem to be a number 1-4. Try again.")
                        
            else:
                await bot.send_message(message.channel, "You are not allowed to execute this command.")
                
        if message.content == '!prac30':
            allowed = False
            user = message.author
            roles = user.roles

            permissions(message.author.id)
            
            if allowed:
                loop = True
                
                await bot.send_message(message.channel,
                                           "```\nFor what division?\n1: Omega\n2: Alpha\n3: Cancel\nRespond to the number that correlates with the division you want. (and respond only with that number)\n```")
                while loop:
                    msg = await bot.wait_for_message(author=message.author)

                    if msg.content == ("2"):
                        loop = False
                        
                        randompass()
                        nou = ('Hi ' + alpmention + '! Practice starts in 30 minutes, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        lop = await bot.send_message(alpanc, nou)

                        pong = "🏓"
                        await bot.add_reaction(lop, pong)
                        
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("1"):
                        loop = False
                        randompass()
                        msg4 = ('Hi ' + omemention + '! Practice starts in 30 minutes, so make sure you react to this message with a 🏓 so we can get a list. The pass will be: ' + sn1 + sn2 + sn3 + sn4)
                        slop = await bot.send_message(channel2, msg4)

                        pong = "🏓"
                        await bot.add_reaction(slop, pong)
                        
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("3"):
                        loop = False
                        await bot.send_message(msg.channel, "Canceled")
                    else:
                        await bot.send_message(msg.channel, "Your response doesn't seem to be a number 1-4. Try again.")
                        
            else:
                await bot.send_message(message.channel, "You are not allowed to execute this command.")
                
        if message.content == '!pracstart':
            allowed = False
            user = message.author
            roles = user.roles

            permissions(message.author.id)
            
            if allowed:
                loop = True
                
                await bot.send_message(message.channel,
                                           "```\nFor what division?\n1: Omega\n2: Alpha\n3: Cancel\nRespond to the number that correlates with the division you want. (and respond only with that number)\n```")
                while loop:
                    msg = await bot.wait_for_message(author=message.author)

                    if msg.content == ("1"):
                        loop = False
                        await bot.send_message(channel2, msg3)
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("2"):
                        loop = False
                        await bot.send_message(alpanc, alpgo)
                        await bot.send_message(message.channel, "Command successful.")
                    elif msg.content == ("3"):
                        loop = False
                        await bot.send_message(msg.channel, "Canceled")
                    else:
                        await bot.send_message(msg.channel, "Your response doesn't seem to be a number 1-4. Try again.")
                        
            else:
                await bot.send_message(message.channel, "You are not allowed to execute this command.")

        if message.content.startswith('!passed'):
            allowed = False
            user = message.author
            roles = user.roles

            permissions(message.author.id)

            if allowed:
                loop = True

                try:
                    mentioned = message.mentions[0].id
                except IndexError:
                    await bot.send_message(message.channel,
                                           "It seems like you didn't mention the person to pass. Exiting command...")
                    loop = False

                if loop:
                    await bot.send_message(message.channel,
                                           "```\nFor what division?\n1: Omega\n2: Infinite\n3: Alpha\n4: Cancel\nRespond to the number that correlates with the division you want. (and respond only with that number)\n```")

                while loop:

                    msg = await bot.wait_for_message(author=message.author)

                    if msg.content == ("1"):
                        loop = False

                        mentioned = message.mentions[0].id
                        await bot.add_roles(message.mentions[0], omerole)
                        welbome = ("Let's welcome <@" + mentioned + "> to Omega!").format(message)
                        welcome = await bot.send_message(channel2, welbome)

                        clap = "👏"
                        await bot.add_reaction(welcome, clap)

                        curname = str(message.mentions[0].display_name)
                        nickchange("△")

                        await bot.change_nickname(message.mentions[0], newnick)

                        await bot.send_message(msg.channel, "Command successful.")

                    elif msg.content == ("2"):
                        loop = False

                        mentioned = message.mentions[0].id
                        await bot.add_roles(message.mentions[0], infrole)
                        welbome = ("Let's welcome <@" + mentioned + "> to Infinite!").format(message)
                        welcome = await bot.send_message(infanc, welbome)

                        clap = "👏"
                        await bot.add_reaction(welcome, clap)

                        curname = str(message.mentions[0].display_name)
                        nickchange("▲")

                        await bot.change_nickname(message.mentions[0], newnick)

                        await bot.send_message(msg.channel, "Command successful.")

                    elif msg.content == ("3"):
                        loop = False

                        mentioned = message.mentions[0].id
                        await bot.add_roles(message.mentions[0], alprole)
                        welbome = ("Let's welcome <@" + mentioned + "> to Alpha!").format(message)
                        welcome = await bot.send_message(alpanc, welbome)

                        clap = "👏"
                        await bot.add_reaction(welcome, clap)

                        curname = str(message.mentions[0].display_name)
                        nickchange("∴")

                        await bot.change_nickname(message.mentions[0], newnick)

                        await bot.send_message(message.channel, "Command successful.")

                    elif msg.content == ("4"):
                        loop = False
                        await bot.send_message(msg.channel, "Canceled.")

                    else:
                        await bot.send_message(msg.channel, "Your response doesn't seem to be a number 1-4. Try again.")

            else:
                await bot.send_message(message.channel, "You are not allowed to execute this command.")

        if message.content.startswith('!capnick'):
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

        if message.content == '!pzhelp':
            await bot.send_message(message.channel, "https://pastebin.com/sBQrV3s3")

        if message.content == '!pzchangelog':
            ori = await bot.send_message(message.channel, "```\nPastebin link: https://pastebin.com/Ejyi0hWx.\nTo navigate the changelog, enter the version you want in the chat (Example: \"v1.2.3\").\nTo see all of the version numbers, type \"list\"\nTo keep up the current screen you are seeing without being able to change the screen via inputs, type \"keepup\"\nTo exit, type \"exit\"\n```")

            loop = True

            versions = ["v1.0.0", "v1.0.1", "v1.1.0", "v1.1.1", "v1.1.2", "v1.1.3", "v1.1.4", "v1.2.0", "v1.2.1",
                        "v1.2.2", "v1.2.3", "v1.2.4", "v1.2.5", "v1.2.6"]
            tosend = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14]

            while loop:
                msg = await bot.wait_for_message(author=message.author)

                if msg.content in versions:
                    num = versions.index(msg.content)
                    tosay = tosend[num]

                    await bot.edit_message(ori, tosay + ending)
                    await bot.delete_message(msg)

                elif msg.content == "list":
                    await bot.edit_message(ori, "```\nAll versions: " + (
                            '%s' % ', '.join(map(str, versions))) + "\n" + ending)
                    await bot.delete_message(msg)

                elif msg.content == "keepup":
                    loop = False
                    akap = await bot.send_message(msg.channel,
                                                  "Alright. I'll keep this screen up, but won't accept any new input, so the screen cannot be edited.")
                    await bot.edit_message(ori, tosay + "```")
                    await bot.delete_message(msg)
                    await asyncio.sleep(4)
                    await bot.delete_message(akap)

                elif msg.content == "exit":
                    await bot.delete_message(ori)
                    await bot.delete_message(msg)
                    akap = await bot.send_message(msg.channel, "Exited.")
                    await asyncio.sleep(3)
                    await bot.delete_message(akap)
                    loop = False
                else:
                    await bot.delete_message(msg)
                    akap = await bot.send_message(msg.channel,
                                                  "This does not appear to be valid. Try again (and due to limitations, you have to wait for four seconds before you can).")
                    await asyncio.sleep(4)
                    await bot.delete_message(akap)

        if message.content == '!pzhello':
            msg = 'Hello {0.author.mention}'.format(message)
            await bot.send_message(message.channel, msg)

        if message.content == '!pzbotcode':
            await bot.send_message(message.channel, "https://github.com/Sonic4999/PriZmBotv2")

        pine = random.randint(0, 499999)
        if pine == 49:
            apple = "🍍"
            await bot.add_reaction(message, apple)


bot.run(TOKEN)

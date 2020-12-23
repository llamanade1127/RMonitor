import discord
import json
import time
from random import randint
from discord.ext import commands
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
#NTAzMDMxM---DQyNDIxMDMwOTIy.X9_3Iw.O882DNtD9DUUs1eJcDeTje409X4 [Walter]
#Nzc5NTA5N---jQ2MTc1NjMzNDMw.X7hk7g.CxSXSuTj9sz0DmL8vvauRB5ZKkw [bot]
#NzkwMzE4OT---A4NTA2MTEyMDMw.X-OEhQ.Cl5j9sE9xDeBTUyz9fOKYNC3Z48 [bot_test]
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    #Screen.wrapper(start)

    print_data_start()



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.event
async def on_message(message):
    channel = message.channel.id
    guild = message.guild.id
    #print(guild)
    if check_channel(channel, guild) == channel:
        channelToSend = client.get_channel(get_private_channel(guild))
        await send_embed_to_channel(channelToSend, message)
    #await channelToSend.send("yay")

#commands
async def send_embed_to_channel(channel_to_send, message):
        embedVar = discord.Embed(title="MESSAGE", description=f"New message from {message.author.mention}", color=0x00ff00)
        embedVar.add_field(name="Message:", value=f"{message.content}", inline=False)
        embedVar.add_field(name="Message Link", value=f"{message.jump_url}", inline=False)
        await channel_to_send.send(embed=embedVar)




#end_commands


def start(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ASCIIMATICS", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])
    time.sleep(3)
    return

#this function Checks if the channel is the same as the channel in the json file
def check_channel(channel, guild):
    with open('./guilds.json') as f:
        data = json.load(f)
    guilds_json = data["guilds"]
    for guilds in guilds_json:
        if guilds["guildId"] == guild:
            channel = guilds["listenChannel"]
            print(channel)
            return channel
    return False

def get_private_channel(guild):
        with open('./guilds.json') as f:
            data = json.load(f)
        guilds = data["guilds"]
        for guild_spef in guilds:
            if guild_spef["guildId"] == guild:
                return guild_spef["privateChannel"]

def print_data_start():

    print_data = [
        f"╔═══════════════════════════ ONLINE ═══════════════════════════╗",
        f"║ Logged in as: {client.user.name}#{client.user.discriminator} | {client.user.id}",
    ]

    for index in range(len(print_data)):
        if index != 0:
            print_data[index] += ((len(print_data[0]) - len(print_data[index])-1) * " ") + "║"
            print_data.append(f"╚{'═'*(len(print_data[0])-2)}╝")

    for line in print_data:
        print(line)

def get_client_data():
    with open('./config.json') as f:
        data = json.load(f)
    token = data['token']
    return token

client.run(get_client_data(), bot = False)

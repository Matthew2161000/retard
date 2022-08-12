from ast import Try
from decouple import config
from distutils.log import error
import discord, os, sys
from discord.ext import commands

TOKEN = config('KEY')

intents = discord.Intents.default()
intents.members = True

prefix = '$'

client = commands.Bot(command_prefix = prefix, intents = intents, case_insensitive = True)

def load_cogs():
    # DOCUMENT FOR CLARITY
    iter = 0
    print("ATTEMPTING TO LOAD ALL COGS \n")

    directory = os.listdir("./cogs")

    # LOOP THROUGH LIST AND LOAD COGS.PY
    for file in directory:
        if file.endswith(".py"):
            try:
                # SUCCESS
                client.load_extension(f"cogs.{file[:-3]}")
                print(f"LOAD: {file} SUCCESS")
                iter += 1
            except commands.ExtensionError as e:
                # FAILURE
                print(f"LOAD: {file} FAILURE ({e.__class__.__name__}: {e})")
    #FINISH
    print(f"\n{iter}/{len(directory)-1} COGS LOADED")
            
load_cogs()

@client.command()
# RELOAD COG VIA DISCORD COMMAND
# ex.: $reload_cog sample
async def reload_cog(ctx, arg):
    try:
        client.reload_extension(f"cogs.{arg}")
        print(f"\nRELOAD: {arg} SUCCESS")
    except commands.ExtensionError as e:
        print(f"\nRELOAD: {arg} FAILURE ({e.__class__.__name__}: {e})")


@client.event
async def on_ready():
    # AWAKE ALERT + ACTIVE GUILDS
    print(f"Client ready and awake in {len(client.guilds)} servers")


client.run(TOKEN)
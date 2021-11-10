import discord
import re
import yaml

# from discord.ext import commands

bot = discord.Client()


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name + "#" + bot.user.discriminator)
    print(bot.user.id)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="with Godlina"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        print("Message from " + message.author.name + ": " + message.content)
        if message.content.startswith(
            ("I'm", "Im", "i'm", "im", "I am", "i am")):
            reply = re.split("I'm |Im |i'm |im |I am |i am ",
                             message.content)[1]
            await message.reply("Hi " + reply + ", I'm Dad")
            print("Replied to " + message.author.name + " with Dad Joke")


with open("secrets.yaml") as stream:
    try:
        secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        print("Secrets.yaml failed to load, exiting...")
        raise SystemExit

# bot.run()

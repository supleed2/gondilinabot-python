import discord
import re
import yaml
import random

# from discord.ext import commands

bot = discord.Client()
mincooldown = 3
maxcooldown = 10
counter = random.randrange(mincooldown, maxcooldown)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name + "#" + bot.user.discriminator)
    print(bot.user.id)
    print("Init Counter: " + str(counter))
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(name="with Godlina")
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.author.id == 581890740360052764:
        reply = re.split("(^| )(I'm|Im|i'm|im|I am|i am)( )", message.content, 1)
        if len(reply) > 1:
            print("Message from " + message.author.name + ": " + message.content)
            print(
                "Reply: Length:"
                + str(len(reply))
                + ", Final Contents: {"
                + reply[-1]
                + "}"
            )
            await message.reply("Hi " + reply[-1] + ", I'm Dad")
            print(
                "Replied unconditionally to " + message.author.name + " with Dad Joke"
            )
    else:
        global counter
        # TODO: Add detection for "genshin" and replace with "g*nshin"
        reply = re.split("(^| )(I'm|Im|i'm|im|I am|i am)( )", message.content, 1)
        if len(reply) > 1:
            print("Message from " + message.author.name + ": " + message.content)
            print(
                "Reply: Length:"
                + str(len(reply))
                + ", Final Contents: {"
                + reply[-1]
                + "}"
            )
            if counter > 0:
                counter -= 1
                print("Cooldown: " + str(counter) + " messages")
            else:
                counter = random.randrange(mincooldown, maxcooldown)
                await message.reply("Hi " + reply[-1] + ", I'm Dad")
                print("Replied to " + message.author.name + " with Dad Joke")


with open("secrets.yaml") as stream:
    try:
        secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        print("Secrets.yaml failed to load, exiting...")
        raise SystemExit


bot.run(secrets["bottoken"])

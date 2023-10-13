import discord, json

with open('config.json') as f:
    config = json.load(f)

owners = config["owners"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print(owners)

    async def on_message(self, message):
        if message.author.id not in owners:
            return

        split = message.content.split(' ')
        print(message.content, message.author.id)
        if (split[0] != config["prefix"]):
            return
        else:
            await message.channel.send(split[1])

def getConfig():
    return config
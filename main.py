import discord
from discord.ext import commands
intents = discord.Intents(messages=True,guilds=True,reactions=True, members=True,presences=True)



Bot = commands.Bot(command_prefix="!mm ", intents=intents)
@Bot.event
async def on_ready():
    print("ben hazırım")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} aramıza katuldı hos geldi")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gidenler")
    await channel.send(f"{member} aramıza katuldı hos geldi")



@Bot.command()
async def link(msg):
    await msg.send("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.trendyol.com%2Fulker%2Flink-seftali-200-ml-p-56949115&psig=AOvVaw2PjLwLcZJjvgiHV0w9CYXZ&ust=1675971163078000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJCN4KDVhv0CFQAAAAAdAAAAABAE")
@Bot.command()
async def devLinks(msg):
    await msg.send("github.com/yusufsaidx and yusuf-said")



Bot.run("#")

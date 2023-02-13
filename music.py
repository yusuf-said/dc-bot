import discord
import asyncio
import requests
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

client = discord.Client()
@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!play'):
        song_name = message.content[6:]
        query = song_name.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={query}"
        source_code = requests.get(url).text
        search_results = source_code.split("/watch?v=")[1]
        video_id = search_results.split('"')[0]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            title = info['title']
            url = info['url']
            voice_channel = message.author.voice.channel
            if not voice_channel:
                await message.channel.send("You're not connected to a voice channel.")
                return
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio(url))
            voice.is_playing()
            await message.channel.send(f'Playing {title}')
    elif message.content.startswith('!stop'):
        voice_channel = message.guild.voice_client
        if not voice_channel:
            await message.channel.send("Bot is not connected to a voice channel.")
            return
        await voice_channel.disconnect()
        await message.channel.send("Music stopped.")



client.run('')


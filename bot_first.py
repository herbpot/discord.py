
import discord
from discord.ext import commands,tasks
import os
import asyncio
import youtube_dl
import list_f_bot



# Get the API token from the .env file.

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "!")
bot.remove_command("help")
music_queues = {}
music_players = {}

def check_queue(id):
	if music_queues[id] != []:
		player = music_queues[id].pop(0)
		music_players[id] = player
		player.start()
		#print(player.title)
		print("[check_queue] Kolejna piosenka")
	else:
		del music_players[id]
		print("[check_queue] Koniec kolejki")

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

@bot.event
async def on_ready():
    print('봇 가동중')
    print(f'봇 이름 >>> {bot.user.name}')
    print('success!')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command()
async def plist(ctx,url) : 
    list_f_bot.playlist.make_play_tread(bot,url)
    await ctx.send('리스트에 저장했습니다')

@bot.command()
async def play(ctx):
    try :
        await ctx.send('노래 시작')
        list_f_bot.playlist.player_start()
    except :
        await ctx.send('오류')

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command()
async def pl(ctx,url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))


# @bot.command(name='play_song', help='To play song')
# async def play(ctx,url):
#     try :
#         server = ctx.message.guild
#         voice_channel = server.voice_clients[0]

#         async with ctx.typing():
#             filename = await YTDLSource.from_url(url, loop=bot.loop)
#             voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
#         await ctx.send('**Now playing:** {}'.format(filename))
#     except:
#         await ctx.send("The bot is not connected to a voice channel.")

bot.run("ODU0NjU3ODExMjE5NDgwNjA2.YMnIHA.KtV3aIqRS6wjcMSrY1cuRHKSTB0")
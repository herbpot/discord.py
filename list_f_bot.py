from re import T
import discord
import youtube_dl
import threading
# import pafy

# music_l = list()
# music_l_name = list()
thread_list = []
player = ()
class playlist():
    def player_start():
        
        while True :
            if not threading.Thread.is_alive :
                thread_list[0] = threading.Thread(thread_list[0])
                thread_list[0].start()
                del thread_list[0]
                print(thread_list)
            if len(thread_list) == 0 :
                break
            

    #     def list(url):
    #         info = pafy.new(url)
    #         music_l.append(url)
    #         music_l_name.append(info.title)
    #         print(music_l_name)
            
    #         return music_l,music_l_name

    def make_play_tread(bot,url):
        global player_th
        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice = bot.voice_clients[0]
        thread_list.append(voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)))
        print(thread_list)


    # def make_play_tread(bot,url):
    #     global player_th
    #     ydl_opts = {'format': 'bestaudio'}
    #     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         info = ydl.extract_info(url, download=False)
    #         URL = info['formats'][0]['url']
    #     voice = bot.voice_clients[0]
    #     a = voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    #     b = threading.Thread(a)
    #     print(thread_list)

    

# a = print('hi')
# b = threading.Thread(a)
# b.start()

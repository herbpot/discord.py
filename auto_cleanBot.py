import discord
from discord.channel import TextChannel
from discord.ext import commands

bot = commands.Bot(command_prefix='*')
bot.remove_command('help')

time = 0
com_channel = 0
setting = 0

@bot.event
async def on_ready():
    print(bot.user.name)
    print('디스코드세계를 돌아다니는 중이에요')
    await bot.change_presence(activity=discord.Game(name='외로운 봇들 귀가시키는 중...'))

@bot.command()
async def setchannel(ctx):
    if ctx.message.author.guild_permissions.manage_messages:
        global time,com_channel,setting
        if time == 0 :
            await ctx.send('입장 메세지를 이 체널에 보내려면 해당 명령어를 다시 입력 하세요')
        if time == 1 :
            com_channel = TextChannel.id
            await ctx.send('저장 완료')
            print(com_channel, TextChannel.id)

        time = time + 1

        if time == 2 :
            time = 0
        setting = 1

@bot.event
async def on_member_join(member):
    global com_channel,setting
    if setting == 1 :
        channel = com_channel
        msg = '<@{}>님이 달 저편에 새롭게 착륙하셨습니다 모두 환영해 주세요'.format(str(member.id))
        channel.send()

@bot.event
async def on_voice_state_update(member,before,after):
    guild = discord.Guild
    for channel in member.guild.voice_channels :
        if len(channel.members) == 1 :
            for role in channel.members[0].roles :
                if member.bot :
                    await channel.members[0].move_to(None)

@bot.command()
async def help(ctx) :
    await ctx.send('''
    지금 가능한 기능:
    음성체널에 혼자 남은 봇 퇴장시키기
    새로운 사람이 들어오면 알려주기(메세지를 입력할 방은 먼저 알려주세요)
    명령어 리스트 보여주기(helpc)
    ''')
@bot.command()
async def helpc(ctx) :
    await ctx.send('''
    지금 가능한 기능:
    setchannel(알림을 전송할 방을 지정해요)
    ''')

bot.run("ODU0NjU3ODExMjE5NDgwNjA2.YMnIHA.KtV3aIqRS6wjcMSrY1cuRHKSTB0")
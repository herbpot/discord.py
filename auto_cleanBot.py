import discord
from discord.channel import TextChannel
from discord.ext import commands
from dataseting import seter as st

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
async def selfinfo(ctx,name,school1,school2,school3,day,password):
    log = st.setdata(name,school1,school2,school3,day,password)
    await ctx.channel.purge(limit=1)
    await ctx.send(log)

@bot.command()
async def selfstart(ctx,name) :
    log = st.start(name)
    await ctx.channel.purge(limit=1)
    await ctx.send(log)


@bot.command()
async def delmsg(ctx,num : int):
    await ctx.channel.purge(limit=num + 1)
    await ctx.send(f'{num}개 청소 완료')

@bot.command()
async def help(ctx) :
    embed = discord.Embed(title='help',description='기능 도움말',color=0x00aaaa)
    embed.add_field(name='음성체널에 혼자 남은 봇 퇴장시키기',value='자동이에요',inline=False)
    embed.add_field(name='새로운 사람이 들어오면 알려주기',value='메세지를 입력할 방은 먼저 알려주세요',inline=False)
    embed.add_field(name='명령어 리스트 보여주기',value='helpc',inline=False)
    embed.add_field(name='자동 자가진단',value='selfinfo,selfstart',inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def helpc(ctx) :
    embed = discord.Embed(title='helpc',description='명령어 도움말',color=0x00aaaa)
    embed.add_field(name='setchannel',value='신규유저의 알림을 전송할 방을 지정해요',inline=False)
    embed.add_field(name='selfinfo',value='자가진단 정보를 입력해요',inline=False)
    embed.add_field(name='selfstart',value='자가진단을 시작해요(1회)',inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def chelp(ctx, m):
    if m == 'selfinfo' :
        embed = discord.Embed(title='chelp',description='명령어 사용 도움말',color=0x00aaaa)
        embed.add_field(name='자가진단 정보를 입력해요',value='selfinfo 이름 지역 학교급 학교이름 생일(6자리) 비밀번호',inline=False)
        await ctx.send(embed=embed)

bot.run("ODU0NjU3ODExMjE5NDgwNjA2.YMnIHA.KtV3aIqRS6wjcMSrY1cuRHKSTB0")
import discord
from discord.channel import TextChannel
from discord.ext import commands
from discord.guild import Guild

bot = commands.Bot(command_prefix='*')
bot.remove_command('help')

time = 0
com_channel = 0
setting = 0

@bot.event
async def on_ready():
    print(bot.user.name)
    print('디스코드세계를 돌아다니는 중이에요')

@bot.command()
async def setchannel(ctx):
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
                if role.name == 'BOT' :
                    await channel.members[0].move_to(None)

bot.run("ODU0NjU3ODExMjE5NDgwNjA2.YMnIHA.KtV3aIqRS6wjcMSrY1cuRHKSTB0")
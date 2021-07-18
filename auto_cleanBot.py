import discord
from discord.channel import TextChannel
from discord.ext import commands
import traceback
import selenium

bot = commands.Bot(command_prefix='*')
bot.remove_command('help')

time = 0
com_channel = 0
setting = 0





from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Ww
import time

URL_login, URL_main = 'https://hcs.eduro.go.kr/#/relogin', 'https://hcs.eduro.go.kr/#/main'

class s :
    def setdata(self,datalist):
        self.password = str(datalist[-1])
        self.school = list([datalist[1],datalist[2],datalist[3]])
        self.name = str(datalist[0])
        self.day = str(datalist[4])
            
    def schoolsearch(self):
        time.sleep(1)
        # driver.implicitly_wait(0.5)
        search = driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#sidolabel')
        select = Select(search)
        select.select_by_visible_text(self.school[0])
        search = driver.find_element_by_css_selector('#crseScCode')
        select = Select(search)
        select.select_by_visible_text(self.school[1])
        search = driver.find_element_by_css_selector('#orgname')
        search.send_keys(str(self.school[2]))
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a')
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input')
        search.send_keys(Keys.ENTER)

    def check(self) :
        time.sleep(1)
        # driver.implicitly_wait(0.5)
        search = driver.find_element_by_css_selector('#user_name_input')
        search.send_keys(str(self.name))
        search = driver.find_element_by_css_selector('#birthday_input')
        search.send_keys(str(self.day))
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.send_keys(Keys.ENTER)

    def num(self) :
        # driver.implicitly_wait(5)
        time.sleep(1)
        search = driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr > td > input')
        search.send_keys(str(self.password))
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.send_keys(Keys.ENTER)

    def selfcheck() :
        driver.implicitly_wait(100)
        Ww(driver,10)
        time.sleep(5)
        search = driver.find_element_by_css_selector('#container > div > section.memberWrap > div:nth-child(2) > ul > li > a') ##container > div > section.memberWrap > div:nth-child(2) > ul > li > a
        search.send_keys(Keys.ENTER)
        search = driver.find_element_by_css_selector('#survey_q1a1')
        search.click()
        search = driver.find_element_by_css_selector('#survey_q2a1')
        search.click()
        search = driver.find_element_by_css_selector('#survey_q3a1')
        search.click()   
        search = driver.find_element_by_css_selector('#btnConfirm')
        search.click()

    
def main() :
    global driver
    start = s
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver',options=option)
    driver.implicitly_wait(1)
    driver.get(URL_login)
    search = driver.find_element_by_css_selector('#btnConfirm2')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    s.schoolsearch(start)
    s.check(start)
    s.num(start)
    s.selfcheck()

    # search = driver.find_element_by_class_name("input_text_common")
    # try:
    #     search = driver.find_element_by_css_selector('#secondaryPwForm > table > tbody > tr > td > input')
    #     search.send_keys(str(password))
    # except :
    time.sleep(1)

    print('end')

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class seter() :


    def __init__(self,name,school1=None,school2=None,school3=None,day=None,password=None):
        self.school = [school1,school2,school3]
        self.name = name
        self.day = day
        self.password = password
        self.row_data = ''
        scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        ]

        json_file_name = 'usekey.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1DkJOReg8aC9BwOY3vfkcW5wmGGt3d0egGejkj7MEZ-Q/edit?usp=sharing'

        doc = gc.open_by_url(spreadsheet_url)

        self.worksheet = doc.worksheet('시트1')
        
        
    def setdata(self) :
        # if not self.school1=='' and self.school2=='' and self.school3=='' and self.day=='' and self.password=='' :
            try :
                self.worksheet.insert_row([self.name, self.school[0], self.school[1], self.school[2], self.day, self.password,], 1)
                log = '데이터 저장 성공'
            except Exception as e:
                log = f'''데이터 저장 실패 log : {e}
                traceback : {traceback.print_exc()}'''
            return str(log)


    def start(self):
        try :
            self.row_data = self.worksheet.row_values(self.worksheet.find(f'{self.name}').row)
        except Exception as e:
            log = f'''데이터 저장 실패 log : {e}
            traceback : {traceback.print_exc()}'''
            return str(log)
        
        try :
            start = s
            s.setdata(start,self.row_data)
            main()
            log = '자가진단 완료'
        except Exception as e:
            log = f'자가진단 실패 log : {e}'
        
        return str(log)



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
    await ctx.send('자가진단 정보 저장 중...')
    log = seter(name,school1,school2,school3,day,password).setdata()
    await ctx.channel.purge(limit=2)
    await ctx.send(str(log))

@bot.command()
async def selfstart(ctx,name) :
    await ctx.send('자가진단 중...')
    log = seter(name).start()
    await ctx.channel.purge(limit=2)
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
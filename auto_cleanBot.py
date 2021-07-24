from os import name
import discord
from discord.channel import TextChannel
from discord.ext import commands
import traceback
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import BadArgument, MissingRequiredArgument
from discord.ext import commands
from discord.guild import Guild
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Ww
from webdriver_manager.chrome import ChromeDriverManager
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from konlpy.tag import Okt

class natural():
    def __init__(self):
        self.okt = Okt()
        self.text = '지금 뭐하고 있어?.'
        self.text_dic = {}

    def text_process(self,text):
        text_nouns = self.okt.nouns(text)

        for i in range(len(text_nouns)) :
            self.text_dic[text_nouns[i]] = True


    def check(self):
        if self.text_dic['뭐'] :
            answer = '지금은 탄생중'
            print(answer)
            return answer
            



bot = commands.Bot(command_prefix='*')
bot.remove_command('help')

com_channel = {}
rolegiver_dic = {}


URL_login, URL_main = 'https://hcs.eduro.go.kr/#/loginHome', 'https://hcs.eduro.go.kr/#/main'

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
        search = driver.find_element_by_css_selector('#container > div > section.memberWrap > div:nth-child(2) > ul > li') ##container > div > section.memberWrap > div:nth-child(2) > ul > li > a
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
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    driver = webdriver.Chrome(
        chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
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
                traceback : {traceback.print_exc()}...'''
            return str(log)


    def start(self):
        try :
            self.row_data = self.worksheet.row_values(self.worksheet.find(f'{self.name}').row)
        except Exception as e:
            log = f'''데이터 저장 실패 log : {e}
            traceback : {traceback.print_exc()}...'''
            return str(log)
        
        try :
            start = s
            s.setdata(start,self.row_data)
            main()
            log = '자가진단 완료'
        except Exception as e:
            log = f'자가진단 실패 log : {e}'
        
        return str(log)


role_check = lambda b : {b[i].name : True for i in range(len(b))} 

@bot.event
async def on_ready():
    print(bot.user.name)
    print('디스코드세계를 돌아다니는 중이에요')
    await bot.change_presence(activity=discord.Game(name='외로운 봇들 귀가시키는 중...'))

@bot.command(name='setchannel',help='역할부여,환영인사 출력을 설정체널에서 합니다',usage='*setchannel 옵션 (필요하다면)제외역할 (필요하다면)부여역할')
@has_permissions()
async def setchannel(ctx,gps,role : discord.Role = None,give_role : discord.Role = None,channelcode=None):
    if ctx.message.author.guild_permissions.manage_messages:
        global com_channel,rolegiver_dic
        guild_id = ctx.guild.id
        if gps == '역할' :
            print(role,'/',give_role)
            rolegiver_dic[guild_id] = [ctx.author.voice.channel,[role, give_role]]  # 채널 구하기 #중복 방지,지급 역할
            if ctx.author.voice and ctx.author.voice.channel: # 채널에 들어가 있는지 파악 # 채널 구하기
                await rolegiver_dic[guild_id][0].connect() # 채널 연결
                await ctx.send(f'지정된 체널 : {rolegiver_dic[guild_id][0]} , 제외역할 : {rolegiver_dic[guild_id][0][0]}, 주어질 역할 : {rolegiver_dic[guild_id][0][1]}')
            else: # 유저가 채널에 없으면
                await ctx.send("채널에 연결되지 않았습니다.") # 출력
        if gps == '환영' :
            com_channel[guild_id] = TextChannel.id
            await ctx.send('저장 완료')

@bot.command(name='setlist', help='역할부여의 설정값이나 환영인사의 설정 체널을 불러옵니다',usage='*setlist (환영/역할)')
async def settinglist(ctx,option=None) :
    if option is not None :
        if option == '역할' :
            embed = discord.Embed(title='settinglist',description='역할지정이 설정된 방입니다',color=0x00aaaa)
            embed.add_field(name='채널 제외역할 지급역할',value=f'{rolegiver_dic}',inline=False)
            await ctx.send(embed=embed)

        if option == '환영' :
            embed = discord.Embed(title='settinglist',description='환영메세지 출력이 설정된 방입니다',color=0x00aaaa)
            embed.add_field(name='채널',value=f'{com_channel}',inline=False)
            await ctx.send(embed=embed)

    
@setchannel.error
async def set_error(ctx,error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('필수 입력 정보를 입력하세요')

@bot.event
async def on_member_join(before,after):
    global com_channel
    guild_id = after.guild.id
    channel = com_channel[guild_id]
    msg = '<@{}>님이 달 저편에 새롭게 착륙하셨습니다 모두 환영해 주세요'.format(str(after.id))
    await channel.send(msg)

@bot.event
async def on_voice_state_update(member,before,after):
    global rolegiver_dic
    guild_id = int(member.guild.id)
    try :
        # print(type(before.channel))
        if len(before.channel.members) == 1 :
            if before.channel.members[0].bot :
                await before.channel.members[0].move_to(None)
    except Exception as e :
        # print(e)
        # print('leave')
        e = e
    print(guild_id)
    try :
        # print(type(after.channel))
        # print(after.channel)
        print(rolegiver_dic)
        print(rolegiver_dic[guild_id])
        if after.channel == rolegiver_dic[guild_id][0] :
            for people in after.channel.members :
                people_roles_dic = role_check(people.roles)
                print(people_roles_dic)
                try :
                    if people_roles_dic[rolegiver_dic[guild_id][1][0]] == False :
                        e=e
                        print('setroler')
                except Exception as e :
                        await people.add_roles(rolegiver_dic[guild_id][1][1])
                        print('given')
    except Exception as e :
        e=e
        # print(e,'error')
        # print('give')
    # print(after.channel.members)
    # print(before.channel.members)

            

@bot.command(name='selfinfo',help='자가진단에 필요한 정보를 입력,저장합니다',usage='*selfinfo 이름 지역 학교급 학교이름 생일(6자리) 비밀번호')
async def selfinfo(ctx,name,school1,school2,school3,day,password):
    await ctx.channel.purge(limit=1)
    await ctx.send('자가진단 정보 저장 중...')
    log = seter(name,school1,school2,school3,day,password).setdata()
    await ctx.send(str(log))

@selfinfo.error
async def selfinfo_error(ctx,error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('자가진단 정보를 전부 입력하세요')

@bot.command(name='selfstart', help='자가진단을 시작합니다',usage='*selfstart 이름')
async def selfstart(ctx,name) :
    await ctx.channel.purge(limit=1)
    await ctx.send('자가진단 중...')
    log = seter(name).start()
    await ctx.send(log)

@selfstart.error
async def start_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('이름을 입력하세요')



@bot.command(name='delmsg',help='메세지를 삭제합니다',usage='*delmsg 삭제할메세지개수')
@has_permissions()
async def delmsg(ctx,num : int):
    await ctx.channel.purge(limit=num + 1)
    await ctx.send(f'{num}개 청소 완료')

@delmsg.error
async def delmsg_error(ctx,error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('삭제할 메세지 개수를 입력하세요')
    if isinstance(error, BadArgument):
        await ctx.send('숫자로 입력하세요')

@bot.command(name='version',help='봇의 버전을 출력합니다',usage='*version')
async def version(ctx):
    await ctx.send('now verion : 2.2.2')

@bot.command(name='ping',help='핑을 출력합니다',usage='*ping')
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency + 1000)}ms')

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
    embed.add_field(name='setchannel',value='특정 행동을 할 방을 지정해요 (역할, 환영)',inline=False)
    embed.add_field(name='selfinfo',value='자가진단 정보를 입력해요',inline=False)
    embed.add_field(name='selfstart',value='자가진단을 시작해요(1회)',inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def chelp(ctx, m):
    if m == 'selfinfo' :
        embed = discord.Embed(title='chelp',description='명령어 사용 도움말',color=0x00aaaa)
        embed.add_field(name='자가진단 정보를 입력해요',value='selfinfo 이름 지역 학교급 학교이름 생일(6자리) 비밀번호',inline=False)
        await ctx.send(embed=embed)
    if m == 'setchannel' :
        embed = discord.Embed(title='chelp',description='명령어 사용 도움말',color=0x00aaaa)
        embed.add_field(name='특정 행동을 할 방을 지정해요',value='역할, 환영',inline=False)
        embed.add_field(name='역할',value='음성채널에 들어간 상태로 사용해요 *setchannel 환영 지급제외역할 지급할역할',inline=False)
        embed.add_field(name='환영',value='신규인원 환영메세지를 출력해요',inline=False)
        await ctx.send(embed=embed)

@bot.command(name="도움")
async def help_command(self, ctx, func=None):
    if func is None:
        embed = discord.Embed(title="Python Bot 도움말", description="접두사는 `!` 입니다.") #Embed 생성
        cog_list = ["Core"] # Cog 리스트 추가
        for x in cog_list: # cog_list에 대한 반복문
            cog_data = self.bot.get_cog(x) # x에 대해 Cog 데이터를 구하기
            command_list = cog_data.get_commands() # cog_data에서 명령어 리스트 구하기
            embed.add_field(name=x, value=" ".join([c.name for c in command_list]), inline=True) # 필드 추가
        await ctx.send(embed=embed) # 보내기
    else: # func가 None이 아니면
        command_notfound = True # 이걸 어떻게 쓸지 생각해보세요!
        for _title, cog in self.bot.cogs.items(): # title, cog로 item을 돌려주는데 title은 필요가 없습니다.
            if not command_notfound: # False면
                break # 반복문 나가기

            else: # 아니면
                for title in cog.get_commands(): # 명령어를 아까처럼 구하고 title에 순차적으로 넣습니다.
                    if title.name == func: # title.name이 func와 같으면
                        cmd = self.bot.get_command(title.name) # title의 명령어 데이터를 구합니다.
                        embed = discord.Embed(title=f"명령어 : {cmd}", description=cmd.help) # Embed 만들기
                        embed.add_field(name="사용법", value=cmd.usage) # 사용법 추가
                        await ctx.send(embed=embed) # 보내기
                        command_notfound = False
                        break # 반복문 나가기
                    else:
                        command_notfound = True

bot.run("ODU0NjU3ODExMjE5NDgwNjA2.YMnIHA.KCGX_Z1UzkNSPjhPXWSmnuV7q3c")
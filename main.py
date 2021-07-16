from selfauto import s,main

f = open('info.txt','r')
data = f.readlines()

if len(data) != 0 :
    print(data)
    school = [data[0].rstrip('\n'),data[1].rstrip('\n'),data[2].rstrip('\n')]
    name = data[3].rstrip('\n')
    day = data[4].rstrip('\n')
    password = data[5].rstrip('\n')

else :
    school = ['','','']
    for i in range(len(school)) :
        school[i] = str(input('학교 지역(예 : 경기도),급(예 : 중학교),이름(예 : 나지중학교) 순으로 입력하세요 >>>'))
    name = str(input('이름을 입력하세요 >>>'))
    day = str(input('생년월일을 6자리로 입력하세요 >>>'))
    password = str(input('비밀번호를 입력하세요 >>>'))
    f = open('info.txt','w')
    f.write(f'{school[0]}\n')
    f.write(f'{school[1]}\n')
    f.write(f'{school[2]}\n')
    f.write(f'{name}\n')
    f.write(f'{day}\n')
    f.write(f'{password}\n')



start = s
s.setdata(start,password,school,name,day)
main()



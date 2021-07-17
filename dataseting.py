from selfauto import s,main


class seter() :
    def __init__(self,name,school1=None,school2=None,school3=None,day=None,password=None):
        self.school1 = school1
        self.school2 = school2
        self.school3 = school3
        self.name = name
        self.day = day
        self.password = password
        
        
        

    def start(self):
        f = open(f'info_{self.name}.txt','r')
        data = f.readlines()

        if len(data) != 0 :
            print(data)
            self.school = [data[0].rstrip('\n'),data[1].rstrip('\n'),data[2].rstrip('\n')]
            self.name = data[3].rstrip('\n')
            self.day = data[4].rstrip('\n')
            self.password = data[5].rstrip('\n')

        else :
            # school = ['','','']
            # for i in range(len(school)) :
            #     school[i] = str(input('학교 지역(예 : 경기도),급(예 : 중학교),이름(예 : 나지중학교) 순으로 입력하세요 >>>'))
            # name = str(input('이름을 입력하세요 >>>'))
            # day = str(input('생년월일을 6자리로 입력하세요 >>>'))
            # password = str(input('비밀번호를 입력하세요 >>>'))
            f = open(f'info_{self.name}.txt','w')
            f.write(f'{self.school[0]}\n')
            f.write(f'{self.school[1]}\n')
            f.write(f'{self.school[2]}\n')
            f.write(f'{self.name}\n')
            f.write(f'{self.day}\n')
            f.write(f'{self.password}\n')



        start = s
        s.setdata(start,self.password,self.school,self.name,self.day)
        main()



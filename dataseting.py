import re
from selfauto import s,main
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class seter() :


    def __init__(self,name,school1=None,school2=None,school3=None,day=None,password=None):
        self.school1 = school1
        self.school2 = school2
        self.school3 = school3
        self.name = name
        self.day = day
        self.password = password
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
        if not self.school1==None&self.school2==None&self.school3==None&self.day==None&self.password==None :
            try :
                self.worksheet.insert_row([self.name, self.school[0], self.school[1], self.school[2], self.day, self.password,], 1)
                return '데이터 저장 성공'
            except :
                return '데이터 저장 실패'


    def start(self):
        try :
            self.row_data = self.worksheet.row_values(self.worksheet.find(f'{self.name}'))
        except :
            return '데이터 불러오기 실패'
        
        try :
            start = s
            s.setdata(start,self.row_data)
            main()
            return '자가진단 완료'
        except :
            return '자가진단 실패'


import gspread 
from oauth2client.service_account import ServiceAccountCredentials

class TransactionSheet:
    def __init__(self):
      scope = ['https://www.googleapis.com/auth/drive']
      creds = ServiceAccountCredentials.from_json_keyfile_name('pmoney_client.json', scope)
      client = gspread.authorize(creds)
      sheet = client.open("pymoney")
      
      self.sheet = sheet.get_worksheet(0)
      
    def getAll(self):
        return self.sheet.get_all_records()
    def add(self,transaction):
        self.sheet.append_row([transaction.title, transaction.value, transaction.type, transaction.category])
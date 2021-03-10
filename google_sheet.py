from openpyxl import load_workbook
import sys, os, pickle
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os, pickle, re


if len(sys.argv) < 4:
    print("python 3.py [file name] [coordinate column name] [text column name]")
    exit()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
file_name = sys.argv[1]
coordinate_col_name = sys.argv[2]
text_col_name = sys.argv[3]
col_num = -1
coordinate_col_num = -1
text_col_num = -1
print(coordinate_col_name)
print(text_col_name)

creds = None
sheet_id =  file_name
sheet_name =  "Hoja 1"
sheet_range =  "A1:I10000"
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=21000)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_name + "!" + sheet_range).execute()
values = result.get('values', [])
resp = ""
if values:
    # Get Header 
    for col in values[0]:
        col_num += 1
        if col == coordinate_col_name: coordinate_col_num = col_num
        if col == text_col_name: text_col_num = col_num
    
    if coordinate_col_num == -1 or text_col_num == -1: 
        print("Wrong Column Names")
        exit()

    for row in values[1:]:
        coordinate = row[coordinate_col_num]
        if coordinate == None : continue
        if coordinate.strip() == "": continue
        text = row[text_col_num].strip()
        print(coordinate + " :: " + text)
        
else:
    print("Wrong Google Sheet Info")



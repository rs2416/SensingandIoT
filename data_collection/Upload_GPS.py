#File pushes data from the CSV of GPS and mobile speed data, then deletes the CSV

from googleapiclient.discovery import build
import pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive and Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

SPREADSHEET_ID = '1W1ehs8Acke7TyA7maPOToAPvqGm-Y9pCDQZV74RwUwU' # Get this one from the link in browser
worksheet_name = 'Tracks'
path_to_csv = 'CSVs/tracks.csv'

def find_sheet_id_by_name(sheet_name):
    sheets_with_properties = API \
        .spreadsheets() \
        .get(spreadsheetId=SPREADSHEET_ID, fields='sheets.properties') \
        .execute() \
        .get('sheets')

    for sheet in sheets_with_properties:
        if 'title' in sheet['properties'].keys():
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']
            
def push_csv_to_gsheet(csv_path, sheet_id):
    
    gc = pygsheets.authorize(service_file='client_secret.json') #authorisation
    worksheet = gc.open('Tracks').sheet1 #opens the first sheet in "Tracks"
    cells = worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    end_row = len(cells) #index number for an empty row
    
    with open(csv_path, 'r') as csv_file:
        csvContents = csv_file.read()
    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": end_row, #appends to index number for an empty row
                    "columnIndex": "0", 
                },
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]
    }
    request = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body)
    response = request.execute()
    return response

API = build('sheets', 'v4', credentials=creds)

push_csv_to_gsheet(
    csv_path=path_to_csv,
    sheet_id=find_sheet_id_by_name(worksheet_name)
)

#Delete track file after upload
os.unlink('CSVs/tracks.csv')
print('file removed')


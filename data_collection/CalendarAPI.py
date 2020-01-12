#File returns events for the next 15 hours (start time, end time, summary, location) using Google Calendar API, then the events are pushed to Google Sheets using the API.

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive and Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("CalendarData").sheet1
SCOPES = ['https://www.googleapis.com/auth/calendar.events.readonly']

def main():
    creds = None
    #The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    
    #Identify the current time
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #Set event collection limit (today at 23:59 pm)
    t = datetime.time(23, 59, 0)
    d = datetime.date.today()
    dt = datetime.datetime.combine(d, t)
    dtt = str(dt.isoformat() + 'Z')

    #Collect events that take place from now til 23:59 tonight
    events_result = service.events().list(calendarId='primary', timeMin= now, singleEvents=True, orderBy='startTime', timeMax = dtt).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        i = 0
        i = i + 1
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        outputstring = (str(start) + "   " + str(end) + "   " + str(event['summary'])) 
        index = i
        startstr = (str(start)) 
        endstr = (str(end))
        summarystr = (str(event['summary']))
        
        #Insert information in googlesheets (start time, end time, summary, location)
        information = [startstr,endstr,summarystr]
        try:
            information = [startstr,endstr,summarystr, (str(event['location']))]
        except: 
            print('no location')
            information = [startstr,endstr,summarystr]
        
        sheet.insert_row(information, i )

if __name__ == '__main__':
    main()


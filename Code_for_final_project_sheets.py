#!/usr/bin/env python
# coding: utf-8

# In[2]:


from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'first_call.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '18X-zRp1mvsZQoIFuy4pC8mdq1jQnpXR_NWYar8Pgi_Y'

  
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Sheet1!A1:Q302").execute()
values = result.get('values', [])

import pandas as pd

df = pd.DataFrame(data=values)


# In[ ]:





# In[ ]:




